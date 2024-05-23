import argparse
from functions.init import init
from functions.git import commit, update_submodule
from functions.template import template, get_template
from functions.cheatsheet import cheatsheet
from functions.comment_readme import auto_comment_gen, auto_readme_gen
from functions.yaml_assistant import yaml_assistant
from functions.questa import copy_and_run_questa_sim_bat
from functions.uvmf import copy_and_run_uvmf_bat
def main():
    parser = argparse.ArgumentParser(description='Matool CLI')
    subparsers = parser.add_subparsers(dest='command')

    init_parser = subparsers.add_parser('init', help='Initialize matool in the current directory')
    
    # Git command with subcommands
    git_parser = subparsers.add_parser('git', help='Git related commands')
    git_subparsers = git_parser.add_subparsers(dest='subcommand')

    commit_parser = git_subparsers.add_parser('commit', help='Commit changes and push to git')
    commit_parser.add_argument('message', type=str, help='Commit message')
    
    upsub_parser = git_subparsers.add_parser('upsub', help='Update the submodule to the latest version')
    upsub_parser.add_argument('submodule_path', type=str, help='Path to the submodule')
    upsub_parser.add_argument('--main_repo_path', type=str, default='.', help='Path to the main repository')
    upsub_parser.add_argument('--submodule_branch', type=str, default='main', help='Branch to update in the submodule')
    upsub_parser.add_argument('--main_repo_branch', type=str, default='main', help='Branch to update in the main repository')

    template_parser = subparsers.add_parser('template', help='Copy a template to the clipboard')
    template_parser.add_argument('-vhdl', dest='template_type', action='store_const', const='vhdl', help='VHDL template')
    template_parser.add_argument('-verilog', dest='template_type', action='store_const', const='verilog', help='Verilog template')
    template_parser.add_argument('template_name', type=str, help='Name of the template to copy')

    cheatsheet_parser = subparsers.add_parser('cheatsheet', help='Open README.md in VS Code')

    comment_parser = subparsers.add_parser('comment', help='Add comments to the input file and save to output file')
    comment_parser.add_argument('input_path', type=str, help='Path to the input file')
    comment_parser.add_argument('output_path', type=str, help='Path to the output file')

    readme_parser = subparsers.add_parser('readme', help='Read the input file and save to output file')
    readme_parser.add_argument('input_path', type=str, help='Path to the input file')
    readme_parser.add_argument('output_path', type=str, help='Path to the output file')

    yaml_parser = subparsers.add_parser('yaml', help='Run the yaml assistant')
    questa_parser = subparsers.add_parser('questa', help='Run the questa')
    uvmf_parser = subparsers.add_parser('uvmf', help='Run the uvmf python script for generating the testbench')

    args = parser.parse_args()

    if args.command == 'init':
        init()
    elif args.command == 'git':
        if args.subcommand == 'commit':
            commit(args.message)
        elif args.subcommand == 'upsub':
            update_submodule(args.submodule_path, args.main_repo_path, args.submodule_branch, args.main_repo_branch)
    elif args.command == 'template':
        template(args.template_type, args.template_name)
    elif args.command == 'cheatsheet':
        cheatsheet()
    elif args.command == 'comment':
        auto_comment_gen(args.input_path, args.output_path)
    elif args.command == 'readme':
        auto_readme_gen(args.input_path, args.output_path)
    elif args.command == 'yaml':
        yaml_assistant()   
    elif args.command == 'questa':
        copy_and_run_questa_sim_bat()  
    elif args.command == 'uvmf':
        copy_and_run_uvmf_bat()          
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
