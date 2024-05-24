import yaml
import os

from .cheatsheet import format_markdown
class important_files:
    def __init__(self, important_files_list_path, matool_yaml_path, updated_important_files_list_path, info_file_path):
        self.important_files_list_path = important_files_list_path
        self.matool_yaml_path = matool_yaml_path
        self.updated_important_files_list_path = updated_important_files_list_path
        self.info_file_path = info_file_path
        self.data1 = None
        self.data2 = None
        self.design_name = None
        self.interfaces = None
    
    def read_yaml_files(self):
        with open(self.important_files_list_path, 'r') as important_files_list:
            self.data1 = yaml.safe_load(important_files_list)
        
        with open(self.matool_yaml_path, 'r') as matool_yaml:
            self.data2 = yaml.safe_load(matool_yaml)
        
        self.design_name = list(self.data2.keys())[0]
        self.interfaces = self.data2[self.design_name]['interfaces']
    
    def update_paths(self):
        for category in self.data1['Categories']:
            updated_items = []
            for item in self.data1['Categories'][category]:
                if '<interface-name>' in item['file_path']:
                    for interface_name, interface_details in self.interfaces.items():
                        if interface_details['active_passive'] == 'ACTIVE' or 'interface driver bfm' not in item['file_name']:
                            new_item = item.copy()
                            new_item['file_path'] = new_item['file_path'].replace('<design-name>', self.design_name).replace('<interface-name>', interface_name)
                            updated_items.append(new_item)
                else:
                    item['file_path'] = item['file_path'].replace('<design-name>', self.design_name)
                    updated_items.append(item)
            self.data1['Categories'][category] = updated_items
    
    def save_updated_important_files_list(self):
        with open(self.updated_important_files_list_path, 'w') as updated_important_files_list_file:
            yaml.dump(self.data1, updated_important_files_list_file)
    
    def read_info_file(self, info_file_path):
        self.info_data = {}
        with open(info_file_path, 'r') as file:
            lines = file.readlines()
            current_key = None
            current_info = []
            for line in lines:
                if '::' in line:
                    if current_key and current_info:
                        self.info_data[current_key] = ''.join(current_info).strip()
                    parts = line.strip().split('::')
                    category = parts[0]
                    file_name = parts[1].rstrip(':')
                    current_key = f"{category}::{file_name}"
                    current_info = []
                else:
                    current_info.append(line)
            if current_key and current_info:  # To handle the last entry
                self.info_data[current_key] = ''.join(current_info).strip()

    def display_info(self, selected_category, selected_file_name):
        key = f"{selected_category}::{selected_file_name}"
        info = self.info_data.get(key, "No information available for this selection.")
        print(f"Information for {selected_file_name} in {selected_category}:\n{info}")
    
    def read_updated_important_files_list_and_select(self):
        # Read the updated_important_files_list YAML file
        with open(self.updated_important_files_list_path, 'r') as updated_important_files_list_file:
            updated_important_files_list_data = yaml.safe_load(updated_important_files_list_file)
        
        # Print categories
        categories = list(updated_important_files_list_data['Categories'].keys())
        print("Available Categories:")
        for idx, category in enumerate(categories, 1):
            print(f"{idx}. {category}")
        
        # User selects a category
        category_choice = int(input("Select a category by number: ")) - 1
        selected_category = categories[category_choice]
        
        # List file names in the selected category
        file_names = [item['file_name'] for item in updated_important_files_list_data['Categories'][selected_category]]
        print(f"Files in {selected_category}:")
        for idx, file_name in enumerate(file_names, 1):
            print(f"{idx}. {file_name}")
        
        # User selects a file name
        file_choice = int(input("Select a file by number: ")) - 1
        selected_file_name = file_names[file_choice]
        
        # Display information from important_files_cheatsheet.txt
        self.display_info(selected_category, selected_file_name)
        
        # Open the selected file in VS Code
        selected_file_path = updated_important_files_list_data['Categories'][selected_category][file_choice]['file_path']
        os.system(f"code {selected_file_path}")

    def display_info(self, selected_category, selected_file_name):
        key = f"{selected_category}::{selected_file_name}"
        info = self.info_data.get(key, "No information available for this selection.")
        formatted_info = format_markdown(info)
        print(f"Information for {selected_file_name} in {selected_category}:\n{formatted_info}")
    
    def generate_file(self):
        self.read_yaml_files()
        self.update_paths()
        self.save_updated_important_files_list()

    def process(self):
        self.read_info_file(self.info_file_path)
        self.read_updated_important_files_list_and_select()
# Example usage
# processor = important_files('important_files_list.yaml', 'matool_yaml.yaml', 'updated_important_files_list.yaml', 'important_files_cheatsheet.txt')
# processor.generate_file()
# processor.process()


def generate_important_files():
    processor = important_files('./.matool/important_files_list.yaml', './tb/yaml/matool.yaml', './.matool/updated_important_files_list.yaml', './.matool/important_files_cheatsheet.txt')
    processor.generate_file()    
def process_important_files():
    processor = important_files('./.matool/important_files_list.yaml', './tb/yaml/matool.yaml', './.matool/updated_important_files_list.yaml', './.matool/important_files_cheatsheet.txt')
    processor.process()       