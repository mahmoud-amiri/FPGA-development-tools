import os
import shutil


def init():
    # Ensure the current directory is a Git repository
    if not os.path.isdir('.git'):
        print("The current directory is not a Git repository.")
        #raise AssertionError("The current directory is not a Git repository.")

    # Create necessary directories
    directories = ['.matool', 'hdl', 'bd', 'cons', 'hls', 'script', 'sdk', 'user_ip', 'xil_ip', 'tb']
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

    os.makedirs('tb/yaml', exist_ok=True)

    # Create README.md in .matool directory
    readme_path = os.path.join('.matool', 'README.md')
    with open(readme_path, 'w') as readme_file:
        readme_file.write("# Matool\nThis is the configuration folder for matool.")
    
    # Define the list of source-destination mappings
    file_mapping = [
        {'src': '/files/project_config.yaml', 'dest': './project_config.yaml'},
        {'src': '/files/README.md', 'dest': './hdl/README.md'},
        {'src': '/files/README.md', 'dest': './bd/README.md'},
        {'src': '/files/README.md', 'dest': './cons/README.md'},
        {'src': '/files/README.md', 'dest': './hls/README.md'},
        {'src': '/files/README.md', 'dest': './script/README.md'},
        {'src': '/files/README.md', 'dest': './sdk/README.md'},
        {'src': '/files/README.md', 'dest': './user_ip/README.md'},
        {'src': '/files/README.md', 'dest': './xil_ip/README.md'},
        {'src': '/files/README.md', 'dest': './tb/README.md'},
        {'src': '/files/.gitignore', 'dest': './.gitignore'},
        {'src': '/files/build_mcs.tcl', 'dest': './script/build_mcs.tcl'},
        {'src': '/files/build_pl.tcl', 'dest': './script/build_pl.tcl'},
        {'src': '/files/build_ps.tcl', 'dest': './script/build_ps.tcl'},
        {'src': '/files/gen_bitstream.tcl', 'dest': './script/gen_bitstream.tcl'},
        {'src': '/files/save_bd.tcl', 'dest': './script/save_bd.tcl'},
        {'src': '/files/matool.yaml', 'dest': './tb/yaml/matool.yaml'},
        # Add the rest of the mappings here
    ]

    # Get the absolute path of the current script
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Navigate one folder up
    base_dir_up = os.path.dirname(base_dir)
    print (base_dir_up)
    # Get the size of file_mapping
    file_mapping_size = len(file_mapping)
    print(f"Total files to copy: {file_mapping_size}")

    # Copy files based on the mapping
    for i, mapping in enumerate(file_mapping, 1):
        src = mapping['src']
        dest = mapping['dest']
        if not os.path.exists(base_dir_up + src):
            raise FileNotFoundError(f"Source file {base_dir_up + src} does not exist.")
        shutil.copy2(base_dir_up + src, dest)

    print("Initialized directory")
