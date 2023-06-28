import subprocess
import sys

sys.path.insert(0, "/mnt/efs/packages")

# Install PyTorch CPU
subprocess.call([
    sys.executable,
    "-m", 
    "pip", 
    "install", 
    "-r", 
    "requirements/torchcpu.txt",
    "-t",
    "/mnt/efs/packages",
    "--index-url",
    "https://download.pytorch.org/whl/cpu"
])

# Install other requirements
subprocess.call([
    sys.executable,
    "-m",
    "pip",
    "install",
    "-r",
    "requirements/standard.txt",
    "-t",
    "/mnt/efs/packages"
])
