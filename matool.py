import os
import sys
import argparse
import subprocess

def init():
    # Create .matool directory
    os.makedirs('.matool', exist_ok=True)
    
    # Create README file inside .matool
    readme_path = os.path.join('.matool', 'README.md')
    with open(readme_path, 'w') as readme_file:
        readme_file.write("# Matool\nThis is the configuration folder for matool.")
    
    print("Initialized .matool directory with README.md")

def commit(message):
    try:
        # Check if the current directory is a git repository
        subprocess.run(['git', 'rev-parse', '--is-inside-work-tree'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        # Add all changes to staging
        subprocess.run(['git', 'add', '.'], check=True)
        
        # Commit changes
        subprocess.run(['git', 'commit', '-m', message], check=True)
        
        # Push to remote repository
        subprocess.run(['git', 'push'], check=True)
        
        print("Changes committed and pushed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description='Matool CLI')
    subparsers = parser.add_subparsers(dest='command')

    # Init command
    init_parser = subparsers.add_parser('init', help='Initialize matool in the current directory')
    
    # Commit command
    commit_parser = subparsers.add_parser('commit', help='Commit changes and push to git')
    commit_parser.add_argument('message', type=str, help='Commit message')

    # Parse the arguments
    args = parser.parse_args()

    if args.command == 'init':
        init()
    elif args.command == 'commit':
        commit(args.message)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
