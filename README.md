# STATS CLI

A simple command line tool to analyze programming projects and display basic statistics about languages and files they contain.

## Features
- Analyxe one or more project directories at the same time.
- Analyze folders containing multiple projects.
- Count the total number of files.
- Count the total number of lines.
- Show how many projects use each language.
- Recursively scan project directories.

## Supported languges

The following table shows which extensions are currently recognized.

| Extension |
|----------|
| .py | 
| .js |
| .html |
| .css |
| .java |
| Others |

## Instalation 

Clone the repository and install the project in editable mode.

```bash
git clone
cd Stats
python -m pip install -e .
```

**Depending on your operating system, you may need to take extra steps to make the `stats` command available in every terminal**

## Usage

##### Analyze the current directory

`stats / stats .`

##### Analyze a directory containig multiple projects

`stats  path/to/folder`

Each subdirectory is treated as a separated project.

##### Analyze multiple directories

`stats path/to/folder1 path/to/folder2`

##### Analyze one or more individual projects

Use the `-m` option;

`stats -m path/to/project`

Or analyze multiple projects at the same time

`stats -m path/to/project1 path/to/project2`

#### Show help

`stats --help`

#### Example output 
STATS: ------------------------------------------------ Files: 5 
Lines: 150 

Python 2 
Js     1 
Html   1 
CSS    1 
Java   0 
Others 0

## Requirements 

- Python 3.11 or newer
- `pip`

The project uses `setuptools` for packaging and exposes the stats command through `pyproject.toml`

## License

This project is licensed under the MIT Licnese.