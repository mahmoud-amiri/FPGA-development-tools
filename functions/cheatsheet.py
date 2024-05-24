import os
import sys
import re

# Keywords definitions (assuming they are defined in keywords.py)
from .keywords import c_keywords, cpp_keywords, python_keywords, tcl_keywords, vhdl_keywords, verilog_keywords, systemverilog_keywords, sh_keywords
sys.path.append(os.path.join(os.path.dirname(__file__), 'cheatsheets_for_digital_designers'))

# ANSI escape codes for colors
class AnsiColors:
    BOLD = '\033[1m'
    RESET = '\033[0m'
    GREEN = '\033[32m'
    CYAN = '\033[36m'

# Function to highlight keywords
def highlight_keywords(code, keywords, color):
    for keyword in keywords:
        code = re.sub(rf'\b{keyword}\b', f"{color}{keyword}{AnsiColors.RESET}", code)
    return code

# Function to extract comments and replace them with placeholders
def extract_comments(code, language):
    comments = []
    placeholders = []

    def replace_with_placeholder(match):
        comments.append(match.group(0))
        return f"__COMMENT_{len(comments)-1}__"

    if language == 'python' or language == 'tcl':
        # Extract single-line comments
        code = re.sub(r'(#.*)', replace_with_placeholder, code)
    elif language in ('c', 'cpp', 'java', 'js', 'verilog', 'systemverilog'):
        # Extract single-line comments (//...)
        code = re.sub(r'(//.*)', replace_with_placeholder, code)
        # Extract multi-line comments (/* ... */)
        code = re.sub(r'(/\*.*?\*/)', replace_with_placeholder, code, flags=re.DOTALL)
    elif language == 'vhdl':
        # Extract VHDL comments
        code = re.sub(r'(--.*)', replace_with_placeholder, code)
    
    return code, comments

# Function to restore comments from placeholders
def restore_comments(code, comments):
    for i, comment in enumerate(comments):
        code = code.replace(f"__COMMENT_{i}__", f"{AnsiColors.GREEN}{comment}{AnsiColors.RESET}")
    return code

# Function to highlight code based on language
def highlight_code(code, language):
    # Extract comments and replace them with placeholders
    code, comments = extract_comments(code, language)
    
    # Highlight keywords in the remaining code
    if language == 'c':
        code = highlight_keywords(code, c_keywords, AnsiColors.CYAN)
    elif language == 'cpp':
        code = highlight_keywords(code, cpp_keywords, AnsiColors.CYAN)
    elif language == 'python':
        code = highlight_keywords(code, python_keywords, AnsiColors.CYAN)
    elif language == 'tcl':
        code = highlight_keywords(code, tcl_keywords, AnsiColors.CYAN)
    elif language == 'vhdl':
        code = highlight_keywords(code, vhdl_keywords, AnsiColors.CYAN)
    elif language == 'verilog':
        code = highlight_keywords(code, verilog_keywords, AnsiColors.CYAN)
    elif language == 'systemverilog':
        code = highlight_keywords(code, systemverilog_keywords, AnsiColors.CYAN)
    elif language == 'sh':
        code = highlight_keywords(code, sh_keywords, AnsiColors.CYAN)    
    else:
        # Handle other languages if needed
        pass
    
    # Restore comments from placeholders
    code = restore_comments(code, comments)
    
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
            for i in range(10):
                if line.startswith('#' * (i + 1) + ' '):
                    formatted_lines.append(f'{AnsiColors.BOLD}{line}{AnsiColors.RESET}')
                    break
            else:
                formatted_lines.append(line)

    return '\n'.join(formatted_lines)

def display_table_of_contents(content):
    def get_heading_indices(level):
        indices = []
        for i, line in enumerate(lines):
            if line.startswith('#' * level + ' '):
                indices.append(i)
        return indices

    def select_heading(level):
        indices = get_heading_indices(level)
        toc_lines = [f'{i+1}. {lines[index][level+1:]}' for i, index in enumerate(indices)]

        for toc_line in toc_lines:
            print(f'{AnsiColors.BOLD}{toc_line}{AnsiColors.RESET}')

        choice = int(input(f'Enter the number of the heading {level} you want to see: ')) - 1

        if 0 <= choice < len(indices):
            start_index = indices[choice]
            end_index = next((indices[i] for i in range(choice + 1, len(indices))), len(lines))
            selected_content = '\n'.join(lines[start_index:end_index])
            return format_markdown(selected_content)
        else:
            print('Invalid choice.')
            return None

    lines = content.split('\n')

    level_2_content = select_heading(2)
    if level_2_content:
        print(level_2_content)
        if get_heading_indices(3):
            level_3_content = select_heading(3)
            if level_3_content:
                print(level_3_content)
                if get_heading_indices(4):
                    level_4_content = select_heading(4)
                    if level_4_content:
                        print(level_4_content)


def list_md_files(directory):
    """
    List all .md files in the given directory and its subdirectories.
    
    :param directory: The root directory to search for .md files.
    :return: A list of paths to .md files.
    """
    md_files = []
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
    
    return md_files

def display_name(file_path):

    file_name = os.path.basename(file_path)
    if file_name.endswith('-cheatsheet.md'):
        return file_name.replace('-cheatsheet.md', '')
    return file_name

def select_md_file(directory):

    md_files = list_md_files(directory)
    
    if not md_files:
        print("No .md files found.")
        return None
    
    print("Found the following .md files:")
    for i, file in enumerate(md_files, start=1):
        print(f"{i}. {display_name(file)}")
    
    while True:
        try:
            choice = int(input("Select a file by number: "))
            if 1 <= choice <= len(md_files):
                return md_files[choice - 1]
            else:
                print(f"Please enter a number between 1 and {len(md_files)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def cheatsheet():
    # Construct the absolute path
    base_path = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current script
    directory = os.path.join(base_path, '..', 'cheatsheets_for_digital_designers', 'CheatSheets')
    readme_path = select_md_file(directory)
    
    print(f"Checking for file at: {readme_path}")  # Debug print to ensure correct path
    
    # Check if the file exists
    if os.path.exists(readme_path):
        with open(readme_path, 'r') as file:
            content = file.read()
            display_table_of_contents(content)
    else:
        raise FileNotFoundError(f"{readme_path} does not exist.")

if __name__ == '__main__':
    cheatsheet()












