import os

def init():
    os.makedirs('.matool', exist_ok=True)
    readme_path = os.path.join('.matool', 'README.md')
    with open(readme_path, 'w') as readme_file:
        readme_file.write("# Matool\nThis is the configuration folder for matool.")
    print("Initialized .matool directory with README.md")


