import subprocess
import os
import sys

def install_something(thing):
    subprocess.run([sys.executable, "-m", "pip", "install", thing])

def install_deno():
    if (os.name == "nt"):
        subprocess.run(["irm", "https://deno.land/install.ps1", "|", "iex"])
    elif (os.name == "posix"):
        subprocess.run(["curl", "-fsSL", "https://deno.land/install.sh", "|", "sh"])

def install_youtube():
    install_something("yt-dlp")
    subprocess.run([sys.executable, "-m", "pip", "install", "-U", '"yt-dlp[default]"'])
