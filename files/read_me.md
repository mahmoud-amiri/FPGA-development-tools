# How to run

1. Edit the YAML files.
2. click on run_yaml_uvmf_script.bat to generate the template file. You should return one level up to see the generated file. this .bat file does not overwrite any file. if there is any generated file it would skip generating the files.
3. copy the run_bcr_sim.bat to the uvmf_template_output\project_benches\ALU\sim folder and execute it. it would run Questasim.
4. inside Questa sim run this command: run -all
5. now you can see the generated wave form.
6. for exiting the Questa, just run the command: quit -f
7. then press any key on the cmd windows

# Note:

1. please consider to install python version which is written in the .bat file
2. please consider to use uvm which is written in .bat file