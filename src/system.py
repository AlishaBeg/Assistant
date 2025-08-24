import os
import platform
import psutil
import socket
from datetime import datetime

class System:

    @staticmethod
    def byte_size(size):
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size < 1024:
                return f"{size:.2f} {unit}"
            size /= 1024

    @staticmethod
    def readable_time(timestamp):
        return datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def information():
        uname = platform.uname()
        cpu_freq = psutil.cpu_freq()

        details = [
            ("OS", f"{uname.system} {uname.release} ({uname.version})"),
            ("Machine", uname.machine),
            ("Processor", uname.processor),
            ("CPU Cores (Logical)", psutil.cpu_count(logical=True)),
            ("CPU Cores (Physical)", psutil.cpu_count(logical=False)),
            ("CPU Frequency", f"{cpu_freq.current:.2f} MHz"),
            ("Total RAM", System.byte_size(psutil.virtual_memory().total)),
            ("Available RAM", System.byte_size(psutil.virtual_memory().available)),
            ("Used RAM", System.byte_size(psutil.virtual_memory().used)),
            ("Disk Partitions", ", ".join([p.device for p in psutil.disk_partitions()])),
            ("Total Disk Space", System.byte_size(psutil.disk_usage('/').total)),
            ("Used Disk Space", System.byte_size(psutil.disk_usage('/').used)),
            ("Free Disk Space", System.byte_size(psutil.disk_usage('/').free)),
            ("Boot Time", System.readable_time(psutil.boot_time())),
            ("Hostname", socket.gethostname()),
            ("IP Address", socket.gethostbyname(socket.gethostname())),
            ("Python Version", platform.python_version()),
        ]

        print("\n System Information")
        print("=" * 60)
        for key, value in details:
            print(f"{key:<20} : {value}")
        print("=" * 60)
