import os
import shutil
import subprocess
from .templater import render_templates
from .storage import save_config, load_config
from .check_docker import assert_docker

def scaffold(email, domain):
    assert_docker()
    dst = os.getcwd()
    template_dir = os.path.join(os.path.dirname(__file__), "templates")
    shutil.copytree(template_dir, dst, dirs_exist_ok=True, ignore=shutil.ignore_patterns("*.j2"))
    render_templates(domain, email, dst)
    save_config(email, domain)
    print("✅ Project initialized.")

def run():
    assert_docker()
    subprocess.run(["docker", "compose", "up"])

def stop():
    assert_docker()
    subprocess.run(["docker", "compose", "down"])

def clear():
    assert_docker()
    subprocess.run(["docker", "volume", "rm", "dockncrypt_certbot_challenges", "dockncrypt_letsencrypt"])

def edit():
    config = load_config()
    email = input(f"Enter email [{config['email']}]: ") or config["email"]
    domain = input(f"Enter domain [{config['domain']}]: ") or config["domain"]
    render_templates(domain, email, os.getcwd())
    save_config(email, domain)
    print("✅ Configuration updated.")
