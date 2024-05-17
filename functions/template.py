import os
import pyperclip


supported_template_types = ['vhdl', 'verilog']

def get_template(template_type, template_name):
    template_file = './templates/' + template_type + '.txt'
    if not os.path.isfile(template_file):
        print(f"Template file '{template_file}' not found.")
        return None
    
    with open(template_file, 'r') as file:
        content = file.read()
    
    templates = {}
    current_template = None
    for line in content.splitlines():
        if line.endswith(':'):
            current_template = line[:-1]
            templates[current_template] = []
        elif current_template:
            templates[current_template].append(line)
    
    if template_name in templates:
        return '\n'.join(templates[template_name])
    else:
        print(f"Template '{template_name}' not found.")
        return None

def template(template_type, template_name):
    if template_type in supported_template_types:
        template_content = get_template(template_type, template_name)
        if template_content:
            pyperclip.copy(template_content)
            print(f"Copied '{template_type}' template '{template_name}' to clipboard.")
    else:
        print(f"Template type '{template_type}' is not supported.")