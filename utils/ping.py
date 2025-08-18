import platform
import subprocess

def ping_host(host: str) -> bool:
    flag = "-n" if platform.system().lower().startswith("win") else "-c"
    cmd = ["ping", flag, "1", host]

    result = subprocess.run(
        cmd,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    return result.returncode == 0