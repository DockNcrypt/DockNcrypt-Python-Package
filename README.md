# 🔐 Dockncrypt

Automate HTTPS setup for your projects using **Docker + Nginx + Certbot**, with a single CLI tool.

> Ideal for devs, internal tools, and college events that need SSL — fast and clean.

---

## ⚡ Features

- 🔧 One-command scaffolding with Nginx + Certbot + Docker Compose
- 🔐 Automatic Let's Encrypt SSL certificate generation
- 🧱 Reverse proxy with backend + static routing
- ✏️ Configurable domain/email setup that doesn’t overwrite manual edits
- 🧹 Easy cleanup of certificate volumes when needed
- 🐳 Clean Docker-based structure — no system-wide installs needed

---

## 📦 Installation

> Requires **Python ≥ 3.8** and **Docker** installed and running.

### Recommended (Safe): Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install .
```
## 🚀 Usage
Initialize a new project:
```
dockncrypt init
```
Start services:
```
dockncrypt run
```
Start with optional flags:
```
dockncrypt run --build --detach
```
Stop containers:
```
dockncrypt stop
```
Clear certificate volumes:
```
dockncrypt clear
```
Edit domain/email (without losing custom Nginx edits):
```
dockncrypt edit
```
Help:
```
dockncrypt --help
```
## 🧰 Commands Overview

| Command               | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| `dockncrypt init`     | 🔧 Scaffold the project (prompts for domain, endpoint & email)                         |
| `dockncrypt run`      | 🚀 Run all services using Docker Compose                                     |
| `dockncrypt stop`     | 🧯 Stop all running containers                                                |
| `dockncrypt clear`    | 🧹 Delete volumes (`certbot_challenges`, `letsencrypt`)                      |
| `dockncrypt edit`     | ✏️  Update domain/email/endpoint & regenerate templates (without clobbering edits)    |

## 🗂 Project Structure
After running dockncrypt init, you’ll get:

```
.
├── Dockerfile                 # Backend Dockerfile
├── docker-compose.yml         # Main orchestrator
├── nginx/
│  ├── Dockerfile             # 
│   └── nginx.conf             # HTTPS reverse proxy config
├── nginx-certbot/
│   ├── Dockerfile             # Lightweight nginx for ACME challenge
│   └── nginx-certbot.conf
└── .dockncrypt.json           # Internal config store (email/domain)
```

## 🔐 Safe Template Detection
Dockncrypt-generated files include this comment at the top:
```
# dockncrypt-template-signature: do-not-edit
```
As long as this comment exists, files may be automatically overwritten when running dockncrypt edit.

If you remove or edit the file manually, it will be preserved.

If you want to reset files run dockncrypt init again

## 🧠 Requirements
Docker + Docker Compose

Python ≥ 3.8

A domain name pointed to your machine’s public IP

Open ports 80 and 443

## 📝 License
MIT License

## 🌐 Connect

**Project Repo** 👉 [github.com/DockNcrypt/DockNcrypt](https://github.com/DockNcrypt/DockNcrypt)

**Creator** 👉 [samirwankhede.in](https://samirwankhede.in)

**Python Package** 👉 [github.com/DockNcrypt/DockNcrypt-Python-Package](https://github.com/DockNcrypt/DockNcrypt-Python-Package)

---


