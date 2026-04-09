from datetime import date
from data import *
from jinja2 import Environment, FileSystemLoader
import os

class Report():
    """Configure email"""
    def __init__(self, analyse, currency):
        folder = os.path.dirname(__file__)
        self.env = Environment(loader = FileSystemLoader(folder))
        self.template = self.env.get_template('template.html')
        self.currency = currency
        self.categories = analyse.list_cat()
        self.lowest = analyse.lowest_expense()
        self.highest = analyse.highest_expense()
        self.total = analyse.total_expenses()
        self.n_exp = analyse.n_expenses()
        # Binding html template file variables to Report() object:
        self.html = self.template.render(
            date_today = date.today(),
            number_today = self.n_exp[1],
            total_today = format(self.total[1], '.2f'),
            highest_today = format(self.highest[1], '.2f'),
            lowest_today = format(self.lowest[1], '.2f'),
            number_alltime = self.n_exp[0],
            total_alltime = format(self.total[0], '.2f'),
            categories = self.categories[0],
            most_cat = self.categories[1],
            highest_alltime = format(self.highest[0], '.2f'),
            lowest_alltime = format(self.lowest[0], '.2f'),
            html_currency = self.currency
        )

