# Table of Contents

- [Table of Contents](#table-of-contents)
- [MATool: Digital Design Development Assistant](#matool-digital-design-development-assistant)
  - [Key Features](#key-features)
    - [Automated Code Commenting](#automated-code-commenting)
    - [Standardized README Generation](#standardized-readme-generation)
    - [Language-Specific Templates](#language-specific-templates)
    - [Task Automation](#task-automation)
    - [Digital Design Cheatsheets](#digital-design-cheatsheets)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Initialize](#initialize)
    - [Commit](#commit)
    - [Upsub](#upsub)
    - [Template](#template)
    - [Cheatsheet](#cheatsheet)
    - [License](#license)
    - [Contributing](#contributing)
    - [Authors](#authors)

# MATool: Digital Design Development Assistant

MATool is a command-line interface (CLI) tool designed to streamline digital design development for ASIC and FPGA designers. With its versatile set of features, MATool simplifies various aspects of the development process, saving time and enhancing productivity.

## Key Features

### Automated Code Commenting

MATool parses Verilog code and automatically adds comments, reducing the time spent on manual commenting by up to 70%. This feature not only improves code readability but also facilitates collaboration among team members.

### Standardized README Generation

By analyzing code comments, MATool generates a standardized README file for the entire project. This README is updated dynamically with each commit, ensuring that project documentation remains comprehensive and up-to-date.

### Language-Specific Templates

MATool provides a variety of templates in different languages, enabling designers to accelerate development by eliminating repetitive setup tasks. These templates adhere to industry standards and are optimized for compatibility with version control systems like Git.

### Task Automation

MATool includes a collection of TCL and Python scripts to automate repetitive tasks, further streamlining the development workflow. From synthesis to verification, these scripts expedite common processes and enhance efficiency.

### Digital Design Cheatsheets

MATool offers a comprehensive set of cheatsheets tailored specifically for digital designers. These cheatsheets serve as quick references for syntaxes and best practices in various languages, enabling designers to troubleshoot and optimize code more efficiently.


## Installation

To utilize this CLI tool, follow these steps:

1. Clone the repository:

```sh
git clone <repository-url>
cd <repository-directory>
```

2. Install the necessary dependencies:

```sh
pip install -r requirements.txt
```

3. Add the directory to the environment variable.
4. Adjust the path inside the matool.bat file located in the same folder as matool.py.

Once these steps are completed, you can execute matool from the terminal in any directory within your system.

## Usage

The matool CLI provides the following commands:

### Initialize

Initialize matool in the current directory. Before running `matool init`, ensure that you have initialized a git repository using `git init` and connected it to a repository on GitHub or GitLab.

```sh
matool init
```

Run `matool init` to initialize your project with all the necessary files, including standard directories, script files, YAML files, and more.

### Commit

This command combines the following git commands into one:

1. update the README document, which is generated automatically using `matool`.
2. `git add .`: Adds all changes to the staging area.
3. `git commit -m <message>`: Commits changes with the specified message.
4. `git push`: Pushes changes to the remote repository.

It streamlines the process of committing changes, allowing you to update the `README.md` and push changes with a single command.

```sh
matool commit <message>
```

`message`: The commit message.

### Upsub

Update the submodule to the latest version.

```sh
matool upsub <submodule_path> [--main_repo_path <main_repo_path>] [--submodule_branch <submodule_branch>] [--main_repo_branch <main_repo_branch>]
```

`submodule_path`: The path to the submodule.
`--main_repo_path`: The path to the main repository (default is the current directory).
`--submodule_branch`: The branch you want to update in the submodule (default is main).
`--main_repo_branch`: The branch you want to update in the main repository (default is main).
This command fetches the latest changes in the submodule, updates it to the specified branch, and then commits and pushes the updated submodule reference in the main repository.

### Template

Copy a template to the clipboard.

```sh
matool template [-vhdl | -verilog] <template_name>
```

`-vhdl`: Use the VHDL template.
`-verilog`: Use the Verilog template.
`template_name`: The name of the template to copy. These are available template for verilog:

- `doc`: Standard document template.
- `case`: Template for a `case` statement.
- `if`: Template for an `if` statement.
- `always`: Template for an `always` block.
- `module`: Template for a module declaration.

This command will add the selected template to your clipboard. You can then paste it into your code base as per your interest and customize it as needed.

### Cheatsheet

This provides users with a brief overview of the available types of cheatsheets, including programming languages, verification techniques, scripting languages, operating systems, tools, IDEs/text editors, libraries, and other useful topics. It also directs contributors to the contribution guidelines for updating or adding new cheatsheets.

```sh
matool cheatsheet

```

This command will display a list of available cheatsheets, allowing you to choose between them. After selecting a cheatsheet, you can navigate through its table of contents and read the topics of interest. The content of each cheatsheet is presented in a beautifully colorful highlighted manner, ensuring a pleasant reading experience without causing fatigue within the terminal.

### License

This project is licensed under the MIT License - see the LICENSE file for details.

### Contributing

Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests.

### Authors

  Mahmoud Amiri 