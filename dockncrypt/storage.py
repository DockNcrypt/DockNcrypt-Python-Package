import json
import os

CONFIG_FILE = os.path.expanduser("~/.dockncrypt.json")

def save_config(email, domain, endpoint):
    with open(CONFIG_FILE, "w") as f:
        json.dump({"email": email, "domain": domain, "endpoint": endpoint}, f)

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return None
