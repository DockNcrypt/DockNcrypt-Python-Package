from setuptools import setup, find_packages

setup(
    name="dockncrypt",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["typer[all]", "jinja2"],
    entry_points={
        'console_scripts': [
            'dockncrypt=dockncrypt.main:app',
        ],
    },
    author="Samir Wankhede",
    description="Automate HTTPS setup with Docker, Nginx, and Certbot.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
