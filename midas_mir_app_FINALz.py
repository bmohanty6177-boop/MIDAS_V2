# ── Modern bright green CSS ──────────────────────────────────────────────
_CSS = """
<style>
/* ── Google Font ─────────────────────────────────────────────────── */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
    font-family: 'Inter', sans-serif !important;
    background: linear-gradient(160deg, #f0f4ff 0%, #eaf0fb 60%, #f5f0ff 100%) !important;
}

.main .block-container {
    background: transparent !important;
    padding-top: 1rem !important;
    max-width: 1200px !important;
}

/* ── Sidebar — deep navy ─────────────────────────────────────────── */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f1f4a 0%, #0a1530 100%) !important;
    border-right: 3px solid #c9a227 !important;
}
section[data-testid="stSidebar"] * { color: #dde6ff !important; }
section[data-testid="stSidebar"] .stMarkdown h3 {
    color: #c9a227 !important;
    font-size: 13px !important;
    letter-spacing: 1px !important;
    text-transform: uppercase !important;
    border-bottom: 1px solid #1e3070 !important;
    padding-bottom: 6px !important;
}
section[data-testid="stSidebar"] .stMarkdown p {
    font-size: 13px !important;
    line-height: 1.7 !important;
    color: #b8c8f0 !important;
}
section[data-testid="stSidebar"] hr { border-color: #1e3070 !important; }

/* ── Section headings ────────────────────────────────────────────── */
h3 {
    font-size: 18px !important;
    font-weight: 700 !important;
    color: #0f1f4a !important;
    letter-spacing: 0.3px !important;
    margin-bottom: 12px !important;
}

/* ── File uploader ───────────────────────────────────────────────── */
[data-testid="stFileUploader"] {
    border: 2.5px dashed #3a5fd9 !important;
    border-radius: 20px !important;
    background: rgba(255,255,255,0.92) !important;
    box-shadow: 0 2px 16px rgba(15,31,74,0.08) !important;
    transition: all 0.25s ease !important;
    padding: 8px !important;
}
[data-testid="stFileUploader"]:hover {
    border-color: #0f1f4a !important;
    box-shadow: 0 4px 24px rgba(15,31,74,0.18) !important;
}

/* ── Buttons ─────────────────────────────────────────────────────── */
.stButton > button {
    font-family: 'Inter', sans-serif !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    font-size: 14px !important;
    transition: all 0.2s ease !important;
    letter-spacing: 0.3px !important;
}
.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #0f1f4a 0%, #3a5fd9 100%) !important;
    border: none !important;
    color: #ffffff !important;
    box-shadow: 0 4px 18px rgba(15,31,74,0.40) !important;
    font-size: 15px !important;
    padding: 0.65rem 2.5rem !important;
    letter-spacing: 0.5px !important;
}
.stButton > button[kind="primary"]:hover {
    background: linear-gradient(135deg, #071230 0%, #2a4fc9 100%) !important;
    box-shadow: 0 8px 28px rgba(10,21,48,0.55) !important;
    transform: translateY(-1px) !important;
}
.stButton > button[kind="secondary"] {
    background: #ffffff !important;
    border: 2px solid #3a5fd9 !important;
    color: #0f1f4a !important;
}
.stButton > button[kind="secondary"]:hover {
    background: #f0f4ff !important;
    border-color: #0f1f4a !important;
}

/* ── Property tags (multiselect) ─────────────────────────────────── */
[data-baseweb="tag"] {
    border-radius: 30px !important;
    font-weight: 600 !important;
    font-size: 12px !important;
    background: linear-gradient(135deg, #0f1f4a, #3a5fd9) !important;
    color: white !important;
    box-shadow: 0 2px 6px rgba(15,31,74,0.25) !important;
    padding: 2px 10px !important;
}

/* ── Results table ───────────────────────────────────────────────── */
[data-testid="stDataFrame"] {
    border-radius: 16px !important;
    overflow: hidden !important;
    border: none !important;
    box-shadow: 0 4px 24px rgba(15,31,74,0.12) !important;
}

/* ── Metric containers ───────────────────────────────────────────── */
[data-testid="metric-container"] {
    background: linear-gradient(135deg, #e8eeff, #dde6ff) !important;
    border: 1.5px solid #3a5fd9 !important;
    border-radius: 14px !important;
    padding: 16px !important;
    box-shadow: 0 2px 10px rgba(15,31,74,0.10) !important;
}

/* ── Alert boxes ─────────────────────────────────────────────────── */
[data-testid="stAlert"] {
    border-radius: 12px !important;
    font-size: 14px !important;
}

/* ── Input number ────────────────────────────────────────────────── */
[data-testid="stNumberInput"] input {
    border-radius: 10px !important;
    border: 1.5px solid #3a5fd9 !important;
    font-family: 'Inter', sans-serif !important;
}

/* ── Expanders ───────────────────────────────────────────────────── */
details {
    border: 1.5px solid #c8d4f8 !important;
    border-radius: 12px !important;
    background: rgba(255,255,255,0.9) !important;
    margin-bottom: 8px !important;
}
details summary {
    font-weight: 600 !important;
    color: #0f1f4a !important;
    padding: 10px 16px !important;
    font-size: 14px !important;
}

/* ── Download buttons ────────────────────────────────────────────── */
[data-testid="stDownloadButton"] button {
    border-radius: 10px !important;
    font-weight: 600 !important;
    background: linear-gradient(135deg, #e8eeff, #dde6ff) !important;
    border: 2px solid #3a5fd9 !important;
    color: #0f1f4a !important;
    transition: all 0.2s ease !important;
}
[data-testid="stDownloadButton"] button:hover {
    background: linear-gradient(135deg, #dde6ff, #c8d8ff) !important;
    box-shadow: 0 4px 14px rgba(15,31,74,0.20) !important;
}

/* ── Multiselect ─────────────────────────────────────────────────── */
.stMultiSelect [data-baseweb="select"] > div:first-child {
    border-radius: 12px !important;
    border: 1.5px solid #3a5fd9 !important;
    background: rgba(255,255,255,0.95) !important;
    min-height: 48px !important;
}

/* ── Progress bar ────────────────────────────────────────────────── */
[data-testid="stProgress"] > div > div {
    background: linear-gradient(90deg, #0f1f4a, #3a5fd9) !important;
    border-radius: 10px !important;
}

/* ── HR divider ──────────────────────────────────────────────────── */
hr {
    border: none !important;
    border-top: 2px solid #c8d4f8 !important;
    margin: 16px 0 !important;
}

/* ── Caption text ────────────────────────────────────────────────── */
.stCaption {
    color: #3a5fd9 !important;
    font-size: 12px !important;
}
</style>
"""
"""
MIDAS MIR — Mid-Infrared Spectroscopy Analysis System
ICAR-IISS Bhopal × ICRAF
"""

import streamlit as st
import pandas as pd
import numpy as np
import joblib, json, os, gc, tempfile, warnings
from scipy.signal import savgol_filter
import plotly.graph_objs as go
import plotly.express as px
warnings.filterwarnings('ignore')
import base64, io, datetime

ICAR_INFO = """**Indian Council of Agricultural Research (ICAR)** — Established 16 July 1929. Autonomous body under Ministry of Agriculture & Farmers Welfare, Govt. of India. HQ: New Delhi. With 113 ICAR institutes and 74 agricultural universities, it is one of the largest national agricultural systems in the world. ICAR enabled India to increase foodgrain production 6.21x, horticulture 11.53x, fish 21.61x, milk 13.01x and eggs 70.74x since 1950-51. [Visit ICAR](https://icar.org.in)"""

