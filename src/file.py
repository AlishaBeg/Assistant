import os
import shutil
from datetime import datetime
from .io import Voice
from .system import System


class File:

    @staticmethod
    def pwd():
        Voice.prompt(os.getcwd())

    @staticmethod
    def ls(path="."):
        try:
            for f in os.listdir(path):
                print(f)
        except Exception as e:
            Voice.prompt(f"[ERROR]: {e}")

    @staticmethod
    def read(path):
        if not os.path.exists(path):
            Voice.prompt("File does not exist")
            return
        try:
            with open(path, "r", encoding="utf-8") as file:
                print(file.read())
        except Exception as e:
            Voice.prompt(f"[ERROR]: {e}")

    @staticmethod
    def write(path, data):
        try:
            with open(path, "w", encoding="utf-8") as file:
                file.write(data)
            Voice.prompt(f"[WRITE]: {path}")
        except Exception as e:
            Voice.prompt(f"[ERROR]: {e}")

    @staticmethod
    def append(path, data):
        try:
            with open(path, "a", encoding="utf-8") as file:
                file.write(data)
            Voice.prompt(f"[APPEND]: {path}")
        except Exception as e:
            Voice.prompt(f"[ERROR]: {e}")

    @staticmethod
    def delete(path):
        try:
            os.remove(path)
            Voice.prompt(f"[DELETED]: {path}")
        except Exception as e:
            Voice.prompt(f"[ERROR]: {e}")

    @staticmethod
    def mkdir(path):
        try:
            os.makedirs(path, exist_ok=True)
            Voice.prompt(f"[DIRECTORY CREATED]: {path}")
        except Exception as e:
            Voice.prompt(f"[ERROR]: {e}")

    @staticmethod
    def rmdir(path):
        try:
            os.rmdir(path)
            Voice.prompt(f"[DIRECTORY REMOVED]: {path}")
        except Exception as e:
            Voice.prompt(f"[ERROR]: {e}")

    @staticmethod
    def rename(old, new):
        try:
            os.rename(old, new)
            Voice.prompt(f"[RENAMED]: {old} → {new}")
        except Exception as e:
            Voice.prompt(f"[ERROR]: {e}")

    @staticmethod
    def move(src, dst):
        try:
            shutil.move(src, dst)
            Voice.prompt(f"[MOVED]: {src} → {dst}")
        except Exception as e:
            Voice.prompt(f"[ERROR]: {e}")

    @staticmethod
    def copy(src, dst):
        try:
            shutil.copy2(src, dst)
            Voice.prompt(f"[COPIED]: {src} → {dst}")
        except Exception as e:
            Voice.prompt(f"[ERROR]: {e}")

    @staticmethod
    def touch(path):
        try:
            with open(path, "a"):
                os.utime(path, None)
            Voice.prompt(f"[TOUCHED]: {path}")
        except Exception as e:
            Voice.prompt(f"[ERROR]: {e}")

    @staticmethod
    def detail(path):
        if not os.path.exists(path):
            print(f"[ERROR] Path not found: {path}")
            return

        try:
            info = os.stat(path)
            
            # Detect type
            if os.path.isdir(path):
                type_label = "📁 Folder"
            elif os.path.isfile(path):
                type_label = "📄 File"
            else:
                type_label = "❓ Other"

            details = [
                ("Type", type_label),
                ("Path", path),
                ("Size", File.System.byte_size(info.st_size)),
                ("Permissions", oct(info.st_mode)),
                ("Inode", info.st_ino),
                ("Device", info.st_dev),
                ("Links", info.st_nlink),
                ("Owner UID", info.st_uid),
                ("Owner GID", info.st_gid),
                ("Last Access", File.readable_time(info.st_atime)),
                ("Last Modified", File.readable_time(info.st_mtime)),
                ("Created", File.readable_time(info.st_ctime)),
            ]

            print("\n📌 File Information")
            print("=" * 50)
            for key, value in details:
                print(f"{key:<18} : {value}")
            print("=" * 50)

        except Exception as e:
            print(f"[ERROR]: {e}")

    @staticmethod
    def readable_time(timestamp):
        dt = datetime.fromtimestamp(timestamp)
        today = datetime.now().date()
        if dt.date() == today:
            return f"Today at {dt.strftime('%H:%M')}"
        elif (today - dt.date()).days == 1:
            return f"Yesterday at {dt.strftime('%H:%M')}"
        else:
            return dt.strftime("%Y-%m-%d %H:%M:%S")