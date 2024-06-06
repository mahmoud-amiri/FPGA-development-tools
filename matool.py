import argparse
from functions.init import init
from functions.git import commit, update_submodule
from functions.template import template
from functions.cheatsheet import cheatsheet
from functions.comment_readme import auto_comment_gen, auto_readme_gen
from functions.yaml_assistant import yaml_assistant
from functions.questa import copy_and_run_questa_sim_bat
from functions.uvmf import copy_and_run_uvmf_bat
from functions.important_files import generate_important_files, process_important_files
from functions.instantiation import instantiation_file, instantiation_clipboard, top_level_instantiation
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
    # template_parser.add_argument('-vhdl', dest='template_type', action='store_const', const='vhdl', help='VHDL template')
    # template_parser.add_argument('-verilog', dest='template_type', action='store_const', const='verilog', help='Verilog template')
    # template_parser.add_argument('-systemverilog', dest='template_type', action='store_const', const='systemverilog', help='Systemverilog template')
    # template_parser.add_argument('-assertion', dest='template_type', action='store_const', const='assertion', help='assertion template')
    # template_parser.add_argument('-ovl', dest='template_type', action='store_const', const='ovl', help='ovl template')
    # template_parser.add_argument('-uvm', dest='template_type', action='store_const', const='uvm', help='uvm template')
    # template_parser.add_argument('-coverage', dest='template_type', action='store_const', const='coverage', help='coverage template')
    # template_parser.add_argument('-c', dest='template_type', action='store_const', const='c', help='c template')
    # template_parser.add_argument('-cpp', dest='template_type', action='store_const', const='cpp', help='cpp template')
    # template_parser.add_argument('-python', dest='template_type', action='store_const', const='python', help='python template')
    # template_parser.add_argument('-tcl', dest='template_type', action='store_const', const='tcl', help='tcl template')
    # template_parser.add_argument('template_name', type=str, help='Name of the template to copy')

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
    important_parser = subparsers.add_parser('important', help='open the important files inside the vscode')
    instantiation_parser = subparsers.add_parser('instantiation', help='Instantiation template generator')
    instantiation_subparsers = instantiation_parser.add_subparsers(dest='subcommand')

    instantiation_default_parser = instantiation_subparsers.add_parser('default', help='Default instantiation')
    instantiation_top_parser = instantiation_subparsers.add_parser('top', help='Top instantiation')
    instantiation_file_parser = instantiation_subparsers.add_parser('file', help='Instantiation from file')
    instantiation_file_parser.add_argument('file_path', type=str, help='Path to the Verilog file')

    args = parser.parse_args()

    if args.command == 'init':
        init()
    elif args.command == 'git':
        if args.subcommand == 'commit':
            commit(args.message)
        elif args.subcommand == 'upsub':
            update_submodule(args.submodule_path, args.main_repo_path, args.submodule_branch, args.main_repo_branch)
    elif args.command == 'template':
        # template(args.template_type, args.template_name)
        template()
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
        generate_important_files()  
    elif args.command == 'important':
        process_important_files()
    elif args.command == 'instantiation':
        if args.subcommand == 'top':
            top_level_instantiation()
        elif args.subcommand == 'file':
            instantiation_file(args.file_path)  
        else:
            instantiation_clipboard()      
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