ICRAF_INFO = """**World Agroforestry (ICRAF)** — Centre of science and development excellence harnessing benefits of trees for people and the environment. The only institution doing globally significant agroforestry research across the developing tropics. Vision: an equitable world where all people have viable livelihoods supported by healthy and productive landscapes. HQ: Nairobi, Kenya. Guided by CGIAR and the SDGs. [Visit ICRAF](https://www.worldagroforestry.org)"""


st.set_page_config(
    page_title="MIDAS MIR — IISS Bhopal",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ── Custom CSS ────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* Background tint — warm soil/nature feel */
.stApp {
    background: linear-gradient(160deg, #f4f9f0 0%, #faf6ee 60%, #f0f4ea 100%);
}

/* Sidebar background */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #e8f0e3 0%, #f0ece0 100%);
    border-right: 2px solid #c8d8c0;
}

/* Main content area card feel */
.main .block-container {
    background: transparent;
    padding-top: 1.5rem;
}

/* Upload area — rounded, dashed border */
[data-testid="stFileUploader"] {
    border: 2.5px dashed #7aab6e !important;
    border-radius: 18px !important;
    background: #f0f8ec !important;
    padding: 18px !important;
    transition: border-color 0.2s;
}
[data-testid="stFileUploader"]:hover {
    border-color: #4a8c3f !important;
    background: #e8f5e4 !important;
}

/* Multiselect tags — we override via group colors using JS not possible,
   but we style the container */
[data-testid="stMultiSelect"] {
    border-radius: 12px;
}


/* Buttons */
.stButton > button {
    border-radius: 10px !important;
    font-weight: 500 !important;
}
.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #3d7a34, #5a9e50) !important;
    border: none !important;
    color: white !important;
}
.stButton > button[kind="primary"]:hover {
    background: linear-gradient(135deg, #2d6025, #4a8e40) !important;
}

/* Metric boxes */
[data-testid="metric-container"] {
    background: #e8f4e4;
    border: 1px solid #b8d8b0;
    border-radius: 10px;
    padding: 12px;
}

/* Section headers */
h3 {
    color: #2d5a27 !important;
    border-bottom: 2px solid #c8e0c0;
    padding-bottom: 6px;
}

/* Success/info boxes */
.stSuccess {
    border-radius: 10px !important;
    border-left: 4px solid #4a8c3f !important;
}
.stInfo {
    border-radius: 10px !important;
}
.stWarning {
    border-radius: 10px !important;
}

/* Dataframe */
[data-testid="stDataFrame"] {
    border-radius: 12px;
    overflow: hidden;
    border: 1px solid #d0e4c8;
}

/* Divider */
hr {
    border-color: #c8d8c0 !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown(_CSS, unsafe_allow_html=True)

try:
    from read_opus import read_opus
except ImportError:
    st.error("read_opus.py not found. Place it in the same folder as this app.")
    st.stop()

# ── Auto-download models from Google Drive on first run (for Streamlit Cloud) ──
@st.cache_resource(show_spinner="Downloading models from Google Drive...")
def ensure_models():
    models_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'models')
    registry   = os.path.join(models_dir, 'mir_model_registry.json')

    # IMPORTANT: don't just check for the registry.json — that small file is
    # often committed to git directly, so its presence doesn't tell us
    # whether the (much larger, gitignored) .pkl model files were actually
    # downloaded from Drive. Check for at least one real model file instead.
    existing_pkls = []
    if os.path.isdir(models_dir):
        existing_pkls = [f for f in os.listdir(models_dir) if f.endswith('.pkl')]

    if os.path.exists(registry) and len(existing_pkls) > 0:
        return True

    try:
        import gdown
        FOLDER_ID = '1t7E867ThQc1vpSClKLoBSwzW-tzn0oyk'
        os.makedirs(models_dir, exist_ok=True)
        gdown.download_folder(id=FOLDER_ID, output=models_dir,
                              quiet=False, use_cookies=False)
    except Exception as e:
        st.error(f'Could not download models: {e}')
        return False

    # Verify the download actually produced .pkl files — gdown can "succeed"
    # (no exception) while silently skipping files due to Drive rate limits
    # or permission issues, leaving the folder empty or incomplete.
    final_pkls = [f for f in os.listdir(models_dir) if f.endswith('.pkl')] if os.path.isdir(models_dir) else []
    if not final_pkls:
        st.error(
            "Model download from Google Drive completed but no .pkl files were found. "
            "This usually means Google Drive rate-limited the download or the folder "
            "permissions changed. Check that the Drive folder is still shared as "
            "'Anyone with the link — Viewer' and try again."
        )
        return False
    return True

ensure_models()

MODELS_DIR = os.path.join(os.path.dirname(__file__), 'models')

PROPERTY_META = {
    'pH':   {'unit': '',        'label': 'pH',   'icon': '🧪', 'color': '#e8a838'},
    'EC':   {'unit': 'dS/m',   'label': 'EC',   'icon': '⚡',  'color': '#e8a838'},
    'SOC':  {'unit': '%',      'label': 'SOC',  'icon': '🌿', 'color': '#4a8c3f'},
    'Av-N': {'unit': 'kg/ha',  'label': 'Av-N', 'icon': '🌱', 'color': '#3a7a6e'},
    'Av_P': {'unit': 'kg/ha',  'label': 'Av-P', 'icon': '🌱', 'color': '#3a7a6e'},
    'Av_K': {'unit': 'kg/ha',  'label': 'Av-K', 'icon': '🌱', 'color': '#3a7a6e'},
    'FC':   {'unit': '%',      'label': 'FC',   'icon': '💧', 'color': '#3a6e9e'},
    'PWP':  {'unit': '%',      'label': 'PWP',  'icon': '💧', 'color': '#3a6e9e'},
    'clay': {'unit': '%',      'label': 'Clay', 'icon': '🪨', 'color': '#8b6b4a'},
    'silt': {'unit': '%',      'label': 'Silt', 'icon': '🪨', 'color': '#8b6b4a'},
    'sand': {'unit': '%',      'label': 'Sand', 'icon': '🪨', 'color': '#8b6b4a'},
    'TC':   {'unit': '%',      'label': 'TC',   'icon': '🌿', 'color': '#4a8c3f'},
    'TN':   {'unit': '%',      'label': 'TN',   'icon': '🌿', 'color': '#4a8c3f'},
    'Cu':   {'unit': 'mg/kg',  'label': 'Total Cu',  'icon': '⚗️',  'color': '#b05a2a'},
    'Zn':   {'unit': 'mg/kg',  'label': 'Total Zn',  'icon': '⚗️',  'color': '#b05a2a'},
    'Fe':   {'unit': 'mg/kg',  'label': 'Total Fe',  'icon': '⚗️',  'color': '#b05a2a'},
    'Mn':   {'unit': 'mg/kg',  'label': 'Total Mn',  'icon': '⚗️',  'color': '#b05a2a'},
}

ALL_PROPERTIES = list(PROPERTY_META.keys())

# Grouped charts — 7 groups
CHART_GROUPS = [
    {'title': 'Carbon & Nitrogen',       'props': ['SOC', 'TC', 'TN']},
    {'title': 'pH',                      'props': ['pH']},
    {'title': 'Available NPK',           'props': ['Av-N', 'Av_P', 'Av_K']},
    {'title': 'Metals — Cu, Zn, Mn',     'props': ['Cu', 'Zn', 'Mn']},
    {'title': 'Iron / Fe (mg/kg)',       'props': ['Fe']},
    {'title': 'Water Retention',         'props': ['FC', 'PWP']},
    {'title': 'Soil Texture',            'props': ['clay', 'silt', 'sand']},
    {'title': 'EC',                      'props': ['EC']},
]

PHYSICAL_BOUNDS = {
    'pH':   (3.0,  11.0),
    'EC':   (0.0,  2000.0),
    'SOC':  (0.0,  20.0),
    'Av-N': (0.0,  1000.0),
    'Av_P': (0.0,  500.0),
    'Av_K': (0.0,  2000.0),
    'FC':   (0.0,  100.0),
    'PWP':  (0.0,  100.0),
    'clay': (0.0,  100.0),
    'silt': (0.0,  100.0),
    'sand': (0.0,  100.0),
    'TC':   (0.0,  20.0),
    'TN':   (0.0,  5.0),
    'Cu':   (0.0,  500.0),
    'Zn':   (0.0,  500.0),
    'Fe':   (0.0,  200000.0),
    'Mn':   (0.0,  10000.0),
}


# ══════════════════════════════════════════════════════════════════════════
#  PREPROCESSING
# ══════════════════════════════════════════════════════════════════════════

def snv(X):
    mu  = X.mean(axis=1, keepdims=True)
    sd  = X.std(axis=1,  keepdims=True)
    sd[sd == 0] = 1
    return (X - mu) / sd

def align_bands(X, n_expected):
    n = X.shape[1]
    if n == n_expected:
        return X
    try:
        from scipy.interpolate import interp1d
        result = interp1d(
            np.linspace(0, 1, n), X, axis=1,
            kind='linear', bounds_error=False,
            fill_value='extrapolate'
        )(np.linspace(0, 1, n_expected))
        # Replace any NaN/inf introduced by interpolation
        return np.where(np.isfinite(result), result, 0.0)
    except Exception:
        if n > n_expected:
            return X[:, :n_expected]
        return np.pad(X, ((0, 0), (0, n_expected - n)), mode='edge')

def apply_preproc(X, name, ref=None):
    if name == 'SNV+SG_smooth':
        return savgol_filter(snv(X), 11, 2, axis=1, deriv=0)
    elif name == 'SNV+SG_1st_deriv':
        return savgol_filter(snv(X), 11, 2, axis=1, deriv=1)
    elif name == 'MSC+SG_smooth':
        if ref is None:
            ref = X.mean(axis=0)
        if len(ref) != X.shape[1]:
            from scipy.interpolate import interp1d
            ref = interp1d(np.linspace(0,1,len(ref)), ref, kind='linear')(np.linspace(0,1,X.shape[1]))
        X_msc = np.zeros_like(X)
        for i in range(X.shape[0]):
            c = np.polyfit(ref, X[i], 1)
            X_msc[i] = (X[i] - c[1]) / c[0]
        return savgol_filter(X_msc, 11, 2, axis=1, deriv=0)
    elif name == 'Raw+SG_1st_deriv':
        return savgol_filter(X, 11, 2, axis=1, deriv=1)
    return X


# ══════════════════════════════════════════════════════════════════════════
#  MODEL LOADING
# ══════════════════════════════════════════════════════════════════════════

@st.cache_resource(show_spinner="Loading models...")
def load_all_models():
    reg_path = os.path.join(MODELS_DIR, 'mir_model_registry.json')
    if not os.path.exists(reg_path):
        return None, {}
    with open(reg_path) as f:
        registry = json.load(f)

    def rp(info, keys, default):
        for k in keys:
            v = info.get(k)
            if not v:
                continue
            if os.path.isabs(v) and os.path.exists(v):
                return v
            pb = os.path.join(MODELS_DIR, os.path.basename(v))
            if os.path.exists(pb):
                return pb
        pd2 = os.path.join(MODELS_DIR, default)
        return pd2 if os.path.exists(pd2) else None

    models = {}
    for prop, info in registry.items():
        pl = prop.lower().replace('-', '_')
        mp = rp(info, ['model_path', 'model_file'], f'mir_{pl}_model.pkl')
        if not mp:
            continue
        entry = {'info': info, 'type': info.get('model_type', 'traditional')}
        try:
            entry['model'] = joblib.load(mp)
        except Exception as e:
            st.warning(f"Could not load model for '{prop}' from {mp}: {type(e).__name__}: {e}")
            continue

        pp2 = rp(info, ['pipeline_path', 'pipeline_file'], f'mir_{pl}_pipeline.pkl')
        if pp2:
            try: entry['pipeline'] = joblib.load(pp2)
            except: pass

        rp2 = rp(info, ['ref_spec_path', 'ref_file'], f'mir_{pl}_ref.npy')
        if rp2:
            try: entry['ref'] = np.load(rp2)
            except: pass

        if info.get('model_type') in ('1D-CNN', 'LSTM-CNN'):
            sp2 = rp(info, ['scaler_path', 'scaler_file'], f'mir_{pl}_scaler.pkl')
            if sp2:
                try: entry['scaler'] = joblib.load(sp2)
                except: pass

        models[prop] = entry

    # Load training-set outlier detector (saved by Step_Fix_All.ipynb Cell 14)
    dd_path = os.path.join(MODELS_DIR, 'outlier_detector.pkl')
    outlier_detector = None
    if os.path.exists(dd_path):
        try:
            outlier_detector = joblib.load(dd_path)
        except Exception:
            pass

    return models, registry, outlier_detector


# ══════════════════════════════════════════════════════════════════════════
#  OUTLIER DETECTION
# ══════════════════════════════════════════════════════════════════════════

def detect_outliers(X, outlier_detector=None):
    """
    Mahalanobis-like outlier detection using saved training PCA.
    If outlier_detector.pkl exists (from Step_Fix_All Cell 14),
    uses the training distribution for proper domain comparison.
    Falls back to batch-relative PCA if not available.
    Domain_distance: 1.0 = at training boundary, >1.0 = outside.
    """
    try:
        X_pp = apply_preproc(X.astype(np.float64), 'SNV+SG_smooth')
        X_pp = np.nan_to_num(X_pp, nan=0.0, posinf=0.0, neginf=0.0)

        if outlier_detector is not None:
            # Use saved training PCA — proper Mahalanobis distance
            scaler    = outlier_detector['scaler']
            pca       = outlier_detector['pca']
            var_T     = outlier_detector['var']
            threshold = outlier_detector['threshold']

            # Align bands if needed
            n_expected = scaler.n_features_in_
            if X_pp.shape[1] != n_expected:
                from scipy.interpolate import interp1d
                f = interp1d(np.linspace(0,1,X_pp.shape[1]), X_pp, axis=1, kind='linear')
                X_pp = f(np.linspace(0,1,n_expected))

            X_sc = scaler.transform(X_pp)
            T    = pca.transform(X_sc)
            var_T[var_T == 0] = 1e-9
            T2 = np.sum((T ** 2) / var_T, axis=1)

            flags = T2 > threshold
            dists = np.round(T2 / (threshold + 1e-9), 3)
        else:
            # Fallback: batch-relative PCA
            from sklearn.decomposition import PCA
            from sklearn.preprocessing import StandardScaler
            from scipy import stats

            n_comp = min(10, X_pp.shape[0] - 1, X_pp.shape[1])
            if n_comp < 2:
                return np.zeros(len(X), dtype=bool), np.zeros(len(X))
            Xs  = StandardScaler().fit_transform(X_pp)
            pca = PCA(n_components=n_comp)
            T   = pca.fit_transform(Xs)
            var_T = T.var(axis=0)
            var_T[var_T == 0] = 1e-9
            T2 = np.sum((T**2) / var_T, axis=1)
            chi2_thresh = stats.chi2.ppf(0.99, df=n_comp)
            flags = T2 > chi2_thresh
            dists = np.round(T2 / (chi2_thresh + 1e-9), 3)

        return flags, dists
    except Exception:
        return np.zeros(len(X), dtype=bool), np.zeros(len(X))


# ══════════════════════════════════════════════════════════════════════════
#  PREDICTION
# ══════════════════════════════════════════════════════════════════════════

def get_n_expected(model_obj, pipeline_obj, ref=None):
    # For Pipeline objects, get n_features from the FIRST step (input features)
    if type(model_obj).__name__ == 'Pipeline':
        first_step = list(model_obj.named_steps.values())[0]
        if hasattr(first_step, 'n_features_in_'):
            return first_step.n_features_in_
        return None
    if pipeline_obj is not None and hasattr(pipeline_obj, 'n_features_in_'):
        return pipeline_obj.n_features_in_
    if hasattr(model_obj, 'n_features_in_'):
        return model_obj.n_features_in_
    if hasattr(model_obj, 'n_features_'):
        return model_obj.n_features_
    # Cubist and some models don't store n_features — use ref spectrum length
    if ref is not None:
        return len(ref)
    return None

def predict_property(X, prop, models):
    if prop not in models and prop != 'EC':
        return np.full(len(X), np.nan)

    if prop == 'EC':
        preds = np.full(len(X), np.nan)
        for i, row in enumerate(X):
            row_2d = row.reshape(1, -1)
            for ec_key in ('EC_normal', 'EC_saline', 'EC'):
                if ec_key not in models:
                    continue
                m = models[ec_key]
                try:
                    X_pp = apply_preproc(row_2d, m['info'].get('preproc','SNV+SG_smooth'), m.get('ref'))
                    n_exp = get_n_expected(m['model'], m.get('pipeline'), m.get('ref'))
                    if n_exp and X_pp.shape[1] != n_exp:
                        X_pp = align_bands(X_pp, n_exp)
                    X_in = m['pipeline'].transform(X_pp) if m.get('pipeline') else X_pp
                    if type(m['model']).__name__ == 'Cubist':
                        import pandas as pd
                        X_in = pd.DataFrame(X_in, columns=[f'var{i}' for i in range(X_in.shape[1])])
                    pred = m['model'].predict(X_in).ravel()[0]
                    if m['info'].get('log_transform'):
                        pred = np.expm1(pred)
                    preds[i] = pred
                    break
                except Exception:
                    continue
        if prop in PHYSICAL_BOUNDS:
            preds = np.clip(preds, *PHYSICAL_BOUNDS[prop])
        return preds

    m     = models[prop]
    info  = m['info']
    mtype = info.get('model_type', 'traditional')
    preproc = info.get('preproc', 'SNV+SG_smooth')
    X_pp = apply_preproc(X.astype(np.float64), preproc, m.get('ref'))

    n_exp = get_n_expected(m['model'], m.get('pipeline'), m.get('ref'))
    if n_exp and X_pp.shape[1] != n_exp:
        X_pp = align_bands(X_pp, n_exp)

    if mtype in ('1D-CNN', 'LSTM-CNN'):
        scaler = m.get('scaler')
        X_sc = scaler.transform(X_pp) if scaler else X_pp
        X_cnn = X_sc.reshape(len(X_sc), X_sc.shape[1], 1)
        preds = m['model'].predict(X_cnn, verbose=0).ravel()
    else:
        pipe = m.get('pipeline')
        X_in = pipe.transform(X_pp) if pipe else X_pp

        # Pipeline model (e.g. SVR with PCA) — predict directly, no separate pipeline
        if type(m['model']).__name__ == 'Pipeline':
            # Align bands to what Pipeline's first step (StandardScaler) expects
            n_exp_pipe = m['model'].named_steps[list(m['model'].named_steps.keys())[0]].n_features_in_
            X_for_pipe = align_bands(X_pp, n_exp_pipe) if X_pp.shape[1] != n_exp_pipe else X_pp
            preds = m['model'].predict(X_for_pipe)
        elif type(m['model']).__name__ == 'Cubist':
            import pandas as pd
            col_names = [f'var{i}' for i in range(X_in.shape[1])]
            X_in = pd.DataFrame(X_in, columns=col_names)
            preds = m['model'].predict(X_in)
        else:
            preds = m['model'].predict(X_in)
        if hasattr(preds, 'ravel'):
            preds = preds.ravel()
        elif hasattr(preds, 'values'):
            preds = preds.values.ravel()

    if info.get('log_transform'):
        preds = np.expm1(preds)

    if prop in PHYSICAL_BOUNDS:
        preds = np.clip(preds, *PHYSICAL_BOUNDS[prop])

    return preds


# ══════════════════════════════════════════════════════════════════════════
#  OPUS CONVERSION
# ══════════════════════════════════════════════════════════════════════════

def convert_uploaded_files(uploaded_files):
    rows, errors = [], []
    bar = st.progress(0, text="Reading OPUS files...")
    for i, uf in enumerate(uploaded_files):
        bar.progress((i+1)/len(uploaded_files),
                     text=f"Reading {uf.name} ({i+1}/{len(uploaded_files)})")
        try:
            with tempfile.NamedTemporaryFile(suffix='.0', delete=False) as tmp:
                tmp.write(uf.read())
                tmp_path = tmp.name
            result = read_opus(tmp_path, speclib='ICRAF')
            os.unlink(tmp_path)
            wn  = result['wavenumbers']
            ab  = result['absorbance']
            pref = result['prefix']
            labels = [f"{pref}{round(w,1):g}" for w in wn]
            row = {
                'SAMPLEID':     result['SAMPLEID'],
                'Material':     result['Material'],
                'Datetime':     result['Datetime'],
                'Zero.filling': result['Zero_filling'],
                'Resolution':   result['Resolution'],
                'LWN':          result['LWN'],
            }
            for lbl, val in zip(labels, ab):
                row[lbl] = val
            rows.append(row)
        except Exception as e:
            errors.append(f"{uf.name}: {e}")
    bar.empty()
    for err in errors:
        st.warning(f"⚠ {err}")
    return pd.DataFrame(rows) if rows else pd.DataFrame()


# ══════════════════════════════════════════════════════════════════════════
#  HEADER
# ══════════════════════════════════════════════════════════════════════════

def _img_b64(path):
    try:
        with open(path, 'rb') as f:
            return base64.b64encode(f.read()).decode()
    except Exception:
        return ''

def render_header():
    assets = os.path.join(os.path.dirname(__file__), 'assets')

    soil_path = os.path.join(assets, 'soil_backdrop.png')
    bg_css = ''
    if os.path.exists(soil_path):
        b64 = _img_b64(soil_path)
        bg_css = f"background-image:url('data:image/png;base64,{b64}');background-size:cover;background-position:center;"

    st.markdown(f"""
    <div style='{bg_css}border-radius:20px;padding:36px 24px 28px;
                margin-bottom:10px;position:relative;overflow:hidden;
                box-shadow:0 8px 32px rgba(20,80,10,0.25);'>
      <div style='position:absolute;inset:0;
                  background:linear-gradient(135deg,rgba(8,15,50,0.75),rgba(20,40,120,0.60));
                  border-radius:20px;'></div>
      <div style='position:relative;z-index:1;text-align:center;'>
        <div style='font-size:72px;font-weight:900;letter-spacing:10px;
                    color:#ffffff;line-height:1;
                    text-shadow:0 4px 20px rgba(0,0,0,0.6);'>MIDAS</div>
        <div style='font-size:22px;font-weight:500;margin:12px 0 0;
                    color:#e8f0ff;letter-spacing:2px;
                    text-shadow:0 1px 8px rgba(0,0,0,0.5);'>
          Mid-Infrared Spectroscopy Analysis System</div>
      </div>
    </div>""", unsafe_allow_html=True)

    c1, c2, c3 = st.columns([1, 3.5, 1])
    with c1:
        p = os.path.join(assets, 'ICAR Logo.png')
        if os.path.exists(p):
            st.image(p, width=110)
        if st.button('ℹ About ICAR', key='icar_btn'):
            st.session_state['show_icar'] = not st.session_state.get('show_icar', False)
            st.rerun()
    with c2:
        # India map image
        _map_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'india_map.png')
        if os.path.exists(_map_path):
            st.image(_map_path, use_container_width=True)
        else:
            st.markdown(
                "<div style='text-align:center;padding:20px;"
                "color:#c9a227;font-size:12px;'>india_map.png not found</div>",
                unsafe_allow_html=True
            )
    with c3:
        p = os.path.join(assets, 'ICRAF Logo.png')
        if os.path.exists(p):
            st.image(p, width=180)
        if st.button('ℹ About ICRAF', key='icraf_btn'):
            st.session_state['show_icraf'] = not st.session_state.get('show_icraf', False)
            st.rerun()

    @st.dialog("About ICAR")
    def _dlg_icar():
        st.markdown(ICAR_INFO)

    @st.dialog("About World Agroforestry (ICRAF)")
    def _dlg_icraf():
        st.markdown(ICRAF_INFO)

    if st.session_state.get('show_icar', False):
        st.session_state['show_icar'] = False
        _dlg_icar()

    if st.session_state.get('show_icraf', False):
        st.session_state['show_icraf'] = False
        _dlg_icraf()


