import os
import shutil
import unicodedata

FOLDERS = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp", ".heic"],
    "Documents": [".pdf", ".doc", ".docx", ".ppt", ".pptx", ".xls", ".xlsx", ".odt", ".ods", ".odp", ".csv"],
    "Text": [".txt", ".md", ".rtf", ".log", ".ini", ".json", ".xml", ".yaml", ".yml"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm"],
    "Music": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a", ".wma"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Programs": [".exe", ".msi", ".apk", ".bat", ".sh", ".deb"]
}

normalize = lambda p: unicodedata.normalize("NFC", p)
get_ext = lambda f: os.path.splitext(f)[1].lower()

def move_file(src, dst):
    src = normalize(src)
    dst = normalize(dst)
    try:
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.move(src, dst)
        print(f"Moved: {os.path.basename(src)} → {os.path.basename(os.path.dirname(dst))}")
    except FileNotFoundError:
        print(f"File tidak ditemukan: {repr(src)}")
    except PermissionError:
        print(f"Tidak punya izin akses: {repr(src)}")
    except Exception as e:
        print(f"Error saat memindahkan {repr(src)}: {e}")

def organize_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isdir(file_path):
            continue

        ext = get_ext(filename)

        for cat, exts in FOLDERS.items():
            if ext in exts:
                move_file(file_path, os.path.join(folder_path, cat, filename))
                break
        else:
            move_file(file_path, os.path.join(folder_path, "Others", filename))

if __name__ == "__main__":
    path = input("Masukkan path folder (contoh: D:/Downloads): ").strip('"')
    if os.path.exists(path):
        organize_folder(path)
    else:
        print("Path tidak ditemukan.")