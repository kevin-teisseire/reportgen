from datetime import date
from os import path
from csv import DictReader, DictWriter
import json

class Analyse():
    """Open, read and analyse the CSV file"""
    def __init__(self, fname, config):
        self.directory = path.dirname(__file__)
        self.filePath = path.join(self.directory, fname)
        self.date_today = str(date.today())
        self.config = config
        self.data = [] # awaiting csv data as dictionnary list
        # Open csv file and save data in self.data:
        with open(self.filePath, 'r') as f:
            reader = DictReader(f)
            for row in reader:
                self.data.append(row)
        if not self.data:
            raise ValueError("\nError : data file is empty\n")
        
    def n_expenses(self):
        "Returns the number of expenses"
        return len(self.data), sum(1 for el in self.data if el['date'] == self.date_today)
    
    def total_expenses(self):
        "Returns the total amount spent"
        total, total_today = 0, 0
        for el in self.data:
            # Total of all time :
            total += float(el['value'])
            # Total of the day :
            if el['date'] == self.date_today:
                total_today += float(el['value'])
        return total, total_today
    
    def highest_expense(self):
        "Returns the highest expense"
        h_exp, h_exp_today = float('-inf'), float('-inf')
        for el in self.data:
            # Highest of all time :
            if float(el['value']) > h_exp:
                h_exp = float(el['value'])
            # Highest of the day :
            if (float(el['value']) > h_exp_today) and el['date'] == self.date_today:
                h_exp_today = float(el['value'])
        if h_exp_today > 0:
            return float(h_exp), float(h_exp_today)
        else:
            return float(h_exp), 0
    
    def lowest_expense(self):
        "Returns the lowest expense"
        # Lowest expense of all :
        l_exp = self.data[0]['value'] # 1st value of the list to compare
        for el in self.data:
            if float(el['value']) < float(l_exp):
                l_exp = float(el['value'])
        # Lowest expense of today :
        data_today = []
        for el in self.data: # creating list of items with today's date
            if el['date'] == self.date_today:
                data_today.append(el)
        if len(data_today) > 0:
            l_exp_today = data_today[0]['value']
            for el in data_today: # Searching for the lowest expense
                if float(el['value']) < float(l_exp_today):
                    l_exp_today = float(el['value'])
            return float(l_exp), float(l_exp_today)
        else:
            return float(l_exp), 0

    def list_cat(self):
        "Returns the different categories"
        # List unique categories :
        cat_li = list(set(el['category'] for el in self.data))
        # Count each category use :
        cat_n = [] # save it in a list of lists
        for cat in cat_li:
            cat_n.append([cat, sum(1 for el in self.data if el['category'] == cat)])
        # Find most used category :
        most_used = cat_n[0]
        for el in cat_n:
            if el[1] > most_used[1]:
                most_used = el
        return cat_li, most_used[0]
    
    def save(self, date_v, cat, desc, val):
        "Add a new expense to the csv file"
        # Verify that all parameters are there:
        requiredParams = {'date':date_v, 'category':cat, 'description':desc, 'value':val}
        for name, value in requiredParams.items():
            if not value:
                print(f'Parameter(s) : --{name} is missing !')
                return
        # Verify date format:
        try:
            date.strptime(date_v, '%Y-%m-%d')
        except ValueError:
            print("Date value incorrect. Format : yyyy-m-d")
            return
        # Verify value format:
        try:
            float(val)
        except ValueError:
            print("Please enter a valid --value (number)")
            return
        # Verify number of words in category:
        if len(cat.split()) > 1:
            print("Please enter a one word category name")
            return
        # Constraint > 3 words < 50 for description
        elif len(desc) > 50 or len(desc) < 3:
            print("please enter between 3 and 50 characters for the description")
            return
        else:
            with open(self.filePath, 'a') as f:
                writer = DictWriter(f, fieldnames=['date', 'category', 'description', 'value'])
                writer.writerow({'date': date_v, 'category': cat.capitalize(), 'description': desc.capitalize(), 'value': val})
            print(f"{desc} - {value} {self.config['currency']} : Added to the list.")
    
    def set_param(self, currency, recipient, file):
        "Change the recipient and the currency"
        self.configPath = path.join(self.directory, file)
        if currency:
            if currency not in ('$', '€', '£', '¥', 'CHF'):
                print("\ninvalid currency. ('$', '€', '£', '¥' or 'CHF')\n")
                return
            else:
                self.config['currency'] = currency
                with open(self.configPath, 'w') as f:
                    json.dump(self.config, f, ensure_ascii=False)
                print(f"\nCurrency changed to '{currency}'\n")
        if recipient:
                self.config['recipient'] = recipient
                with open(self.configPath, 'w') as f:
                    json.dump(self.config, f)
                print(f"\nRecipient changed to '{recipient}'\n")

    def print_param(self):
        "Display user settings"
        print()
        print(f"Currency : {self.config['currency']}")
        print(f"Recipient : {self.config['recipient']}")
        print()

    def list_exp(self):
        for el in self.data:
            el = list(el.values())
            print(f"{el[0]} : {el[1]} - {el[2]} - {el[3]} {self.config['currency']}")
                






    



  