import shutil
import subprocess

def is_docker_installed() -> bool:
    return shutil.which("docker") is not None

def assert_docker():
    if not is_docker_installed():
        raise RuntimeError(
            "❌ Docker is not installed or not in your PATH.\n"
        )
    try:
        subprocess.run(["docker", "info"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    except subprocess.CalledProcessError:
        raise RuntimeError("❌ Docker seems to be installed but not running. Start Docker and try again.")
