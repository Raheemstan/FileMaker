# File Creator

File Creator is a Python script that allows you to generate multiple Python files with specified names in a given directory using relative paths.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Author](#author)

## Features

- Create multiple Python files with custom names.
- Specify the directory where the files will be generated using relative paths.
- Customize the content of the generated files.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Raheemstan/FileMaker.git
   ```

2. Navigate to the project directory:

   ```bash
   cd FileMaker
   ```

## Usage

Run the script by executing the following command:

   ```bash
python create_files.py
 ```

Follow the prompts to enter the following details:

- The directory path where you want to create the files (use a relative path).
- The base name for the files.
- The number of files you want to generate.
- The script will create the specified number of Python files with names like `0-name.py`, `1-name.py`, and so on, in the specified directory.

## Example

   Suppose you run the script with the following inputs:

- Directory: `my_project`
- Name: `hello`
- Number: `3`

   The script will generate the following files in the `my_project` directory:

   my_project/
   ├── 0-hello.py
   ├── 1-hello.py
   ├── 2-hello.py

## Author

[Michael Raheem](https://github.com/Raheemstan)
