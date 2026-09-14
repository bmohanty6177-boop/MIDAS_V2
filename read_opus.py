"""
read_opus.py
============
Python equivalent of read.opus.R (Author: Andrew Sila, ICRAF/CGIAR)
Converted for IISS Bhopal by Claude — January 2025

Reads Bruker OPUS binary spectral files (.0, .1, .2 etc.) produced by:
  - Bruker Alpha (MIR, ZnSe or standard beam splitter)
  - Bruker Tensor-27 / HTS-XT (MIR)
  - Bruker MPA (NIR)

Output: a dict with metadata + absorbance values on the ICRAF wavenumber grid.

Dependencies:
    pip install numpy scipy
"""

import os
import struct
import numpy as np
from scipy.interpolate import CubicSpline
from datetime import datetime

# ── ICRAF instrument wavenumber grids ─────────────────────────────────────────
ICRAF_GRIDS = {
    # (lxv, fxv, npt) — all reversed to high→low after construction
    "ten-mir": (599.76,  7497.964, 3578),   # Tensor-27 / HTS-XT
    "alp-mir": (399.387991, 3998.12872, 2542),  # Alpha (KBr beam splitter)
    "alp-znse":(499.8151,   3996.4810, 1714),   # Alpha (ZnSe beam splitter)
    "mpa-nir": (3598.69, 12493.2,   2307),   # MPA NIR
}

def _icraf_grid(key):
    """Return ICRAF wavenumber array (high → low) for given instrument key."""
    lxv, fxv, npt = ICRAF_GRIDS[key]
    return np.linspace(lxv, fxv, npt)[::-1]


# ── Low-level binary helpers ───────────────────────────────────────────────────

def _find_tag(tag: str, raw: bytes):
    """Return list of all 0-based byte positions where `tag` appears in `raw`."""
    tag_b = tag.encode("latin-1")
    pos, positions = 0, []
    while True:
        p = raw.find(tag_b, pos)
        if p == -1:
            break
        positions.append(p)
        pos = p + 1
    return positions


def _read_str(raw: bytes, offset: int, nbytes: int) -> str:
    """Read a null-terminated Latin-1 string from raw bytes."""
    chunk = raw[offset: offset + nbytes]
    out = ""
    for b in chunk:
        if b == 0:
            break
        if 32 <= b < 127:       # printable ASCII only
            out += chr(b)
    return out.strip()


def _read_int16(raw: bytes, tag_pos: int) -> int:
    """Read int16 at (tag_pos + 6), matching R's grepRaw+5 → 1-based → 0-based."""
    # R: z <- grepRaw(tag)[1]+5  (1-based result + 5)
    # R readRaw offset is 0-based → Python offset = tag_pos + 6
    return struct.unpack_from("<h", raw, tag_pos + 6)[0]


def _read_float64(raw: bytes, tag_pos: int) -> float:
    """Read float64 at (tag_pos + 8)."""
    return struct.unpack_from("<d", raw, tag_pos + 8)[0]


def _read_int32(raw: bytes, tag_pos: int) -> int:
    """Read int32 at (tag_pos + 8)."""
    return struct.unpack_from("<i", raw, tag_pos + 8)[0]


# ── OPUS single-file reader ───────────────────────────────────────────────────

