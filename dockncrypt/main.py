import typer
from .manager import scaffold, run, stop, clear, edit

app = typer.Typer()

@app.command()
def init():
    domain = typer.prompt("Enter domain name")
    email = typer.prompt("Enter email address")
    scaffold(email, domain)

@app.command()
def run_():
    run()

@app.command()
def stop():
    stop()

@app.command()
def clear():
    clear()

@app.command()
def edit():
    edit()

if __name__ == "__main__":
    app()
