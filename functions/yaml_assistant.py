import re
import yaml
import json
import os

class HardwareComponent:
    def __init__(self):
        self.parameters = []
        self.ports = []

    def add_parameter(self, line_no, name, input_type, size, description, default_value):
        self.parameters.append({
            'name': name,
            'type': 'int',
            'value': default_value.strip(',')
        })

    def add_input(self, line_no, name, input_type, size, description):
        self.ports.append({
            'name': name,
            'dir': 'input',
            'width': size
        })

    def add_output(self, line_no, name, input_type, size, description):
        self.ports.append({
            'name': name,
            'dir': 'output',
            'width': size
        })

class YamlProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.parsed_yaml = self.parse_yaml_to_dict()

    def parse_yaml_to_dict(self):
        with open(self.file_path, 'r') as file:
            return yaml.safe_load(file)
    

    def recognize_ports_structure(self, code_lines, hardware_component):
        patterns = [
            (re.compile(r'\binput\s+\[([^\]]+)-\d+:\d+\]\s+(\w+)\s*,'), 'input array', '{size}-bit input array for <1>', hardware_component.add_input),
            (re.compile(r'\binput\s+\[([^\]]+):0\]\s+(\w+)\s*,'), 'input array', '({size} + 1)-bit input array for <2>', hardware_component.add_input),
            (re.compile(r'\binput\s+(\w+)\s*,'), 'input single_bit', '{size}-bit input for <3>', hardware_component.add_input),
            (re.compile(r'\binput\s+reg\s+\[([^\]]+)-\d+:\d+\]\s+(\w+)\s*,'), 'input array', '{size}-bit input reg array for <4>', hardware_component.add_input),
            (re.compile(r'\binput\s+logic\s+\[([^\]]+)-\d+:\d+\]\s+(\w+)\s*,'), 'input array', '{size}-bit input logic array for <5>', hardware_component.add_input),
            (re.compile(r'\binput\s+bit\s+\[([^\]]+)-\d+:\d+\]\s+(\w+)\s*,'), 'input array', '{size}-bit input bit array for <6>', hardware_component.add_input),
            (re.compile(r'\binput\s+wire\s+\[([^\]]+)-\d+:\d+\]\s+(\w+)\s*,'), 'input array', '{size}-bit input wire array for <7>', hardware_component.add_input),
            (re.compile(r'\binput\s+reg\s+\[([^\]]+):0\]\s+(\w+)\s*,'), 'input array', '({size} + 1)-bit input reg array for <8>', hardware_component.add_input),
            (re.compile(r'\binput\s+logic\s+\[([^\]]+):0\]\s+(\w+)\s*,'), 'input array', '({size} + 1)-bit input logic array for <9>', hardware_component.add_input),
            (re.compile(r'\binput\s+bit\s+\[([^\]]+):0\]\s+(\w+)\s*,'), 'input array', '({size} + 1)-bit input bit array for <10>', hardware_component.add_input),
            (re.compile(r'\binput\s+wire\s+\[([^\]]+):0\]\s+(\w+)\s*,'), 'input array', '({size} + 1)-bit input wire array for <11>', hardware_component.add_input),
            (re.compile(r'\binput\s+reg\s+(\w+)\s*,'), 'input single_bit', '{size}-bit input reg for <12>', hardware_component.add_input),
            (re.compile(r'\binput\s+logic\s+(\w+)\s*,'), 'input single_bit', '{size}-bit input logic for <13>', hardware_component.add_input),
            (re.compile(r'\binput\s+bit\s+(\w+)\s*,'), 'input single_bit', '{size}-bit input bit for <14>', hardware_component.add_input),
            (re.compile(r'\binput\s+wire\s+(\w+)\s*,'), 'input single_bit', '{size}-bit input wire for <15>', hardware_component.add_input),

            (re.compile(r'\boutput\s+\[([^\]]+)-\d+:\d+\]\s+(\w+)\s*,'), 'output array', '{size}-bit output array for <16>', hardware_component.add_output),
            (re.compile(r'\boutput\s+\[([^\]]+):0\]\s+(\w+)\s*,'), 'output array', '({size} + 1)-bit output array for <17>', hardware_component.add_output),
            (re.compile(r'\boutput\s+(\w+)\s*,'), 'output single_bit', '{size}-bit output single bit for <18>', hardware_component.add_output),
            (re.compile(r'\boutput\s+reg\s+(\w+)\s*,'), 'output single_bit', '{size}-bit output reg for <19>', hardware_component.add_output),
            (re.compile(r'\boutput\s+logic\s+(\w+)\s*,'), 'output single_bit', '{size}-bit output logic for <20>', hardware_component.add_output),
            (re.compile(r'\boutput\s+bit\s+(\w+)\s*,'), 'output single_bit', '{size}-bit output bit for <21>', hardware_component.add_output),
            (re.compile(r'\boutput\s+wire\s+(\w+)\s*,'), 'output single_bit', '{size}-bit output wire for <22>', hardware_component.add_output),
            (re.compile(r'\boutput\s+reg\s+\[([^\]]+)-\d+:\d+\]\s+(\w+)\s*,'), 'output array', '{size}-bit output reg array for <23>', hardware_component.add_output),
            (re.compile(r'\boutput\s+logic\s+\[([^\]]+)-\d+:\d+\]\s+(\w+)\s*,'), 'output array', '{size}-bit output logic array for <24>', hardware_component.add_output),
            (re.compile(r'\boutput\s+bit\s+\[([^\]]+)-\d+:\d+\]\s+(\w+)\s*,'), 'output array', '{size}-bit output bit array for <25>', hardware_component.add_output),
            (re.compile(r'\boutput\s+wire\s+\[([^\]]+)-\d+:\d+\]\s+(\w+)\s*,'), 'output array', '{size}-bit output wire array for <26>', hardware_component.add_output),
            (re.compile(r'\boutput\s+reg\s+\[([^\]]+):0\]\s+(\w+)\s*,'), 'output array', '({size} + 1)-bit output reg array for <27>', hardware_component.add_output),
            (re.compile(r'\boutput\s+logic\s+\[([^\]]+):0\]\s+(\w+)\s*,'), 'output array', '({size} + 1)-bit output logic array for <28>', hardware_component.add_output),
            (re.compile(r'\boutput\s+bit\s+\[([^\]]+):0\]\s+(\w+)\s*,'), 'output array', '({size} + 1)-bit output bit array for <29>', hardware_component.add_output),
            (re.compile(r'\boutput\s+wire\s+\[([^\]]+):0\]\s+(\w+)\s*,'), 'output array', '({size} + 1)-bit output wire array for <30>', hardware_component.add_output),

            (re.compile(r'\bparameter\s+(\w+)\s*=\s*([^\s;]+)\s*,'), 'parameter', 'parameter {name} with default value {default_value}', hardware_component.add_parameter)
        ]

        for pattern_info in patterns:
            pattern, input_type, description_format, add_method = pattern_info
            for line_no, line in enumerate(code_lines, start=1):
                match = pattern.search(line)
                if match:
                    if 'array' in input_type:
                        size = match.group(1)
                        name = match.group(2)
                        size = re.sub(r'-\d+', '', size)
                    elif input_type == 'parameter':
                        size = '1'
                        name = match.group(1)
                        default_value = match.group(2)
                    else:
                        size = '1'
                        name = match.group(1)

                    description = description_format.format(size=size.strip() if isinstance(size, str) else size, name=name, default_value=default_value if input_type == 'parameter' else "")

                    if input_type == 'parameter':
                        add_method(line_no, name, input_type, size, description, default_value)
                    else:
                        add_method(line_no, name, input_type, size, description)


    def convert_to_desired_format(self):
        design_name = list(self.parsed_yaml.keys())[0]
        interfaces = self.parsed_yaml[design_name]['interfaces']
        
        output_dict = {"design_name": design_name, "interfaces": []}
        
        for interface_name, details in interfaces.items():
            hardware_component = HardwareComponent()
            code_lines = details['parameters'] + details['ports']
            self.recognize_ports_structure(code_lines, hardware_component)
            
            interface_dict = {
                "interface_name": interface_name,
                "parameters": hardware_component.parameters,
                "ports": hardware_component.ports
            }
            output_dict["interfaces"].append(interface_dict)
        
        return output_dict

    def switch_directions(self, data_dict):
        for interface in data_dict["interfaces"]:
            for port in interface["ports"]:
                if port["dir"] == "input":
                    port["dir"] = "output"
                elif port["dir"] == "output":
                    port["dir"] = "input"

    def process(self):
        formatted_output = self.convert_to_desired_format()
        self.switch_directions(formatted_output)
        return formatted_output




