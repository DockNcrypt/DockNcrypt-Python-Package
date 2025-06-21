from jinja2 import Environment, FileSystemLoader
import os

def render_templates(domain, email, endpoint, dst_dir):
    env = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))
    context = {"domain": domain, "email": email, "endpoint": endpoint}

    for name in ["docker-compose.yml.j2", "nginx/nginx.conf.j2","nginx-certbot/nginx-certbot.conf.j2"]:
        template = env.get_template(name)
        output_path = os.path.join(dst_dir, name.replace(".j2", ""))
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w") as f:
            f.write(template.render(context))
