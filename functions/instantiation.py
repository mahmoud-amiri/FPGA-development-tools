import re
import pyperclip
import sys
import os
import yaml
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from readme_generator.functions.structure_recognizer import StructureRecognizer
from readme_generator.functions.hardware_component import HardwareComponent

def read_verilog_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def find_top_level_module(verilog_code):
    module_pattern = re.compile(r'\bmodule\s+(\w+)\s*#*\s*\([^)]*\)\s*[^)]*\);', re.DOTALL)
    module_match = re.search(module_pattern, verilog_code)
    if not module_match:
        raise ValueError("No module definition found in the file")
    
    module_name = module_match.group(1)
    module_start = module_match.start()
    
    end_pattern = re.compile(r'\bendmodule\b')
    end_match = end_pattern.search(verilog_code, module_start)
    if not end_match:
        raise ValueError("No matching 'endmodule' found for the top-level module")
    
    module_code = verilog_code[module_start:end_match.end()]
    return module_name, module_code

def generate_instantiation_template(module_name, hardware_component):
    parameters = sorted(hardware_component.component['parameters'], key=lambda x: x['line_no'])
    inputs = sorted(hardware_component.component['inputs'], key=lambda x: x['line_no'])
    outputs = sorted(hardware_component.component['outputs'], key=lambda x: x['line_no'])
    inouts = sorted(hardware_component.component['inouts'], key=lambda x: x['line_no'])

    if parameters:
        template = f'{module_name} #(\n'
        for param in parameters:
            template += f'    .{param["name"]}({param["default_value"]}),\n'
        template = template.rstrip(',\n') + '\n) '
    else:
        template = f'{module_name} '

    template += f'{module_name}_inst (\n'

    if inputs or outputs or inouts:
        for input in inputs:
            template += f'    .{input["name"]}({input["name"]}),\n'
        for output in outputs:
            template += f'    .{output["name"]}({output["name"]}),\n'
        for inout in inouts:
            template += f'    .{inout["name"]}({inout["name"]}),\n'
        template = template.rstrip(',\n') + '\n'
    
    template += ');\n'
    return template

def process_verilog_code(verilog_code):
    code_lines = verilog_code.splitlines()

    module_name, module_code = find_top_level_module(verilog_code)

    hardware_component = HardwareComponent()
    recognizer = StructureRecognizer(hardware_component)
    recognizer.recognize_ports_structure(module_code.splitlines())
    hardware_component.remove_duplicate_line_entries()
    instantiation_template = generate_instantiation_template(module_name, hardware_component)
    
    pyperclip.copy(instantiation_template)
    print("The instantiation template has been copied to the clipboard:")
    print(instantiation_template)

def instantiation_file(file_path):
    verilog_code = read_verilog_file(file_path)
    process_verilog_code(verilog_code)

def instantiation_clipboard():
    verilog_code = pyperclip.paste()
    if not verilog_code:
        raise ValueError("No Verilog code found in the clipboard")
    process_verilog_code(verilog_code)

def get_top_level_module_address(yaml_file_path):
    with open(yaml_file_path, 'r') as file:
        data = yaml.safe_load(file)
    
    top_level_module = data['project']['hierarchy'][0]
    module_name = top_level_module['module_name']
    file_path = top_level_module['files'][0]['path']
    
    return module_name, file_path

def top_level_instantiation():
    module_name, file_path = get_top_level_module_address('./project_config.yaml')
    print(file_path)
    instantiation_file(file_path)




