#!/usr/bin/env python

from pathlib import Path
import yaml
from jinja2 import Template

# Read the YAML specification from the file
spec = Path("./planning/specs/cli_spec.yaml").read_text()
parsed_spec = yaml.safe_load(spec)

# Define the Jinja2 template for the README
readme_template_source = Path("./templates/README.md.j2").read_text()
readme_template = Template(readme_template_source)

# Render the README using the template and parsed YAML data
readme = readme_template.render(parsed_spec)

# Write the rendered README to a file
with open("README.md", "w") as file:
    file.write(readme)