import yaml

class YamlWriter:
    def __init__(self, output_dict):
        self.output_dict = output_dict

    def generate_interface_yaml(self, interface, design_name):
        interface_name = interface["interface_name"]
        yaml_content = {
            "uvmf": {
                "interfaces": {
                    f"{design_name}_{interface_name}": {
                        "clock": "clk",
                        "reset": "rst",
                        "reset_assertion_level": "False",
                        "config_constraints": [],
                        "config_vars": [],
                        "hdl_typedefs": [
                            {
                            "name" : f"{design_name}_{interface_name}_<type-name>_t" ,
                            "type": "enum bit[n:0] {A = 3'b000, B = 3'b001, C = 3'b010}"
                            }
                        ],
                        "hvl_typedefs": [],
                        "parameters": [
                            {
                                "name": f"{design_name}_{interface_name}_{param['name']}",
                                "type": "int",
                                "value": param['value']
                            }
                            for param in interface["parameters"]
                        ],
                        "ports": [
                            {
                                "name": port['name'],
                                "dir": port['dir'],
                                "width": f"{design_name}_{interface_name}_{port['width']}" if not port['width'].isdigit() else port['width']


                            }
                            for port in interface["ports"]
                        ],
                        "response_info": {
                            "data": [],
                            "operation": "1'b0"
                        },
                        "transaction_constraints": [
                            {
                                "name": f"{port['name']}_c",
                                "value": f"{{ {port['name']} inside {{A, B, C}} }}; "
                            }
                            for port in interface["ports"]
                        ],
                        "transaction_vars": [
                            {
                                "name": port['name'],
                                "type": f"bit [{design_name}_{interface_name}_{port['width']}-1:0]" if not port['width'].isdigit() else f"bit [{port['width']}-1:0]",
                                "iscompare": "True",
                                "isrand": "True"
                            }
                            for port in interface["ports"]
                        ]
                    }
                }
            }
        }
        return yaml_content

    def write_interface_yaml_files(self):
        design_name = self.output_dict["design_name"]
        for interface in self.output_dict["interfaces"]:
            yaml_content = self.generate_interface_yaml(interface, design_name)
            interface_name = interface["interface_name"]
            file_name = f"{design_name}_{interface_name}_interface.yaml"
            with open(f"./tb/yaml/{file_name}", 'w') as file:
                yaml.dump(yaml_content, file, sort_keys=False)
                print(f"Written: {file_name}")

    def generate_env_yaml(self, design_name):
        interface_names = [interface["interface_name"] for interface in self.output_dict["interfaces"]]
        yaml_content = {
            "uvmf": {
                "environments": {
                    design_name: {
                        "agents": [
                            {
                                "name": f"{design_name}_{interface_name}_agent",
                                "type": f"{design_name}_{interface_name}",
                                "initiator_responder": """INITIATOR" or "RESPONDER"""
                            }
                            for interface_name in interface_names
                        ],
                        "analysis_components": [
                            {
                                "name": f"{design_name}_pred",
                                "type": f"{design_name}_predictor"
                            }
                        ],
                        "analysis_exports": [],
                        "analysis_ports": [],
                        "config_constraints": [],
                        "config_vars": [],
                        "parameters": [],
                        "scoreboards": [
                            {
                                "name": f"{design_name}_sb",
                                "sb_type": "uvmf_in_order_scoreboard",
                                "trans_type": f"{design_name}_<interface-names>_transaction"
                            }
                        ],
                        "subenvs": [],
                        "tlm_connections": [
                            {
                                "driver": f"{design_name}_<interface-name>_agent.monitored_ap",
                                "receiver": f"{design_name}_pred.{design_name}_<interface-name>_agent_ae"
                            },
                            {
                                "driver": f"{design_name}_pred.{design_name}_sb_ap",
                                "receiver": f"{design_name}_sb.expected_analysis_export"
                            },
                            {
                                "driver": f"{design_name}_<interface-name>_agent.monitored_ap",
                                "receiver": f"{design_name}_sb.actual_analysis_export"
                            }
                        ]
                    }
                }
            }
        }
        return yaml_content

    def write_env_yaml_file(self):
        design_name = self.output_dict["design_name"]
        yaml_content = self.generate_env_yaml(design_name)
        file_name = f"{design_name}_env.yaml"
        with open(f"./tb/yaml/{file_name}", 'w') as file:
            yaml.dump(yaml_content, file, sort_keys=False)
            print(f"Written: {file_name}")  

    def generate_benches_yaml(self):
        design_name = self.output_dict["design_name"]
        benches_yaml = {
            "uvmf": {
                "benches": {
                    design_name: {
                        "active_passive": [
                            {
                                "bfm_name": f"{design_name}_{interface['interface_name']}_agent",
                                "value": """ACTIVE" or "PASSIVE"""
                            }
                            for interface in self.output_dict["interfaces"]
                        ],
                        "clock_half_period": "5ns",
                        "clock_phase_offset": "9ns",
                        "interface_params": [],
                        "reset_assertion_level": "False",
                        "reset_duration": "200ns",
                        "top_env": design_name
                    }
                }
            }
        }
        return benches_yaml

    def write_benches_yaml_file(self):
        benches_yaml = self.generate_benches_yaml()
        design_name = self.output_dict["design_name"]
        file_name = f"{design_name}_benches.yaml"
        with open(f"./tb/yaml/{file_name}", 'w') as file:
            yaml.dump(benches_yaml, file, sort_keys=False)
            print(f"Written: {file_name}")  

    def generate_util_components_yaml(self):
        design_name = self.output_dict["design_name"]
        interfaces = self.output_dict["interfaces"]
        util_components_yaml = {
            "uvmf": {
                "util_components": {
                    f"{design_name}_predictor": {
                        "analysis_exports": [
                            {
                                "name": f"{design_name}_<interface-name>_agent_ae",
                                "type": f"{design_name}_<interface-name>_transaction #()"
                            }
                        ],
                        "analysis_ports": [
                            {
                                "name": f"{design_name}_sb_ap",
                                "type": f"{design_name}_<interface-name>_transaction #()"
                            }
                        ],
                        "type": "predictor"
                    }
                }
            }
        }
        return util_components_yaml

    def write_util_components_yaml_file(self):
        util_components_yaml = self.generate_util_components_yaml()
        design_name = self.output_dict["design_name"]
        file_name = f"{design_name}_predictor.yaml"
        with open(f"./tb/yaml/{file_name}", 'w') as file:
            yaml.dump(util_components_yaml, file, sort_keys=False)
            print(f"Written: {file_name}")  

    def generate_batch_script_content(self):
        # Read QUESTA_ROOT and UVMF_HOME from config.cf file
        current_script_path = os.path.abspath(__file__)
        current_script_directory = os.path.dirname(current_script_path)
        config_file_path = f"{current_script_directory}/../config.cfg"

        questa_root = None
        uvmf_home = None

        with open(config_file_path, 'r') as config_file:
            config_lines = config_file.readlines()
            for line in config_lines:
                if line.startswith('QUESTA_HOME='):
                    questa_root = line.split('=')[1].strip()
                elif line.startswith('UVMF_HOME='):
                    uvmf_home = line.split('=')[1].strip()

        # Generate the script content
        design_name = self.output_dict["design_name"]
        interface_yaml_file = f"{design_name}_interface.yaml"
        predictor_yaml_file = f"{design_name}_predictor.yaml"
        environment_yaml_file = f"{design_name}_environment.yaml"
        bench_yaml_file = f"{design_name}_bench.yaml"
        script_content = f"""@set QUESTA_ROOT={questa_root}
@set UVMF_HOME={uvmf_home}
{os.path.join(questa_root, 'bin', 'python')} {os.path.join(uvmf_home, 'scripts', 'yaml2uvmf.py')} {interface_yaml_file} {predictor_yaml_file} {environment_yaml_file} {bench_yaml_file} -d ../uvmf
pause"""
        return script_content

    def write_batch_script_file(self):
        script_content = self.generate_batch_script_content()
        design_name = self.output_dict["design_name"]
        file_name = f"{design_name}_generate_uvmf.bat"
        with open(f"./tb/yaml/{file_name}", 'w') as file:
            file.write(script_content)
            print(f"Written: {file_name}")  

    def write_yaml_files(self):
        self.write_interface_yaml_files()
        self.write_env_yaml_file()
        self.write_benches_yaml_file()
        self.write_util_components_yaml_file()
        self.write_batch_script_file()  # Call the method to write batch script file


# Example usage
def yaml_assistant():
    # Assuming processor.process() returns the output_dict
    file_path = './tb/yaml/matool.yaml'
    processor = YamlProcessor(file_path)
    output_dict = processor.process()

    writer = YamlWriter(output_dict)
    writer.write_yaml_files()

if __name__ == "__main__":
    yaml_assistant()


