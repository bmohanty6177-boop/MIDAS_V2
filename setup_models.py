"""
Downloads MIDAS model files from Google Drive on first run.
Place this in the same folder as midas_mir_app_FINALF.py
"""
import os, gdown

MODELS_DIR = 'models'
FOLDER_ID  = '1t7E867ThQc1vpSClKLoBSwzW-tzn0oyk'

def download_models():
    if os.path.exists(MODELS_DIR) and len(os.listdir(MODELS_DIR)) >= 30:
        print(f'Models already present ({len(os.listdir(MODELS_DIR))} files)')
        return
    print('Downloading models from Google Drive...')
    os.makedirs(MODELS_DIR, exist_ok=True)
    gdown.download_folder(
        id=FOLDER_ID,
        output=MODELS_DIR,
        quiet=False,
        use_cookies=False
    )
    print(f'Done — {len(os.listdir(MODELS_DIR))} files downloaded')

if __name__ == '__main__':
    download_models()
