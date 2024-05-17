
#import os
#import subprocess
#
#def cheatsheet():
#    readme_path = './.matool/README.md'
#    if os.path.exists(readme_path):
#        print(f"Open {readme_path} in VS Code.")
#        subprocess.run(['code', readme_path], check=True)
#    else:
#        raise FileNotFoundError(f"{readme_path} does not exist.")

#import os
#
#def cheatsheet():
#    readme_path = os.path.join('.matool', 'README.md')
#    if os.path.exists(readme_path):
#        with open(readme_path, 'r') as file:
#            content = file.read()
#            print(content)
#    else:
#        raise FileNotFoundError(f"{readme_path} does not exist.")


import os

def format_markdown(content):
    lines = content.split('\n')
    formatted_lines = []
    for line in lines:
        if line.startswith('# '):
            formatted_lines.append(f'\033[1;34m{line[2:]}\033[0m')  # Bold blue for H1
        elif line.startswith('## '):
            formatted_lines.append(f'\033[1;32m{line[3:]}\033[0m')  # Bold green for H2
        elif line.startswith('### '):
            formatted_lines.append(f'\033[1;33m{line[4:]}\033[0m')  # Bold yellow for H3
        else:
            formatted_lines.append(line)
    return '\n'.join(formatted_lines)

def cheatsheet():
    readme_path = os.path.join('.matool', 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r') as file:
            content = file.read()
            formatted_content = format_markdown(content)
            print(formatted_content)
    else:
        raise FileNotFoundError(f"{readme_path} does not exist.")


#import os
#
#def format_markdown(content):
#    lines = content.split('\n')
#    formatted_lines = []
#    line_number = 1
#    headings = []
#
#    for line in lines:
#        if line.startswith('# '):
#            headings.append((line_number, line[2:], 'H1'))
#            formatted_lines.append(f'\033[1;34m{line[2:]}\033[0m')  # Bold blue for H1
#        elif line.startswith('## '):
#            headings.append((line_number, line[3:], 'H2'))
#            formatted_lines.append(f'\033[1;32m{line[3:]}\033[0m')  # Bold green for H2
#        elif line.startswith('### '):
#            headings.append((line_number, line[4:], 'H3'))
#            formatted_lines.append(f'\033[1;33m{line[4:]}\033[0m')  # Bold yellow for H3
#        else:
#            formatted_lines.append(line)
#        line_number += 1
#
#    return '\n'.join(formatted_lines), headings, lines
#
#def print_table_of_contents(headings):
#    print('\033[1;36mTable of Contents\033[0m')  # Cyan bold
#    for index, (line_number, heading, level) in enumerate(headings):
#        print(f'\033[1;34m[{index + 1}]\033[0m {heading}')
#
#def print_section(lines, start_line):
#    end_line = len(lines)
#    for i in range(start_line, len(lines)):
#        if lines[i].startswith('#'):
#            end_line = i
#            break
#    section_content = '\n'.join(lines[start_line:end_line])
#    print(section_content)
#
#def cheatsheet():
#    readme_path = os.path.join('.matool', 'README.md')
#    if os.path.exists(readme_path):
#        with open(readme_path, 'r') as file:
#            content = file.read()
#            formatted_content, headings, lines = format_markdown(content)
#            print_table_of_contents(headings)
#            choice = int(input("Select a heading by number: ")) - 1
#            if 0 <= choice < len(headings):
#                start_line = headings[choice][0] - 1
#                print_section(lines, start_line)
#            else:
#                print("Invalid choice.")
#    else:
#        raise FileNotFoundError(f"{readme_path} does not exist.")
#
