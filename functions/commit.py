import subprocess
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'readme_generator'))
from readme_generator.functions.readme_gen import generate_readme

def commit(message):
    try:
        generate_readme("./project_structure.yaml")
        subprocess.run(['git', 'rev-parse', '--is-inside-work-tree'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(['git', 'add', '.'], check=True)
        subprocess.run(['git', 'commit', '-m', message], check=True)
        subprocess.run(['git', 'push'], check=True)
        print("Changes committed and pushed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")