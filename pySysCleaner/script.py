import os
import shutil
import tempfile
from pathlib import Path
import time
import platform
import logging

# === Setup Logging ===
log_file = Path.home() / "system_cleaner_log.txt"
logging.basicConfig(filename=log_file, level=logging.INFO, format="%(asctime)s - %(message)s")

def safe_delete(path: Path):
    """Try to safely delete a file or folder"""
    try:
        if path.is_file() or path.is_symlink():
            path.unlink()
            logging.info(f"Deleted file: {path}")
        elif path.is_dir():
            shutil.rmtree(path)
            logging.info(f"Deleted folder: {path}")
    except Exception as e:
        logging.warning(f"Skipped {path} — {e}")

def clean_folder(folder_path: Path):
    """Clean all unnecessary files in a given folder"""
    if folder_path.exists():
        for item in folder_path.iterdir():
            safe_delete(item)

def system_clean():
    os_name = platform.system().lower()
    logging.info(f"=== Starting Cleanup on {os_name.upper()} ===")

    folders_to_clean = []

    if "windows" in os_name:
        folders_to_clean = [
            Path(tempfile.gettempdir()),  # C:\Users\<user>\AppData\Local\Temp
            Path(os.getenv("LOCALAPPDATA", "")) / "Temp",
            Path(os.getenv("WINDIR", "")) / "Temp",
            Path.home() / "AppData/Local/CrashDumps",
            Path.home() / "AppData/Local/Microsoft/Windows/INetCache"
        ]
    else:  # Linux / macOS
        folders_to_clean = [
            Path("/tmp"),
            Path.home() / ".cache",
            Path.home() / "Downloads/.temp",
            Path.home() / "logs"
        ]

    for folder in folders_to_clean:
        if folder.exists():
            print(f"🧹 Cleaning: {folder}")
            clean_folder(folder)

    print("\n✅ Cleanup completed!")
    logging.info("=== Cleanup Completed ===")

if __name__ == "__main__":
    print("Starting system cleanup...")
    time.sleep(1)
    system_clean()