# ══════════════════════════════════════════════════════════════════════════
#  SIDEBAR
# ══════════════════════════════════════════════════════════════════════════

def render_sidebar(registry):
    st.sidebar.markdown("### Instructions")
    st.sidebar.markdown("""
1. Select soil properties to predict
2. Upload OPUS files (`.0` extension)
3. Click **Preview Spectral Data** to view MIR spectra
4. Click **Run the Model** to get predictions
5. Download results as **CSV**, **Excel** or **PDF**
""")
    st.sidebar.markdown("---")

    # ── Download format previews ───────────────────────────────────────
    st.sidebar.markdown("### Download Formats Available")

    # Images live in same folder as the app itself
    assets = os.path.dirname(os.path.abspath(__file__))

    # PDF
    pdf_img = os.path.join(assets, 'pdf_format.png')
    if os.path.exists(pdf_img):
        st.sidebar.markdown("**📄 PDF Report**")
        st.sidebar.image(pdf_img, use_container_width=True,
                         caption="MIDAS branded PDF — landscape A4, all predictions")
    else:
        st.sidebar.markdown("**📄 PDF Report** — MIDAS branded, landscape A4, all predictions")

    st.sidebar.markdown("")

    # Excel
    excel_img = os.path.join(assets, 'excel_format.png')
    if os.path.exists(excel_img):
        st.sidebar.markdown("**📊 Excel Sheet**")
        st.sidebar.image(excel_img, use_container_width=True,
                         caption="Formatted Excel — green headers, yellow outlier rows")
    else:
        st.sidebar.markdown("**📊 Excel Sheet** — Green headers, outlier highlighting, model info tab")

    st.sidebar.markdown("")

    # CSV
    csv_img = os.path.join(assets, 'csv_format.png')
    if os.path.exists(csv_img):
        st.sidebar.markdown("**📋 CSV File**")
        st.sidebar.image(csv_img, use_container_width=True,
                         caption="Raw CSV — compatible with Excel, R, Python")
    else:
        st.sidebar.markdown("**📋 CSV File** — Raw predictions, compatible with Excel, R, Python")


