#!/usr/bin/env python

import os
import platform
import sys
import subprocess
from pathlib import Path


def create_directory(directory_path):
    try:
        os.makedirs(directory_path, exist_ok=True)
    except OSError as error:
        print(f"Error in creating directory {directory_path}: {error}")
        sys.exit(1)


def create_symlink(source_file, link_name):
    if os.path.exists(link_name):
        print(f"Link {link_name} already exists.")
        return
    os_name = platform.system()
    if os_name == "Windows":
        print(f"Windows not supported yet.")
        sys.exit(1)
    else:  # Unix-based system
        try:
            os.symlink(source_file, link_name)
        except OSError as error:
            print(f"Error in creating symlink {link_name}: {error}")
            sys.exit(1)


def install_dependencies():
    requirements_file = Path(__file__).resolve(strict=False).parent / "requirements.txt"
    subprocess.run(
        [sys.executable, "-m", "pip", "install", "-r", str(requirements_file)]
    )


def main():
    cli_tool = Path(__file__).resolve(strict=False).parent / "./smarty_pants.py"
    symlink_name_sp = os.path.expanduser("~/bin/sp")
    symlink_name_smartypants = os.path.expanduser("~/bin/smartypants")
    config_directory = os.path.expanduser("~/.smarty_pants")

    install_dependencies()

    create_symlink(cli_tool, symlink_name_sp)
    create_symlink(cli_tool, symlink_name_smartypants)

    create_directory(config_directory)

    print("Smarty Pants installed successfully.")


if __name__ == "__main__":
    main()
