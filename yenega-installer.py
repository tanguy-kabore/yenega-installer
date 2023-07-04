#!/usr/bin/env python
import os
import subprocess
import sys
import importlib
import requests
from requests.exceptions import RequestException

def clone_repository(url, destination):
    try:
        subprocess.run(["git", "clone", url, destination], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred during git clone: {e}")
        raise

def create_project(project_name, framework_files_url):
    # Create the project folder
    os.makedirs(project_name)

    # Clone the framework repository from the GitHub URL
    try:
        clone_repository(framework_files_url, project_name)
    except subprocess.CalledProcessError:
        print("Failed to clone the framework repository. Aborting.")
        return

def install_dependencies(project_name):
    # Activate the virtual environment
    activate_env_command = os.path.join(project_name, "venv", "Scripts", "activate") if os.name == "nt" \
        else "source " + os.path.join(project_name, "venv", "bin", "activate")
    subprocess.run(activate_env_command, shell=True)

    # Check if the dependencies are already installed in the system or virtual environment
    dependencies = ["mysql-connector-python", "Pillow"]
    missing_dependencies = [dep for dep in dependencies if importlib.util.find_spec(dep) is None]

    # Install missing dependencies using pip in the virtual environment
    if missing_dependencies:
        try:
            subprocess.run(["python", "-m", "pip", "install"] + missing_dependencies, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error occurred during dependency installation: {e}")
            return

def setup_virtual_environment(project_name):
    try:
        # Create a virtual environment using the 'venv' module
        subprocess.run(["python", "-m", "venv", os.path.join(project_name, "venv")], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred during virtual environment setup: {e}")
        raise

def main():
    if len(sys.argv) < 3:
        print("Usage: python yenega-installer.py new <project_name>")
        return

    command = sys.argv[1]
    project_name = sys.argv[2]

    if command != "new":
        print(f"Invalid command: {command}")
        return

    # Check if the project already exists
    if os.path.exists(project_name):
        print(f"Error: Project '{project_name}' already exists.")
        return

    # GitHub repository URL for framework files
    framework_files_url = "https://github.com/baowendnere/yenega.git"

    # Create the project folder and clone the framework repository
    create_project(project_name, framework_files_url)

    # Set up the virtual environment
    try:
        setup_virtual_environment(project_name)
    except subprocess.CalledProcessError:
        print("Failed to set up the virtual environment. Aborting.")
        return

    # Install dependencies
    try:
        install_dependencies(project_name)
    except RequestException as e:
        print(f"Error occurred during dependency installation: {e}")
        return

    print(f"Created new project: {project_name}")

if __name__ == "__main__":
    main()
