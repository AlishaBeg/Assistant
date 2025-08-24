import socket
import psutil
import platform
import uuid
import requests
import subprocess
import os
from datetime import datetime
from .system import System

class Network:

    @staticmethod
    def isOnline(host="8.8.8.8", port=53, timeout=3):
        try:
            socket.setdefaulttimeout(timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
            return True
        except socket.error:
            return False

    @staticmethod
    def hostname():
        return socket.gethostname()

    def ip():
        return socket.gethostbyname(Network.hostname())

    @staticmethod
    def mac():
        return ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff)
                         for elements in range(0, 8*6, 8)][::-1])

    @staticmethod
    def public_ip():
        try:
            return requests.get("https://api.ipify.org").text
        except:
            return "[UNAVAILABLE]"
    
    @staticmethod
    def data_status():
        net_io = psutil.net_io_counters()
        print(f" Sent     : {Network.byte_size(net_io.bytes_sent)}")
        print(f" Received : {Network.byte_size(net_io.bytes_recv)}")


    @staticmethod
    def ping(host="8.8.8.8"):
        print(f"\n📡 Pinging {host} ...")
        cmd = ["ping", "-n", "4", host] if platform.system() == "Windows" else ["ping", "-c", "4", host]
        subprocess.call(cmd)

    @staticmethod
    def information():
        print("\n🌐 Network Information")
        print("=" * 60)

        print(f"Hostname        : {Network.hostname()}")
        print(f"Local IP        : {Network.ip()}")
        print(f"MAC Address     : {Network.mac()}")
        print(f"Public IP       : {Network.public_ip()}")
        print(f"Platform        : {platform.system()} {platform.release()}")

        print("\nInterfaces:")
        for interface, addrs in psutil.net_if_addrs().items():
            print(f"  {interface}:")
            for addr in addrs:
                if addr.family == socket.AF_INET:
                    print(f"    IPv4 : {addr.address}")
                elif addr.family == socket.AF_INET6:
                    print(f"    IPv6 : {addr.address}")
                elif hasattr(psutil, "AF_LINK") and addr.family == psutil.AF_LINK:
                    print(f"    MAC  : {addr.address}")

        Network.data_usage()
        print("=" * 60)


    @staticmethod
    def connections():
        print("\n🔌 Active Connections")
        print("=" * 60)
        for conn in psutil.net_connections(kind="inet"):
            laddr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else ""
            raddr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else ""
            print(f"{conn.status:<15} {laddr:<22} -> {raddr}")

    @staticmethod
    def wifi_info():
        if platform.system() == "Windows":
            print("\n📶 Wi-Fi Networks:")
            os.system("netsh wlan show networks mode=bssid")
        elif platform.system() == "Linux":
            os.system("nmcli dev wifi")
        else:
            print("Wi-Fi info not supported on this OS")