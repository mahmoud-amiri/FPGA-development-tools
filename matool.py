import argparse


from functions.init import init
from functions.commit import commit
from functions.template import template,get_template



def main():
    parser = argparse.ArgumentParser(description='Matool CLI')
    subparsers = parser.add_subparsers(dest='command')

    init_parser = subparsers.add_parser('init', help='Initialize matool in the current directory')
    
    commit_parser = subparsers.add_parser('commit', help='Commit changes and push to git')
    commit_parser.add_argument('message', type=str, help='Commit message')
    
    template_parser = subparsers.add_parser('template', help='Copy a template to the clipboard')
    template_parser.add_argument('-vhdl', dest='template_type', action='store_const', const='vhdl', help='VHDL template')
    template_parser.add_argument('-verilog', dest='template_type', action='store_const', const='verilog', help='Verilog template')
    template_parser.add_argument('template_name', type=str, help='Name of the template to copy')

    args = parser.parse_args()

    if args.command == 'init':
        init()
    elif args.command == 'commit':
        commit(args.message)
    elif args.command == 'template':
        template(args.template_type, args.template_name)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
