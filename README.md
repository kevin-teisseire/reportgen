![Tests](https://github.com/kevin-teisseire/reportgen/actions/workflows/tests.yml/badge.svg)

# ReportGen - Report generator

Add your expenses and generate a report sent to your email address.

## Installation
```
git clone https://github.com/kevin-teisseire/reportGen
cd reportGen
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
go to gmail and create an application password
echo EMAIL_PASSWORD=your_own_token > .env
python3 main.py set -r youremail@gmail.com 
```
## Use
```
python3 main.py set --currency "$"
python3 main.py add -date "2026-04-04" --category "clothes" --description "shoes" --value 99.99
python3 main.py send
```
## Commands

| Command | Description |
| ------- | ----------- |
| set     | Set email or currency |
| add     | Add an expense |
| send    | Generate and send report |
| param   | View current settings |
| list    | List expenses |
| count  | Count expenses |
| highest | Print highest expenses |
| lowest  | Print lowest expenses |
| total   | Print total expenses |
| cat     | Print categories |

## Options

For all available options : python3 main.py --help

## Tests

This project uses 'unittest' framework to grant fiability to the data analyses.

### Run tests localy 
To run the tests, please ensure to have installed all dependecies, then run:

````bash
python -m unittest discover -s  tests

