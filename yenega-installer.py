#!/usr/bin/env python
import os
import subprocess
import sys
import importlib
from requests.exceptions import RequestException
import argparse

# Define ANSI escape codes for colors
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def clone_repository(url, destination):
    try:
        subprocess.run(["git", "clone", url, destination], check=True)
    except subprocess.CalledProcessError as e:
        print(f"{Colors.FAIL}Error occurred during git clone: {e}{Colors.ENDC}")
        raise

def create_project(project_name, framework_files_url):
    # Create the project folder
    os.makedirs(project_name)

    # Clone the framework repository from the GitHub URL
    try:
        clone_repository(framework_files_url, project_name)
    except subprocess.CalledProcessError:
        print(f"{Colors.FAIL}Failed to clone the framework repository. Aborting.{Colors.ENDC}")
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
            print(f"{Colors.FAIL}Error occurred during dependency installation: {e}{Colors.ENDC}")
            return

def setup_virtual_environment(project_name):
    try:
        # Create a virtual environment using the 'venv' module
        subprocess.run(["python", "-m", "venv", os.path.join(project_name, "venv")], check=True)
    except subprocess.CalledProcessError as e:
        print(f"{Colors.FAIL}Error occurred during virtual environment setup: {e}{Colors.ENDC}")
        raise

def update_installer(installer_path):
    try:
        subprocess.run(["git", "pull"], cwd=installer_path, check=True)
        print(f"{Colors.OKGREEN}Installer updated successfully.{Colors.ENDC}")
    except subprocess.CalledProcessError as e:
        print(f"{Colors.FAIL}Error occurred during installer update: {e}{Colors.ENDC}")
        raise

def main():
    parser = argparse.ArgumentParser(description="Yenega Installer")
    parser.add_argument("command", choices=["new", "update"], help="Specify the command to perform.")
    parser.add_argument("project_name", help="Specify the project name.")

    args = parser.parse_args()

    command = args.command
    project_name = args.project_name

    if command == "new":
        # Set the PYTHONPATH environment variable
        current_directory = os.getcwd()
        os.environ['PYTHONPATH'] = current_directory

        # GitHub repository URL for framework files
        framework_files_url = "https://gitlab.com/yenega/yenega.git"

        # Create the project folder and clone the framework repository
        create_project(project_name, framework_files_url)

        # Set up the virtual environment
        try:
            setup_virtual_environment(project_name)
        except subprocess.CalledProcessError:
            print(f"{Colors.FAIL}Failed to set up the virtual environment. Aborting.{Colors.ENDC}")
            return

        # Install dependencies
        try:
            install_dependencies(project_name)
        except RequestException as e:
            print(f"{Colors.FAIL}Error occurred during dependency installation: {e}{Colors.ENDC}")
            return

        print(f"{Colors.OKGREEN}Created new project: {project_name}{Colors.ENDC}")

    elif command == "update":
        current_directory = os.getcwd()
        update_installer(current_directory)
        return

    else:
        print(f"{Colors.FAIL}Invalid command: {command}{Colors.ENDC}")

if __name__ == "__main__":
    main()