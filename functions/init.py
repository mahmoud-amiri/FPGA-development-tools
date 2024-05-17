import os

def init():
    os.makedirs('.matool', exist_ok=True)
    os.makedirs('hdl', exist_ok=True)
    os.makedirs('bd', exist_ok=True)
    os.makedirs('cons', exist_ok=True)
    os.makedirs('hls', exist_ok=True)
    os.makedirs('script', exist_ok=True)
    os.makedirs('sdk', exist_ok=True)
    os.makedirs('user_ip', exist_ok=True)
    os.makedirs('xil_ip', exist_ok=True)
    os.makedirs('tb', exist_ok=True)
    readme_path = os.path.join('.matool', 'README.md')
    with open(readme_path, 'w') as readme_file:
        readme_file.write("# Matool\nThis is the configuration folder for matool.")
    print("Initialized .matool directory with README.md")