# ══════════════════════════════════════════════════════════════════════════
#  GROUPED CHARTS
# ══════════════════════════════════════════════════════════════════════════

def render_grouped_charts(df_results, props_predicted):
    st.markdown("### Prediction Charts")
    ids = df_results['ID'].astype(str).tolist()

    for group in CHART_GROUPS:
        # Find which props in this group were predicted
        group_props = [p for p in group['props'] if p in props_predicted]
        if not group_props:
            continue

        # Build column name lookup
        col_map = {}
        for p in group_props:
            label = PROPERTY_META[p]['label']
            unit  = PROPERTY_META[p]['unit']
            col   = f"{label} ({unit})" if unit else label
            if col in df_results.columns:
                col_map[p] = col

        if not col_map:
            continue

        fig = go.Figure()
        colors = px.colors.qualitative.Set2
        for idx, (p, col) in enumerate(col_map.items()):
            label = PROPERTY_META[p]['label']
            unit  = PROPERTY_META[p]['unit']
            fig.add_trace(go.Bar(
                name=f"{label} ({unit})" if unit else label,
                x=ids,
                y=df_results[col].tolist(),
                marker_color=colors[idx % len(colors)]
            ))

        fig.update_layout(
            barmode='group',
            title=group['title'],
            xaxis_title='Sample ID',
            yaxis_title='Value',
            template='plotly_white',
            height=380,
            legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
            xaxis=dict(tickangle=-45)
        )
        st.plotly_chart(fig, use_container_width=True)


