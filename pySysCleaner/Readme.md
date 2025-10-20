# 🧹 System Cleaner (Python)

A lightweight and safe **Python-based system cleaner** that automatically deletes temporary, cache, and log files from your system.  
It works on **Windows, Linux, and macOS**, and can even be converted into a **standalone executable (.exe)** — so it runs without needing Python installed.

---

## 🚀 Features

- 🧽 Automatically cleans:
  - Temporary files
  - Cache folders
  - Log directories
  - Crash dumps
- 💾 Keeps a log of all deleted items
- ⚙️ Cross-platform (Windows / Linux / macOS)
- 🧠 Skips files currently in use or protected

---

## ⚙️ Installation & Usage

### ▶️ Run Directly (if Python is installed)

1. Clone or download this repository  
2. Run the script:
   ```bash
   python cleaner.py
   ```
3. The cleaner will:
    Scan common temp/cache/log directories
    Delete unnecessary files
    Save a detailed log at:
    ```bash
    C:\Users\<YourName>\system_cleaner_log.txt
    or
    ~/system_cleaner_log.txt
    ```