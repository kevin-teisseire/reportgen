from data import Analyse
from report import Report
from mailer import Mailer
from argparse import ArgumentParser
import json, os

# Load config file
folder = os.path.dirname(__file__)
jsonPath = os.path.join(folder, 'config.json')
with open(jsonPath) as f:
    config = json.load(f)

# Create parser
parser = ArgumentParser(description='A program to follow your expenses and generate reports.')
# Create 'command' argument
parser.add_argument('command', help='Commands are : send, add, set')
# Create option arguments
parser.add_argument('-d', '--date')
parser.add_argument('-cat', '--category')
parser.add_argument('-ds', '--description')
parser.add_argument('-v', '--value')
parser.add_argument('-r', '--recipient')
parser.add_argument('-c', '--currency')
# Parse arguments
arguments = parser.parse_args()

# Handle empty data file case
try:
    d = Analyse('data.csv', config)
except ValueError as err:
    print(err)
    exit()

# Main program :
argDict = {'highest': d.highest_expense, 
           'lowest': d.lowest_expense, 'total': d.total_expenses}

if __name__ == '__main__':
    if arguments.command == 'send':
        r = Report(d, config['currency'])
        m = Mailer(config)
        m.send_message(r.html)
    elif arguments.command == 'add':
        d.save(arguments.date, arguments.category, arguments.description, arguments.value)
    elif arguments.command == 'set':
        d.set_param(arguments.currency, arguments.recipient, 'config.json')
    elif arguments.command == 'param':
        d.print_param()
    elif arguments.command == 'cat':
        liste_cat = d.list_cat()
        print(f'List : {liste_cat[0]}\nMost used : {liste_cat[1]}')
    elif arguments.command == 'list':
        d.list_exp()
    elif arguments.command == 'count':
        count = d.n_expenses()
        print(f'All time : {count[0]}\nToday : {count[1]}')
    elif arguments.command in argDict.keys():
        res = argDict[arguments.command]()
        print(f'All time : {res[0]:.2f} {config['currency']}\nToday : {res[1]:.2F} {config['currency']}')