# ══════════════════════════════════════════════════════════════════════════
#  MAIN
# ══════════════════════════════════════════════════════════════════════════

def main():
    render_header()
    st.markdown("---")

    models, registry, outlier_detector = load_all_models()
    if models is None:
        st.error("No model files found. Place model pkl files in the models/ folder.")
        return

    render_sidebar(registry)

    # ── Property multi-select ──────────────────────────────────────────
    st.markdown("**Select soil properties to predict:**")
    col_all, col_none = st.columns([1, 5])
    with col_all:
        select_all = st.button("Select All")

    prop_labels = {
        p: (f"{PROPERTY_META[p]['icon']} {PROPERTY_META[p]['label']} ({PROPERTY_META[p]['unit']})"
            if PROPERTY_META[p]['unit']
            else f"{PROPERTY_META[p]['icon']} {PROPERTY_META[p]['label']}")
        for p in ALL_PROPERTIES
    }

    default = ALL_PROPERTIES if select_all else st.session_state.get('selected_props', ALL_PROPERTIES)
    selected_props = st.multiselect(
        label="Properties",
        options=ALL_PROPERTIES,
        default=default,
        format_func=lambda p: prop_labels[p],
        label_visibility='collapsed'
    )
    st.session_state['selected_props'] = selected_props

    if not selected_props:
        st.warning("Please select at least one property.")
        return

    # ── File upload ────────────────────────────────────────────────────
    if 'uploader_key' not in st.session_state:
        st.session_state['uploader_key'] = 0

    uploaded = st.file_uploader(
        "Upload your OPUS files (.0)",
        type=['0'],
        accept_multiple_files=True,
        help="Select one or more Bruker Alpha OPUS files",
        key=f"opus_{st.session_state['uploader_key']}"
    )

    if uploaded:
        col_ra, _ = st.columns([1, 5])
        with col_ra:
            if st.button("Remove All Files", type="secondary"):
                st.session_state['uploader_key'] += 1
                st.session_state['upload_key']   = None
                st.session_state['df_spec']      = None
                st.rerun()

    if not uploaded:
        st.info("Upload OPUS files above to begin.")
        return

    # ── Convert OPUS ───────────────────────────────────────────────────
    cache_key = tuple(sorted(f.name for f in uploaded))
    if st.session_state.get('upload_key') != cache_key:
        with st.spinner("Converting OPUS files..."):
            df_spec = convert_uploaded_files(uploaded)
            st.session_state['df_spec']    = df_spec
            st.session_state['upload_key'] = cache_key
    else:
        df_spec = st.session_state['df_spec']

    if df_spec.empty:
        st.error("No files could be read. Check file format.")
        return

    spectral_cols = [c for c in df_spec.columns 
                         if c[0] in ('a', 'm', 'n')
                         and not (2200 <= float(c[1:]) <= 2400)]  # remove CO2 bands
    wavenumbers   = [float(c[1:]) for c in spectral_cols]
    n_samples     = len(df_spec)
    X             = df_spec[spectral_cols].values.astype(float)

    st.success(f"✓ {n_samples} file(s) converted · {len(spectral_cols)} wavenumbers "
               f"({max(wavenumbers):.0f}–{min(wavenumbers):.0f} cm⁻¹)")

    n_preview = st.number_input(
        "Number of spectra to preview:",
        min_value=1, max_value=n_samples,
        value=min(3, n_samples), step=1
    )

    col1, _, col2 = st.columns([1, 3, 1])
    with col1:
        preview_btn = st.button("📊 Preview Spectral Data", use_container_width=True)
    with col2:
        run_btn = st.button("🚀 Run the Model", use_container_width=True, type="primary")

    # ── Preview ────────────────────────────────────────────────────────
    if preview_btn:
        fig = go.Figure()
        for i in range(int(n_preview)):
            fig.add_trace(go.Scatter(
                x=wavenumbers,
                y=df_spec[spectral_cols].iloc[i].values,
                mode='lines',
                name=str(df_spec['SAMPLEID'].iloc[i]),
                line=dict(width=1.5)
            ))
        fig.update_layout(
            title='MIR Spectra — Raw Absorbance',
            xaxis=dict(title='Wavenumber (cm⁻¹)', autorange='reversed'),
            yaxis_title='Absorbance',
            legend_title='Sample ID',
            template='plotly_white',
            height=420
        )
        st.plotly_chart(fig, use_container_width=True)

    # ── Run model ──────────────────────────────────────────────────────
    if run_btn:
        ids = df_spec['SAMPLEID'].values
        with st.spinner("Running predictions..."):
            outlier_flags, outlier_dists = detect_outliers(X, outlier_detector)
            results = {'ID': ids}
            props_predicted = []
            for prop in selected_props:
                try:
                    preds = predict_property(X, prop, models)
                    label = PROPERTY_META[prop]['label']
                    unit  = PROPERTY_META[prop]['unit']
                    col_name = f"{label} ({unit})" if unit else label
                    results[col_name] = np.round(preds, 3)
                    props_predicted.append(prop)
                    if np.all(np.isnan(preds)):
                        st.warning(f"{prop}: all predictions are NaN — check model compatibility")
                except Exception as e:
                    st.warning(f"Could not predict {prop}: {type(e).__name__}: {e}")

            results['Outlier']         = outlier_flags
            results['Domain_distance'] = np.round(outlier_dists, 3)
            df_results = pd.DataFrame(results)
            st.session_state['df_results'] = df_results
            st.session_state['registry_snap'] = registry
            st.session_state['n_samples_snap'] = n_samples

            # Texture normalization — clay+silt+sand must sum to 100%
            clay_col = 'Clay (%)'
            silt_col = 'Silt (%)'
            sand_col = 'Sand (%)'
            if all(c in df_results.columns for c in [clay_col, silt_col, sand_col]):
                tex_sum = df_results[clay_col] + df_results[silt_col] + df_results[sand_col]
                valid = tex_sum > 0
                df_results.loc[valid, clay_col] = np.round(df_results.loc[valid, clay_col] / tex_sum[valid] * 100, 4)
                df_results.loc[valid, silt_col] = np.round(df_results.loc[valid, silt_col] / tex_sum[valid] * 100, 4)
                df_results.loc[valid, sand_col] = np.round(df_results.loc[valid, sand_col] / tex_sum[valid] * 100, 4)

        df_results  = st.session_state.get('df_results', df_results)
        n_out = outlier_flags.sum()
        if n_out > 0:
            st.warning(
                f"⚠ **{n_out} sample(s) flagged outside training domain.** "
                "Predictions for these may be less reliable."
            )

        # Results table
        st.markdown("### Prediction Results")
        def highlight_outlier(row):
            if row.get('Outlier', False):
                return ['background-color: #fff3cd'] * len(row)
            return [''] * len(row)

        st.dataframe(
            df_results.style.apply(highlight_outlier, axis=1),
            use_container_width=True
        )

        # Grouped charts
        render_grouped_charts(df_results, props_predicted)

        # Model info footer
        if registry:
            info_parts = []
            for prop in props_predicted[:4]:
                v = registry.get(prop, {})
                if v:
                    info_parts.append(
                        f"{prop}: {v.get('model_type','?')} "
                        f"(R²={v.get('test_R2',0):.3f}, RPD={v.get('test_RPD',0):.2f})"
                    )

        # ── Downloads ─────────────────────────────────────────────────────────
        st.markdown("### Downloads")
        dl1, dl2, dl3 = st.columns(3)

        with dl1:
            csv_bytes = df_results.to_csv(index=False).encode()
            st.download_button("⬇ Download CSV", data=csv_bytes,
                file_name=f"midas_{datetime.date.today()}.csv",
                mime="text/csv", use_container_width=True)

        with dl2:
            try:
                import openpyxl
                from openpyxl.styles import PatternFill, Font, Alignment
                from openpyxl.utils import get_column_letter
                wb  = openpyxl.Workbook()
                ws  = wb.active
                ws.title = 'Predictions'
                hf  = PatternFill(start_color='1e7a14', end_color='1e7a14', fill_type='solid')
                hfn = Font(bold=True, color='FFFFFF')
                ofill = PatternFill(start_color='FFF3CD', end_color='FFF3CD', fill_type='solid')
                for ci, cn in enumerate(df_results.columns, 1):
                    c = ws.cell(row=1, column=ci, value=cn)
                    c.fill = hf; c.font = hfn
                    c.alignment = Alignment(horizontal='center')
                for ri, (_, row) in enumerate(df_results.iterrows(), 2):
                    is_out = bool(row.get('Outlier', False))
                    for ci, val in enumerate(row, 1):
                        c = ws.cell(row=ri, column=ci)
                        if isinstance(val, float) and not isinstance(val, bool):
                            try: c.value = round(val, 4)
                            except: c.value = val
                        elif isinstance(val, bool):
                            c.value = 'Yes' if val else 'No'
                        else:
                            c.value = val
                        c.alignment = Alignment(horizontal='center')
                        if is_out: c.fill = ofill
                for ci in range(1, len(df_results.columns)+1):
                    ws.column_dimensions[get_column_letter(ci)].width = 16
                ws.freeze_panes = 'B2'
                buf = io.BytesIO(); wb.save(buf); buf.seek(0)
                st.download_button("📊 Download Excel", data=buf.read(),
                    file_name=f"midas_{datetime.date.today()}.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    use_container_width=True)
            except ImportError:
                st.info("pip install openpyxl for Excel export")

        with dl3:
            if st.button("📄 Generate PDF Report", use_container_width=True,
                         key="pdf_btn"):
                # Build HTML directly here — no session state needed
                _df = st.session_state.get('df_results', pd.DataFrame())
                if _df.empty:
                    st.session_state['pdf_html'] = None
                    st.warning("Run the model first before generating PDF.")
                else:
                    _now = datetime.datetime.now().strftime('%d-%b-%Y %H:%M')
                    _nc  = [c for c in _df.columns
                            if c not in ('ID','Outlier','Domain_distance')]
                    _h = f"""<!DOCTYPE html><html><head><meta charset='UTF-8'>
<style>
body{{font-family:Arial,sans-serif;margin:30px;color:#1a1a1a}}
.hdr{{background:linear-gradient(135deg,#1e7a14,#2ea81e);color:white;padding:24px;border-radius:12px;text-align:center}}
.hdr .big{{font-size:36px;font-weight:900;letter-spacing:6px;margin:0}}
.hdr .sub{{font-size:13px;color:#d4f7c0;margin:4px 0 0}}
h2{{color:#1e7a14;border-bottom:2px solid #8ad880;margin-top:22px;font-size:15px}}
table{{width:100%;border-collapse:collapse;margin-top:10px;font-size:12px}}
th{{background:#1e7a14;color:white;padding:8px 10px;text-align:left}}
td{{padding:7px 10px;border-bottom:1px solid #d8ecd4}}
tr:nth-child(even) td{{background:#f0faea}}
.out td{{background:#fff3cd!important}}
.foot{{margin-top:28px;font-size:10px;color:#888;border-top:1px solid #ddd;padding-top:8px}}
</style></head><body>
<div class='hdr'>
  <div class='big'>MIDAS</div>
  <div class='sub'>Mid-Infrared Spectroscopy Analysis System</div>
  <div class='sub'>ICAR-IISS Bhopal x ICRAF | Generated: {_now}</div>
</div>
<h2>Soil Property Predictions</h2>
<table><tr><th>Sample ID</th>{''.join(f'<th>{c}</th>' for c in _nc)}</tr>"""
                    for _, _row in _df.iterrows():
                        _rc = 'out' if _row.get('Outlier', False) else ''
                        _h += f"<tr class='{_rc}'><td><b>{_row['ID']}</b></td>"
                        for _col in _nc:
                            try: _h += f"<td>{round(float(_row[_col]),3)}</td>"
                            except: _h += f"<td>{_row.get(_col,'')}</td>"
                        _h += "</tr>"
                    _h += "<div class='foot'>MIDAS | ICAR-IISS Bhopal x ICRAF | Model predictions — verify critical values with lab analysis.</div></table></body></html>"
                    st.session_state['pdf_html'] = _h

        # Show PDF/HTML download if ready
        if st.session_state.get('pdf_html'):
            _h = st.session_state['pdf_html']
            # Always offer HTML — works 100% without any installation
            st.download_button(
                label="⬇ Download Report (HTML → open in Chrome → Ctrl+P → Save as PDF)",
                data=_h.encode('utf-8'),
                file_name=f"midas_report_{datetime.date.today()}.html",
                mime="text/html",
                use_container_width=True,
                key="html_dl_btn"
            )

        # ── Batch history ──────────────────────────────────────────────────
        if 'batch_history' not in st.session_state:
            st.session_state['batch_history'] = []
        st.session_state['batch_history'].append({
            'ts': datetime.datetime.now().strftime('%d-%b %H:%M'),
            'n': n_samples, 'df': df_results.copy()
        })
        if len(st.session_state['batch_history']) > 1:
            st.markdown("---")
            st.markdown("### Batch History (this session)")
            for batch in reversed(st.session_state['batch_history'][-5:]):
                with st.expander(f"{batch['ts']} — {batch['n']} samples"):
                    st.dataframe(batch['df'], use_container_width=True, hide_index=True)

        gc.collect()

    # ── Display results from session state (persists across button clicks) ──
    if 'df_results' in st.session_state and st.session_state['df_results'] is not None:
        _df  = st.session_state['df_results']
        _reg = st.session_state.get('registry_snap', registry)

        if not run_btn:  # only show if not currently running (avoid duplicate)
            n_out = int(_df['Outlier'].sum()) if 'Outlier' in _df.columns else 0
            if n_out > 0:
                st.warning(f"⚠ **{n_out} sample(s) flagged outside training domain.**")

            st.markdown("### Prediction Results")
            # Force 3 decimal places by converting to string
            _df_display = _df.copy()
            for _col in _df_display.columns:
                if _col not in ('ID', 'Outlier', 'Domain_distance'):
                    try:
                        _df_display[_col] = _df_display[_col].apply(
                            lambda x: f'{float(x):.3f}' if pd.notna(x) else '—'
                        )
                    except Exception:
                        pass
            _df_display['Domain_distance'] = _df_display['Domain_distance'].apply(
                lambda x: f'{float(x):.3f}' if pd.notna(x) else '—'
            ) if 'Domain_distance' in _df_display.columns else _df_display.get('Domain_distance', '')
            def _hl(row):
                if row.get('Outlier', False):
                    return ['background-color: #fff3cd'] * len(row)
                return [''] * len(row)
            st.dataframe(_df_display.style.apply(_hl, axis=1), use_container_width=True)

            # Charts
            _props_pred = [p for p in ALL_PROPERTIES
                           if any(PROPERTY_META[p]['label'] in c for c in _df.columns)]
            render_grouped_charts(_df, _props_pred)

            # Downloads
            st.markdown("### Downloads")
            _dl1, _dl2, _dl3 = st.columns(3)

            with _dl1:
                _csv = _df.to_csv(index=False).encode()
                st.download_button("⬇ Download CSV", data=_csv,
                    file_name=f"midas_{datetime.date.today()}.csv",
                    mime="text/csv", use_container_width=True)

            with _dl2:
                try:
                    import openpyxl
                    from openpyxl.styles import PatternFill, Font, Alignment
                    from openpyxl.utils import get_column_letter
                    _wb = openpyxl.Workbook()
                    _ws = _wb.active
                    _ws.title = 'Predictions'
                    _hf  = PatternFill(start_color='1e7a14', end_color='1e7a14', fill_type='solid')
                    _hfn = Font(bold=True, color='FFFFFF')
                    _of  = PatternFill(start_color='FFF3CD', end_color='FFF3CD', fill_type='solid')
                    for _ci, _cn in enumerate(_df.columns, 1):
                        _c = _ws.cell(row=1, column=_ci, value=_cn)
                        _c.fill = _hf; _c.font = _hfn
                        _c.alignment = Alignment(horizontal='center')
                    for _ri, (_, _row) in enumerate(_df.iterrows(), 2):
                        _io = bool(_row.get('Outlier', False))
                        for _ci, _val in enumerate(_row, 1):
                            _c = _ws.cell(row=_ri, column=_ci)
                            if isinstance(_val, float) and not isinstance(_val, bool):
                                try: _c.value = round(_val, 4)
                                except: _c.value = _val
                            elif isinstance(_val, bool):
                                _c.value = 'Yes' if _val else 'No'
                            else:
                                _c.value = _val
                            _c.alignment = Alignment(horizontal='center')
                            if _io: _c.fill = _of
                    for _ci in range(1, len(_df.columns)+1):
                        _ws.column_dimensions[get_column_letter(_ci)].width = 16
                    _ws.freeze_panes = 'B2'
                    _buf = io.BytesIO(); _wb.save(_buf); _buf.seek(0)
                    st.download_button("📊 Download Excel", data=_buf.read(),
                        file_name=f"midas_{datetime.date.today()}.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                        use_container_width=True)
                except ImportError:
                    st.info("pip install openpyxl for Excel")

            with _dl3:
                try:
                    import io as _io
                    from reportlab.lib.pagesizes import A4, landscape
                    from reportlab.platypus import (SimpleDocTemplate, Table,
                        TableStyle, Paragraph, Spacer)
                    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
                    from reportlab.lib import colors
                    from reportlab.lib.units import cm

                    _now = datetime.datetime.now().strftime('%d-%b-%Y %H:%M')
                    _nc  = [c for c in _df.columns
                            if c not in ('ID','Outlier','Domain_distance')]

                    _buf  = _io.BytesIO()
                    _doc  = SimpleDocTemplate(
                        _buf,
                        pagesize=landscape(A4),
                        rightMargin=1.5*cm, leftMargin=1.5*cm,
                        topMargin=2*cm, bottomMargin=1.5*cm
                    )
                    _styles = getSampleStyleSheet()
                    _green  = colors.HexColor('#1e7a14')
                    _lgreen = colors.HexColor('#f0faea')
                    _yellow = colors.HexColor('#fff3cd')

                    _title_style = ParagraphStyle(
                        'MIDASTitle',
                        fontSize=28, fontName='Helvetica-Bold',
                        textColor=colors.white, alignment=1,
                        spaceAfter=2
                    )
                    _sub_style = ParagraphStyle(
                        'MIDASSub',
                        fontSize=11, fontName='Helvetica',
                        textColor=colors.HexColor('#d4f7c0'), alignment=1
                    )
                    _h2_style = ParagraphStyle(
                        'MIDASH2',
                        fontSize=13, fontName='Helvetica-Bold',
                        textColor=_green, spaceBefore=14, spaceAfter=6,
                        borderPadding=(0,0,3,0)
                    )
                    _footer_style = ParagraphStyle(
                        'MIDASFooter',
                        fontSize=8, fontName='Helvetica',
                        textColor=colors.grey, alignment=1, spaceBefore=16
                    )

                    # Header block as a 1-cell table with green background
                    _hdr_data = [[
                        Paragraph("MIDAS", _title_style),
                    ]]
                    _hdr_sub  = [[
                        Paragraph(
                            "Mid-Infrared Spectroscopy Analysis System<br/>"
                            f"ICAR-IISS Bhopal x ICRAF &nbsp;|&nbsp; {_now}",
                            _sub_style
                        )
                    ]]
                    _hdr_table = Table(
                        _hdr_data + _hdr_sub,
                        colWidths=[_doc.width]
                    )
                    _hdr_table.setStyle(TableStyle([
                        ('BACKGROUND', (0,0), (-1,-1), _green),
                        ('ALIGN',      (0,0), (-1,-1), 'CENTER'),
                        ('VALIGN',     (0,0), (-1,-1), 'MIDDLE'),
                        ('TOPPADDING', (0,0), (-1,-1), 10),
                        ('BOTTOMPADDING', (0,-1), (-1,-1), 14),
                        ('ROUNDEDCORNERS', [8]),
                    ]))

                    # Results table
                    _col_headers = ['Sample ID'] + _nc
                    _tdata = [_col_headers]
                    for _, _row in _df.iterrows():
                        _trow = [str(_row['ID'])]
                        for _col in _nc:
                            try: _trow.append(str(round(float(_row[_col]), 3)))
                            except: _trow.append(str(_row.get(_col, '')))
                        _tdata.append(_trow)

                    # Auto column widths
                    _n_cols   = len(_col_headers)
                    _col_w    = _doc.width / _n_cols
                    _id_w     = _col_w * 1.6
                    _other_w  = (_doc.width - _id_w) / (_n_cols - 1)
                    _col_widths = [_id_w] + [_other_w] * (_n_cols - 1)

                    _tbl = Table(_tdata, colWidths=_col_widths, repeatRows=1)
                    _tbl_style = [
                        # Header row
                        ('BACKGROUND',   (0,0), (-1,0), _green),
                        ('TEXTCOLOR',    (0,0), (-1,0), colors.white),
                        ('FONTNAME',     (0,0), (-1,0), 'Helvetica-Bold'),
                        ('FONTSIZE',     (0,0), (-1,0), 9),
                        ('ALIGN',        (0,0), (-1,0), 'CENTER'),
                        ('BOTTOMPADDING',(0,0), (-1,0), 8),
                        ('TOPPADDING',   (0,0), (-1,0), 8),
                        # Data rows
                        ('FONTNAME',     (0,1), (-1,-1), 'Helvetica'),
                        ('FONTSIZE',     (0,1), (-1,-1), 8),
                        ('ALIGN',        (0,1), (0,-1),  'LEFT'),
                        ('ALIGN',        (1,1), (-1,-1), 'CENTER'),
                        ('ROWBACKGROUNDS',(0,1),(-1,-1), [colors.white, _lgreen]),
                        ('TOPPADDING',   (0,1), (-1,-1), 5),
                        ('BOTTOMPADDING',(0,1), (-1,-1), 5),
                        # Grid
                        ('GRID',         (0,0), (-1,-1), 0.4, colors.HexColor('#c8e8c0')),
                        ('LINEBELOW',    (0,0), (-1,0),  1.2, _green),
                    ]
                    # Yellow for outlier rows
                    for _ri, (_, _row) in enumerate(_df.iterrows(), 1):
                        if _row.get('Outlier', False):
                            _tbl_style.append(
                                ('BACKGROUND', (0,_ri), (-1,_ri), _yellow)
                            )
                    _tbl.setStyle(TableStyle(_tbl_style))

                    _story = [
                        _hdr_table,
                        Spacer(1, 0.4*cm),
                        Paragraph("Soil Property Predictions", _h2_style),
                        _tbl,
                        Spacer(1, 0.3*cm),
                        Paragraph(
                            "MIDAS | ICAR-IISS Bhopal x World Agroforestry (ICRAF) | "
                            "Auto-generated report. Results are model predictions — "
                            "verify critical values with standard lab analysis.",
                            _footer_style
                        )
                    ]
                    _doc.build(_story)
                    _pdf_bytes = _buf.getvalue()

                    st.download_button(
                        "📄 Download PDF Report",
                        data=_pdf_bytes,
                        file_name=f"midas_report_{datetime.date.today()}.pdf",
                        mime="application/pdf",
                        use_container_width=True
                    )
                except Exception as _e:
                    st.error(f"PDF error: {_e}")

            # Batch history
            if 'batch_history' not in st.session_state:
                st.session_state['batch_history'] = []
            if run_btn or not st.session_state['batch_history'] or                st.session_state['batch_history'][-1]['df'].shape != _df.shape:
                st.session_state['batch_history'].append({
                    'ts': datetime.datetime.now().strftime('%d-%b %H:%M'),
                    'n': len(_df), 'df': _df.copy()
                })
            if len(st.session_state['batch_history']) > 1:
                st.markdown("---")
                st.markdown("### Batch History (this session)")
                for _batch in reversed(st.session_state['batch_history'][-5:]):
                    with st.expander(f"{_batch['ts']} — {_batch['n']} samples"):
                        st.dataframe(_batch['df'], use_container_width=True, hide_index=True)


if __name__ == "__main__":
    main()
