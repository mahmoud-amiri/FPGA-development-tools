import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'readme_generator'))
from readme_generator.functions.VerilogAnalyzer import VerilogAnalyzer
from readme_generator.functions.VerilogCommentWriter import VerilogCommentWriter


def auto_comment_gen(verilog_path, output_path):
    analyzer = VerilogAnalyzer(verilog_path)
    analyzer.analyze()
    #analyzer.print_results()
    #component_dict = analyzer.get_component_dict()
    #pprint.pprint(component_dict)
    code_lines = analyzer.read_verilog_code()
    analyzer.hardware_component.update_comments_in_dict(code_lines)
    analyzer.hardware_component.remove_duplicate_line_entries()
    analyzer.hardware_component.update_size_in_comment()
    comment_writer = VerilogCommentWriter(analyzer.hardware_component)
    comment_writer.add_comments_to_code(code_lines, output_path)


def auto_readme_gen(verilog_path, output_path):
    analyzer = VerilogAnalyzer(verilog_path)
    analyzer.analyze()
    code_lines = analyzer.read_verilog_code()
    comment_writer = VerilogCommentWriter(analyzer.hardware_component)
    comment_writer.add_description_block_to_code(code_lines, output_path)