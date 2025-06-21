import typer
from .manager import (
    scaffold,
    run_compose,
    stop_compose,
    clear_volumes,
    edit_config
)

app = typer.Typer(help="🔐 Dockncrypt: Automate HTTPS setup with Docker, Nginx, and Certbot.")

@app.command("init", help="🛠️  Scaffold the project with your domain and email.")
def init():
    domain = typer.prompt("Enter domain name")
    email = typer.prompt("Enter email address")
    endpoint = typer.prompt("Enter backend endpoint")
    temp_endpoint = endpoint.split('/')
    endpoint = ""
    for url in temp_endpoint:
        if url != "":
            endpoint+=url
            endpoint+='/'
    scaffold(email, domain, endpoint)

@app.command("run", help="🚀 Run all services using docker compose. Use --detach or -d to run in background. Use --build or -b to rebuild containers after editing")
def run(
    detach: bool = typer.Option(False, "--detach", "-d", help="Run in detached (background) mode"),
    build: bool = typer.Option(False, "--build", "-b", help="Rebuild Docker images before starting")
):
    run_compose(detached=detach, rebuild=build)

@app.command("stop", help="🧯 Stop all running containers using docker compose down.")
def stop():
    stop_compose()

@app.command("clear", help="🧹 Remove certbot and letsencrypt volumes (safe to recreate certs).")
def clear():
    clear_volumes()

@app.command("edit", help="✏️  Reconfigure domain/email and regenerate Nginx/Certbot templates.")
def edit():
    edit_config()

if __name__ == "__main__":
    app()
