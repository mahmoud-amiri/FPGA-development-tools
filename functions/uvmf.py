import shutil
import subprocess

def copy_and_run_uvmf_bat():
    src = f"./script/run_yaml_uvmf_scripts.bat"
    dst = f"./tb/yaml/run_yaml_uvmf_scripts.bat"
    # Copy the file to the destination
    shutil.copy(src, dst)

    # Run the copied file
    subprocess.run(dst, shell=True)
    process = subprocess.Popen(["cmd", "/c", "run_yaml_uvmf_scripts.bat"], cwd='./tb/yaml', stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate()
    
    print("STDOUT:")
    print(stdout)
    print("STDERR:")
    print(stderr)
 