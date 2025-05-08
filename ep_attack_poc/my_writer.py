import platform
import subprocess


def hack_write(*args, **kwargs):
    system_name = platform.system()
    print("Triggered!!!!!!")
    print("Running calculator command...")
    try:
        if system_name == "Windows":
            # Open GUI Calculator
            subprocess.run(["calc.exe"])
        elif system_name in ["Darwin", "Linux"]:  # macOS
            # Open bc from terminal since macOS doesn't have a direct bc GUI
            subprocess.run(["bc"])
        else:
            print(f"Unsupported operating system: {system_name}")
    except Exception as e:
        print(f"An error occurred: {e}")
