#!/usr/bin/env python

import os
import sys


def remove_symlink(symlink_path):
    try:
        if os.path.islink(symlink_path):
            os.unlink(symlink_path)
        else:
            print(f"No symlink found at {symlink_path}")
    except OSError as error:
        print(f"Error in removing symlink {symlink_path}: {error}")
        sys.exit(1)


def remove_directory(directory_path):
    try:
        if os.path.isdir(directory_path):
            os.rmdir(directory_path)
        else:
            print(f"No directory found at {directory_path}")
    except OSError as error:
        print(f"Error in removing directory {directory_path}: {error}")
        sys.exit(1)


def main():
    symlink_name_sp = os.path.expanduser("/usr/local/bin/sp")
    symlink_name_smartypants = os.path.expanduser("/usr/local/bin/smartypants")
    config_directory = os.path.expanduser("~/.smarty_pants")

    remove_symlink(symlink_name_sp)
    remove_symlink(symlink_name_smartypants)
    remove_directory(config_directory)

    print("Smarty Pants uninstalled successfully.")


if __name__ == "__main__":
    main()
