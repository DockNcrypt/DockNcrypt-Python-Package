import os
import shutil
import subprocess
from .templater import render_templates
from .storage import save_config, load_config
from .check_docker import assert_docker

def scaffold(email, domain, endpoint):
    assert_docker()
    dst = os.getcwd()
    template_dir = os.path.join(os.path.dirname(__file__), "templates")
    shutil.copytree(template_dir, dst, dirs_exist_ok=True, ignore=shutil.ignore_patterns("*.j2"))
    render_templates(domain, email, endpoint, dst)
    save_config(email, domain, endpoint)
    print("✅ Project initialized.")
    print("➡️ Please make sure you have your service's dockerfile in cwd!")

def run_compose(detached, rebuild):
    assert_docker()
    cmd = ["docker", "compose", "up"]
    if rebuild:
        cmd.append("--build")
    if detached:
        cmd.append("-d")
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError:
        print("❌ Failed to run docker compose up.")

def stop_compose():
    assert_docker()
    try:
        subprocess.run(["docker", "compose", "down"], check=True)
    except subprocess.CalledProcessError:
        print("❌ Failed to stop containers.")

def clear_volumes():
    assert_docker()
    project_name = os.path.basename(os.getcwd())
    volume_1 = f"{project_name}_certbot_challenges"
    volume_2 = f"{project_name}_letsencrypt"

    try:
        subprocess.run(["docker", "volume", "rm", volume_1, volume_2], check=True)
        print(f"✅ Removed volumes storing certificates: {volume_1}, {volume_2}")
    except subprocess.CalledProcessError:
        print(f"⚠️ Could not remove one or both volumes: {volume_1}, {volume_2}. They may not exist.")

def edit_config():
    choice = input("🚨 Edit will not change particular file if any prior manual changes have been made.\n " \
    "If you want to enable editing again for all run init\n " \
    "do you wish to continue to edit? (y/n)")
    if choice=='y':
        config = load_config()
        email = input(f"Enter email [{config['email']}]: ") or config["email"]
        domain = input(f"Enter domain [{config['domain']}]: ") or config["domain"]
        endpoint = input(f"Enter endpoint [{config['endpoint']}]: ") or config["endpoint"]
        temp_endpoint = endpoint.split('/')
        endpoint = ""
        for url in temp_endpoint:
            if url != "":
                endpoint+=url
                endpoint+='/'
        render_templates(domain, email, endpoint, os.getcwd())
        save_config(email, domain, endpoint)
        print("✅ Configuration updated.")
        print("➡️ Please run with build flag to apply the changes!")
    elif choice=='n':
        print("➡️ Please always run with build flag to apply the manual changes!")
    else:
        print("Invalid choice.")
