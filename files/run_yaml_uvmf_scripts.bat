@set QUESTA_ROOT=C:/questasim64_2021.1
@set UVMF_HOME=C:/UVMF_2023.4/UVMF_2023.4

C:/Python27/python %UVMF_HOME%/scripts/yaml2uvmf.py ALU_in_interface.yaml ALU_out_interface.yaml ALU_util_comp_alu_predictor.yaml ALU_environment.yaml ALU_bench.yaml -d ../uvmf_template_output

pause
