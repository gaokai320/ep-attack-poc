import os
import platform
import subprocess


def hack_write(*args, **kwargs):
    print("Attack Triggered!!!!!!")
    print("Running `ls` command...")
    system_name = platform.system()
    home_dir = os.path.expanduser("~")
    try:
        if system_name in ["Darwin", "Linux"]:  # macOS
            subprocess.run(["ls", "-l", home_dir])
        elif system_name == "Windows":
            subprocess.run(["cmd", "/c", "dir", home_dir])
        else:
            print(f"Unsupported operating system: {system_name}")
    except Exception as e:
        print(f"An error occurred: {e}")
