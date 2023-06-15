#!/usr/bin/env python

import os
import platform
import sys


def create_directory(directory_path):
    try:
        os.makedirs(directory_path, exist_ok=True)
    except OSError as error:
        print(f"Error in creating directory {directory_path}: {error}")
        sys.exit(1)


def create_symlink(source_file, link_name):
    os_name = platform.system()
    if os_name == "Windows":
        print(f"Windows not supported yet.")
        sys.exit(1)
        # with open(link_name + ".bat", "w") as f:
        #     f.write(f"@echo off\npython {source_file} %*")
    else:  # Unix-based system
        try:
            os.symlink(source_file, link_name)
        except OSError as error:
            print(f"Error in creating symlink {link_name}: {error}")
            sys.exit(1)


def main():
    cli_tool = "smarty_pants.py"  # Path to the CLI tool
    symlink_name_sp = os.path.expanduser("/usr/local/bin/sp")  # Symlink name for 'sp'
    symlink_name_smartypants = os.path.expanduser(
        "/usr/local/bin/smartypants"
    )  # Symlink name for 'smartypants'
    config_directory = os.path.expanduser(
        "~/.smarty_pants"
    )  # Configuration directory in user's home

    create_symlink(cli_tool, symlink_name_sp)
    create_symlink(cli_tool, symlink_name_smartypants)

    create_directory(config_directory)

    print("Smarty Pants installed successfully.")


if __name__ == "__main__":
    main()
