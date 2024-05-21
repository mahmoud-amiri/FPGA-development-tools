import os

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
    """
    Display the name of the file without the path and the '-cheatsheet.md' suffix.
    
    :param file_path: The full path of the file.
    :return: The cleaned name of the file.
    """
    file_name = os.path.basename(file_path)
    if file_name.endswith('-cheatsheet.md'):
        return file_name.replace('-cheatsheet.md', '')
    return file_name

def select_md_file(directory):
    """
    List all .md files in the given directory, assign numbers to them, 
    and return the path of the selected file.
    
    :param directory: The root directory to search for .md files.
    :return: The path of the selected .md file.
    """
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


# Example usage:
base_path = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current script
directory = os.path.join(base_path, '..', 'cheatsheets_for_digital_designers', 'CheatSheets')
selected_file = select_md_file(directory)

if selected_file:
    print(f"You selected: {selected_file}")