#!/usr/bin/env python

from pathlib import Path
import yaml


def generate_command_readme(command, prefix):
    readme = []
    examples = []
    toc_entry = f"* [`{prefix} {command['name']}`](#{prefix}-{command['name'].replace(' ', '-')})"
    readme.append(f"#### Command: {toc_entry}\n")
    readme.append(f"{command['description']}\n")
    if "arguments" in command and len(command["arguments"]) > 0:
        readme.append("\nArguments:\n")
        for argument in command["arguments"]:
            readme.append(f"- `{argument['name']}`: {argument['description']}\n")
    if "options" in command and len(command["options"]) > 0:
        readme.append("\nOptions:\n")
        for option in command["options"]:
            readme.append(f"- `{option['name']}`: {option['description']}\n")
    readme.append(f"\nUsage:\n")
    readme.append("```bash\n")
    readme.append(f"{prefix} {command['name']} <arguments> <options>\n")
    readme.append("```\n")
    if "example" in command:
        examples.append(f"Example for {toc_entry}:\n")
        examples.append("```bash\n")
        examples.append(f"{prefix} {command['name']} {command['example']}\n")
        examples.append("```\n")
    if "commands" in command:
        for subcommand in command["commands"]:
            sub_readme, sub_examples, sub_toc_entry = generate_command_readme(
                subcommand, f"{prefix} {command['name']}"
            )
            readme.extend(sub_readme)
            examples.extend(sub_examples)
    return readme, examples, toc_entry


def generate_readme(yaml_string):
    spec = yaml.safe_load(yaml_string)

    readme = []
    examples = []
    toc = []

    readme.append(f"# {spec['name']}\n")
    readme.append(f"{spec['description']}\n")

    readme.append("## Table of Contents\n")
    readme.append("* [Installation](#installation)\n")
    readme.append("* [Usage](#usage)\n")
    readme.append("* [Examples](#examples)\n")

    readme.append("## Installation\n")
    readme.append("Replace `<version>` with the version you want to install.\n")
    readme.append("You can install this package using pip, npm or homebrew:\n")

    readme.append("### Homebrew:\n")
    readme.append("```bash\n")
    readme.append("brew install " + spec["name"] + "\n")
    readme.append("```\n")

    readme.append("### NPM:\n")
    readme.append("```bash\n")
    readme.append("npm install -g " + spec["name"] + "\n")
    readme.append("```\n")

    readme.append("### Pip:\n")
    readme.append("```bash\n")
    readme.append("pip install " + spec["name"] + "\n")
    readme.append("```\n")

    readme.append("## Usage\n")

    for module in spec["modules"]:
        readme.append(f"### {module['name']}\n")
        toc.append(f"* [{module['name']}](#{module['name'].replace(' ', '-')})")
        for command in module["commands"]:
            command_readme, command_examples, toc_entry = generate_command_readme(
                command, f"{spec['binary_name']} {module['name']}"
            )
            readme.extend(command_readme)
            examples.extend(command_examples)
            toc.append(toc_entry)

    readme.append("## Plugins\n")
    toc.append("* [Plugins](#plugins)")
    for plugin in spec["plugins"]:
        readme.append(f"### {plugin['name']}\n")
        toc.append(f"* [{plugin['name']}](#{plugin['name'].replace(' ', '-')})")
        for command in plugin["commands"]:
            command_readme, command_examples, toc_entry = generate_command_readme(
                command, f"{spec['binary_name']} {plugin['name']}"
            )
            readme.extend(command_readme)
            examples.extend(command_examples)
            toc.append(toc_entry)

    readme = readme[:3] + toc + readme[3:]

    readme.append("## Examples\n")
    readme.extend(examples)

    return "\n".join(readme)


spec = Path("./planning/spec.yaml").read_text()

with open("README.md", "w") as file:
    file.write(generate_readme(spec))
