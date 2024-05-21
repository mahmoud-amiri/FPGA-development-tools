# Table of Contents

- [Table of Contents](#table-of-contents)
- [Matool CLI](#matool-cli)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Initialize](#initialize)
    - [Commit](#commit)
    - [Template](#template)
    - [Cheatsheet](#cheatsheet)
    - [License](#license)
    - [Contributing](#contributing)
    - [Authors](#authors)

# Matool CLI

This is a command-line interface (CLI) tool called `matool` that provides several commands for initializing a project, committing changes, copying templates, and opening a cheatsheet.

## Installation

To use this CLI tool, clone the repository and install the required dependencies:

```sh
git clone <repository-url>
cd <repository-directory>
pip install -r requirements.txt
```

## Usage

The matool CLI provides the following commands:

### Initialize

Initialize matool in the current directory.

```sh
python matool.py init
```

### Commit

Commit changes and push to git with a commit message.

```sh
python matool.py commit <message>
```

`message`: The commit message.

### Template

Copy a template to the clipboard.

```sh
python matool.py template [-vhdl | -verilog] <template_name>
```

`-vhdl`: Use the VHDL template.
`-verilog`: Use the Verilog template.
`template_name`: The name of the template to copy.

### Cheatsheet

Open README.md in VS Code.

```sh
python matool.py cheatsheet

```

### License

This project is licensed under the MIT License - see the LICENSE file for details.

### Contributing

Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests.

### Authors

  Mahmoud Amiri 