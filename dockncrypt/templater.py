from jinja2 import Environment, FileSystemLoader
import hashlib
import os

def file_checksum(path):
    if not os.path.exists(path):
        return None
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def render_templates(domain, email, endpoint, dst_dir, force_overwrite=False):
    env = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))
    context = {"domain": domain, "email": email, "endpoint": endpoint}

    for name in ["docker-compose.yml.j2", "nginx/nginx.conf.j2","nginx-certbot/nginx-certbot.conf.j2"]:
        template = env.get_template(name)
        output_path = os.path.join(dst_dir, name.replace(".j2", ""))
        rendered = template.render(context)
        rendered_checksum = hashlib.sha256(rendered.encode()).hexdigest()

        current_checksum = file_checksum(output_path)

        if force_overwrite or current_checksum is None or current_checksum == rendered_checksum:
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            with open(output_path, "w") as f:
                f.write(rendered)
            print(f"✅ Rendered {name.replace(".j2", "")}")
        else:
            print(f"⚠️  Skipped {name.replace(".j2", "")} (user-modified, not overwriting)")
