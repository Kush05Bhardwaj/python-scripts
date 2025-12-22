import os
import shutil

DOWNLOADS = os.path.expanduser("~/Downloads")

FILES = {
    "Images": [".jpg", ".png", ".jpeg", ".gif"],
    "Videos": [".mp4", ".mkv"],
    "Docs": [".pdf", ".docx", ".txt"],
    "Music": [".mp3", ".wav"],
    "Zips": [".zip", ".rar"]
}

for file in os.listdir(DOWNLOADS):
    path = os.path.join(DOWNLOADS, file)
    if os.path.isfile(path):
        for folder, exts in FILES.items():
            if file.lower().endswith(tuple(exts)):
                os.makedirs(os.path.join(DOWNLOADS, folder), exist_ok=True)
                shutil.move(path, os.path.join(DOWNLOADS, folder, file))
