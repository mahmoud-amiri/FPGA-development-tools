import subprocess
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'readme_generator'))
from readme_generator.functions.readme_gen import generate_readme

def commit(message):
    try:
        if os.path.exists("./project_structure.yaml"):
            generate_readme("./project_structure.yaml")
        else:
            print("Project structure file (project_structure.yaml) not found. README not generated.")
        
        subprocess.run(['git', 'rev-parse', '--is-inside-work-tree'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(['git', 'add', '.'], check=True)
        subprocess.run(['git', 'commit', '-m', message], check=True)
        subprocess.run(['git', 'push'], check=True)
        print("Changes committed and pushed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

def update_submodule(submodule_path, main_repo_path='.', submodule_branch='main', main_repo_branch='main'):
    try:
        if main_repo_path == '.':
            main_repo_path = os.getcwd()
            
        # Ensure the provided paths are valid
        if not os.path.isdir(submodule_path):
            raise ValueError(f"The provided submodule path '{submodule_path}' is not a valid directory.")
        if not os.path.isdir(main_repo_path):
            raise ValueError(f"The provided main repository path '{main_repo_path}' is not a valid directory.")

        # Navigate to the Submodule Directory
        os.chdir(submodule_path)
        
        # Fetch the Latest Changes in the Submodule
        subprocess.run(['git', 'fetch'], check=True)
        
        # Checkout the specified branch in the Submodule
        subprocess.run(['git', 'checkout', submodule_branch], check=True)
        
        # Pull the latest changes in the Submodule
        subprocess.run(['git', 'pull', 'origin', submodule_branch], check=True)
        
        # Navigate Back to the Main Repository Directory
        os.chdir(main_repo_path)
        
        # Update the Submodule Reference in the Main Repository
        if not os.path.isdir(submodule_path):
            raise ValueError(f"Cannot add submodule path '{submodule_path}' to the main repository. Ensure it is a valid path relative to the main repository.")
        
        subprocess.run(['git', 'add', submodule_path], check=True)
        subprocess.run(['git', 'commit', '-m', 'Updated submodule to latest version'], check=True)
        subprocess.run(['git', 'push', 'origin', main_repo_branch], check=True)
        
        print("Submodule updated and changes pushed successfully.")
        
    except ValueError as ve:
        print(f"Validation error: {ve}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")