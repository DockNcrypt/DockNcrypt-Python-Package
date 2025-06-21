from jinja2 import Environment, FileSystemLoader
import os

def is_dockncrypt_template(path):
    if not os.path.exists(path):
        return True
    with open(path, "r") as f:
        return "# dockncrypt-template-signature: do-not-edit" in f.readline()

def render_templates(domain, email, endpoint, dst_dir, force_overwrite=False):
    env = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))
    context = {"domain": domain, "email": email, "endpoint": endpoint}

    for name in ["docker-compose.yml.j2", "nginx/nginx.conf.j2","nginx-certbot/nginx-certbot.conf.j2"]:
        template = env.get_template(name)
        output_name = name.replace(".j2", "")
        output_path = os.path.join(dst_dir, output_name)
        rendered = template.render(context)
    
        if force_overwrite or is_dockncrypt_template(output_path):
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            with open(output_path, "w") as f:
                f.write(rendered)
            print(f"✅ Rendered {output_name}")
        else:
            print(f"⚠️  Skipped {output_name} (user-modified, not overwriting)")
