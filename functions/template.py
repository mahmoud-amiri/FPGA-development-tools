# import os
# import pyperclip


# supported_template_types = ['vhdl', 'verilog', 'systemverilog', 'tcl', 'python', 'cpp', 'c', 'assertion', 'coverage', 'UVM', 'OVL']

# def get_template(template_type, template_name):
#     script_path = os.path.realpath(__file__)
#     # Get the directory of the current script
#     script_dir = os.path.dirname(script_path)
#     template_file = f"{script_dir}/../templates/{template_type}.txt"
#     if not os.path.isfile(template_file):
#         print(f"Template file '{template_file}' not found.")
#         return None
    
#     with open(template_file, 'r') as file:
#         content = file.read()
    
#     templates = {}
#     current_template = None
#     for line in content.splitlines():
#         if line.endswith(':'):
#             current_template = line[:-1]
#             templates[current_template] = []
#         elif current_template:
#             templates[current_template].append(line)
    
#     if template_name in templates:
#         return '\n'.join(templates[template_name])
#     else:
#         print(f"Template '{template_name}' not found.")
#         return None

# def template(template_type, template_name):
#     if template_type in supported_template_types:
#         template_content = get_template(template_type, template_name)
#         if template_content:
#             pyperclip.copy(template_content)
#             print(f"Copied '{template_type}' template '{template_name}' to clipboard.")
#     else:
#         print(f"Template type '{template_type}' is not supported.")

import os
import pyperclip

def list_template_files(directory):
    files = [f for f in os.listdir(directory) if f.endswith(".tmpl")]
    return files

def display_template_files(files):
    for index, filename in enumerate(files, 1):
        print(f"{index}. {filename}")

def select_template_file(files):
    try:
        choice = int(input("Select a template file by number: ")) - 1
        if choice < 0 or choice >= len(files):
            print("Invalid selection.")
            return None
        return files[choice]
    except ValueError:
        print("Invalid input.")
        return None

def get_templates_from_file(filepath):
    with open(filepath, 'r') as file:
        content = file.read()
    
    templates = {}
    current_template = None
    for line in content.splitlines():
        if line.endswith(':::'):
            current_template = line[:-3].strip()
            templates[current_template] = []
        elif line == ':::':
            current_template = None
        elif current_template:
            templates[current_template].append(line)
    return templates

def display_templates(templates):
    for index, template_name in enumerate(templates.keys(), 1):
        print(f"{index}. {template_name}")

def select_template(templates):
    try:
        choice = int(input("Select a template by number: ")) - 1
        if choice < 0 or choice >= len(templates):
            print("Invalid selection.")
            return None
        return list(templates.keys())[choice]
    except ValueError:
        print("Invalid input.")
        return None

def copy_template_to_clipboard(templates, template_name):
    if template_name in templates:
        template_content = '\n'.join(templates[template_name])
        pyperclip.copy(template_content)
        print(f"Copied template '{template_name}' to clipboard.")
    else:
        print(f"Template '{template_name}' not found.")

def template():
    directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../templates')
    
    files = list_template_files(directory)
    if not files:
        print("No template files found.")
        return

    display_template_files(files)
    selected_file = select_template_file(files)
    if not selected_file:
        return

    file_path = os.path.join(directory, selected_file)
    templates = get_templates_from_file(file_path)
    
    if not templates:
        print("No templates found in the selected file.")
        return

    display_templates(templates)
    template_name = select_template(templates)
    if template_name:
        copy_template_to_clipboard(templates, template_name)

if __name__ == "__main__":
    template()