def read_opus(file_path: str, speclib: str = "ICRAF") -> dict:
    """
    Read a single Bruker OPUS binary file.

    Parameters
    ----------
    file_path : str
        Path to the OPUS file (e.g. 'Kar1/iis_004224.0').
    speclib : str
        'ICRAF' — interpolate onto the standard ICRAF wavenumber grid (default).
        'raw'   — return the native instrument wavenumbers without resampling.

    Returns
    -------
    dict with keys:
        SAMPLEID, Material, Datetime, Zero_filling, Resolution, LWN,
        wavenumbers (np.ndarray), absorbance (np.ndarray),
        instrument (str), grid_key (str)

    Raises
    ------
    ValueError  if the file format is not recognised.
    FileNotFoundError  if the file does not exist.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(file_path, "rb") as fh:
        raw = fh.read()

    # ── 1. Instrument identification ──────────────────────────────────────────
    ins_positions = _find_tag("INS", raw)
    src_positions = _find_tag("SRC", raw)
    bms_positions = _find_tag("BMS", raw)

    ins = _read_str(raw, ins_positions[-1] + 8, 3)   # e.g. 'Alp'
    src = _read_str(raw, src_positions[0]  + 8, 3)   # e.g. 'MIR'
    bms = _read_str(raw, bms_positions[0]  + 8, 4)   # e.g. 'ZnSe'

    instr_range = f"{ins.lower()}-{src.lower()}"     # 'alp-mir'

    # Map to ICRAF grid key
    if "ten" in instr_range or "off" in instr_range:
        grid_key = "ten-mir"
    elif "alp" in instr_range:
        grid_key = "alp-znse" if bms == "ZnSe" else "alp-mir"
    elif "mpa" in instr_range:
        grid_key = "mpa-nir"
    else:
        raise ValueError(
            f"Unknown instrument: INS={ins!r}, SRC={src!r}, BMS={bms!r}. "
            "Supported: Tensor-27/HTS-XT (MIR), Alpha (MIR), MPA (NIR)."
        )

    # Wavenumber prefix used in column names  (m=Tensor, a=Alpha, n=MPA)
    pref = {"ten-mir": "m", "alp-mir": "a", "alp-znse": "a", "mpa-nir": "n"}[grid_key]

    # ── 2. Metadata ───────────────────────────────────────────────────────────
    # Sample name (SNM) ─ format: "NNNNNN;LAB;MATERIAL"
    snm_pos = _find_tag("SNM", raw)[0]
    snm_str = _read_str(raw, snm_pos + 8, 22)
    parts = snm_str.split(";")
    if len(parts) >= 2:
        sampleid = parts[1] + parts[0]                       # e.g. iis004224
        sampleid = sampleid[:3].lower() + sampleid[3:]
        material = parts[2].strip() if len(parts) > 2 else ""
    else:
        sampleid = snm_str
        material = ""

    # Date and time
    dat_pos = _find_tag("DAT", raw)[0]
    tim_positions = _find_tag("TIM", raw)
    dat_str = _read_str(raw, dat_pos + 8, 10)                # '02/01/2024'
    tim_str = _read_str(raw, tim_positions[1] + 8, 12)       # '11:29:10.230'
    tim_str_clean = tim_str.split(".")[0]                     # '11:29:10'
    datetime_str = f"{dat_str} {tim_str_clean}"

    # Instrument parameters
    zff_pos = _find_tag("ZFF", raw)[0]
    res_pos = _find_tag("RES", raw)[0]
    lwn_pos = _find_tag("LWN", raw)[0]

    zero_filling = _read_int16(raw, zff_pos)
    resolution   = _read_int16(raw, res_pos)
    lwn          = _read_float64(raw, lwn_pos + 0)  # LWN uses +8 directly

    # ── 3. Spectral data ──────────────────────────────────────────────────────
    # Native wavenumbers from NPT/FXV/LXV (3rd occurrence, index 2)
    npt_positions = _find_tag("NPT", raw)
    fxv_positions = _find_tag("FXV", raw)
    lxv_positions = _find_tag("LXV", raw)

    npt1 = _read_int32(raw, npt_positions[2])
    fxv  = _read_float64(raw, fxv_positions[2])
    lxv  = _read_float64(raw, lxv_positions[2])
    wn_native = np.linspace(lxv, fxv, npt1)[::-1]  # high → low

    # Find spectral data blocks via END tag positions
    end_positions = _find_tag("END", raw)
    # R: offs <- sapply(5:10, function(x){end[x]}) → Python: end[4:10]
    # R: readRaw(offset=offs.f-4) → Python data start = end_pos + 8
    nbytes_f = npt1 * 4

    best_arr, best_max = None, -1.0
    for idx in range(4, min(10, len(end_positions))):
        data_start = end_positions[idx] + 8   # matches R's offs.f - 4 (1-based)
        if data_start + nbytes_f > len(raw):
            continue
        arr = np.array(struct.unpack_from(f"<{npt1}f", raw, data_start))
        arr_clean = np.where(np.isfinite(arr), arr, 0.0)
        mx = float(arr_clean.max())
        if 0.1 < mx < 5.0 and mx > best_max:  # physically reasonable absorbance
            best_max = mx
            best_arr = arr_clean

    if best_arr is None:
        raise ValueError(f"No valid spectral block found in {file_path}")

    # ── 4. Resample to ICRAF grid ─────────────────────────────────────────────
    if speclib == "ICRAF":
        wb = _icraf_grid(grid_key)
        # Natural cubic spline, same as R's spline(..., method='natural')
        cs = CubicSpline(wn_native[::-1], best_arr[::-1], bc_type="natural")
        spectra_out = cs(wb[::-1])[::-1]
        wavenumbers_out = wb
    else:
        spectra_out   = best_arr
        wavenumbers_out = wn_native

    return {
        "SAMPLEID":     sampleid,
        "Material":     material,
        "Datetime":     datetime_str,
        "Zero_filling": zero_filling,
        "Resolution":   resolution,
        "LWN":          lwn,
        "instrument":   instr_range,
        "grid_key":     grid_key,
        "prefix":       pref,
        "wavenumbers":  wavenumbers_out,
        "absorbance":   spectra_out,
    }


# ── Batch converter ────────────────────────────────────────────────────────────

def convert_folder_to_csv(
    opus_folder: str,
    output_csv: str,
    speclib: str = "ICRAF",
    verbose: bool = True,
) -> "pd.DataFrame":
    """
    Read all OPUS files in `opus_folder` and save a CSV matching the R output.

    Parameters
    ----------
    opus_folder : str   Path to folder containing .0 / .1 / .2 … OPUS files.
    output_csv  : str   Path for the output CSV file.
    speclib     : str   'ICRAF' or 'raw' (see read_opus).
    verbose     : bool  Print progress for each file.

    Returns
    -------
    pandas.DataFrame  — same structure as Kar1.csv produced by R.
    """
    import pandas as pd
    import re

    # Find files ending in a digit (same pattern as R's pattern=".[0-9]$")
    all_files = sorted(
        f for f in os.listdir(opus_folder)
        if re.search(r"\.\d+$", f)
    )
    if not all_files:
        raise FileNotFoundError(f"No OPUS files found in {opus_folder}")

    rows = []
    for i, fname in enumerate(all_files, 1):
        fpath = os.path.join(opus_folder, fname)
        try:
            result = read_opus(fpath, speclib=speclib)
            if verbose:
                print(f"[{i:>4}/{len(all_files)}] Converting {fname} ✓")

            # Build wavenumber column names  e.g. 'a3996.5'
            wn_labels = [
                f"{result['prefix']}{round(w, 1):g}"
                for w in result["wavenumbers"]
            ]

            row = {
                "SAMPLEID":     result["SAMPLEID"],
                "Material":     result["Material"],
                "Datetime":     result["Datetime"],
                "Zero.filling": result["Zero_filling"],
                "Resolution":   result["Resolution"],
                "LWN":          result["LWN"],
            }
            for label, val in zip(wn_labels, result["absorbance"]):
                row[label] = val

            rows.append(row)

        except Exception as exc:
            print(f"[{i:>4}/{len(all_files)}] WARNING: {fname} — {exc}")

    if not rows:
        raise RuntimeError("No files were successfully converted.")

    df = pd.DataFrame(rows)

    # Save CSV
    os.makedirs(os.path.dirname(os.path.abspath(output_csv)), exist_ok=True)
    df.to_csv(output_csv, index=False)
    if verbose:
        print(f"\n✓ Saved {len(df)} spectra → {output_csv}")
        print(f"  Shape: {df.shape[0]} rows × {df.shape[1]} columns")

    return df


# ── CLI entry point ────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Convert Bruker OPUS files to CSV (Python port of read.opus.R)"
    )
    parser.add_argument("opus_folder", help="Folder containing OPUS files")
    parser.add_argument("output_csv",  help="Output CSV file path")
    parser.add_argument("--speclib", default="ICRAF",
                        help="'ICRAF' (default) or 'raw'")
    parser.add_argument("--quiet", action="store_true", help="Suppress progress output")
    args = parser.parse_args()

    convert_folder_to_csv(
        opus_folder=args.opus_folder,
        output_csv=args.output_csv,
        speclib=args.speclib,
        verbose=not args.quiet,
    )
