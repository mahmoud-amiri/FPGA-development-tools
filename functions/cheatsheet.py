import os

# Keywords definitions (assuming they are defined in keywords.py)
from keywords import c_keywords, cpp_keywords, python_keywords, tcl_keywords, vhdl_keywords, verilog_keywords, systemverilog_keywords

# ANSI escape codes for colors
class AnsiColors:
    BLUE = '\033[1;34m'
    GREEN = '\033[1;32m'
    YELLOW = '\033[1;33m'
    CYAN = '\033[1;36m'
    MAGENTA = '\033[1;35m'
    RED = '\033[1;31m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

# Function to highlight keywords
def highlight_keywords(code, keywords, color):
    for keyword in keywords:
        code = code.replace(keyword, f"{color}{keyword}{AnsiColors.RESET}")
    return code

# Function to highlight code based on language
def highlight_code(code, language):
    if language == 'c':
        return highlight_keywords(code, c_keywords, AnsiColors.BLUE)
    elif language == 'cpp':
        return highlight_keywords(code, cpp_keywords, AnsiColors.GREEN)
    elif language == 'python':
        return highlight_keywords(code, python_keywords, AnsiColors.YELLOW)
    elif language == 'tcl':
        return highlight_keywords(code, tcl_keywords, AnsiColors.CYAN)
    elif language == 'vhdl':
        return highlight_keywords(code, vhdl_keywords, AnsiColors.MAGENTA)
    elif language == 'verilog':
        return highlight_keywords(code, verilog_keywords, AnsiColors.RED)
    elif language == 'systemverilog':
        return highlight_keywords(code, systemverilog_keywords, AnsiColors.GREEN)
    else:
        return code

# Function to format Markdown content and highlight code blocks
def format_markdown(content):
    lines = content.split('\n')
    formatted_lines = []
    in_code_block = False
    code_block_language = ''
    code_block_lines = []

    for line in lines:
        if line.startswith('```'):
            if in_code_block:
                # End of code block
                in_code_block = False
                code_block = '\n'.join(code_block_lines)
                highlighted_code_block = highlight_code(code_block, code_block_language)
                formatted_lines.append('```')
                formatted_lines.append(highlighted_code_block)
                formatted_lines.append('```')
                code_block_lines = []
            else:
                # Start of code block
                in_code_block = True
                code_block_language = line[3:].strip()
                formatted_lines.append(line)
        elif in_code_block:
            code_block_lines.append(line)
        else:
            if line.startswith('# '):
                formatted_lines.append(f'{AnsiColors.BOLD}{AnsiColors.BLUE}{line[2:]}{AnsiColors.RESET}')  # Bold blue for H1
            elif line.startswith('## '):
                formatted_lines.append(f'{AnsiColors.BOLD}{AnsiColors.GREEN}{line[3:]}{AnsiColors.RESET}')  # Bold green for H2
            elif line.startswith('### '):
                formatted_lines.append(f'{AnsiColors.BOLD}{AnsiColors.YELLOW}{line[4:]}{AnsiColors.RESET}')  # Bold yellow for H3
            else:
                formatted_lines.append(line)

    return '\n'.join(formatted_lines)

# Function to display the Table of Contents and let the user choose an item
def display_table_of_contents(content):
    lines = content.split('\n')
    toc_lines = []
    toc_indices = []
    index = 1

    for i, line in enumerate(lines):
        if line.startswith('# '):
            toc_lines.append(f'{index}. {line[2:]}')
            toc_indices.append(i)
            index += 1
        elif line.startswith('## '):
            toc_lines.append(f'  {index}. {line[3:]}')
            toc_indices.append(i)
            index += 1
        elif line.startswith('### '):
            toc_lines.append(f'    {index}. {line[4:]}')
            toc_indices.append(i)
            index += 1

    # Display the table of contents
    for toc_line in toc_lines:
        print(f'{AnsiColors.BOLD}{toc_line}{AnsiColors.RESET}')

    # Ask the user to choose an item
    choice = int(input('Enter the number of the section you want to see: ')) - 1

    # Display the selected section
    if 0 <= choice < len(toc_indices):
        start_index = toc_indices[choice]
        end_index = toc_indices[choice + 1] if choice + 1 < len(toc_indices) else len(lines)
        selected_content = '\n'.join(lines[start_index:end_index])
        print(format_markdown(selected_content))
    else:
        print('Invalid choice.')

# Main function to read the README.md file and display its content
def cheatsheet():
    readme_path = os.path.join('.matool', 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r') as file:
            content = file.read()
            display_table_of_contents(content)
    else:
        raise FileNotFoundError(f"{readme_path} does not exist.")

if __name__ == '__main__':
    cheatsheet()


