import unittest
from data import Analyse
import json, os

class TestAnalyse(unittest.TestCase):
    """Tests unitaires"""
    def setUp(self):
        # Initialise clean config
        self.config = {
            "email": "test@test.com",
            "password": "test_pass",
            "recipient": "recipient@gmail.com",
            "currency": "€"
        }
        self.folder = os.path.dirname(__file__)
        self.jsonF = os.path.join(self.folder, 'test_config.json')
        with open(self.jsonF, 'w') as f:
            json.dump(self.config, f, ensure_ascii=False)
        # Create object Analyse
        self.a = Analyse("test_data.csv", self.config)
        # Unpack tuples in variables
        self.exp_total_alltime, self.exp_total_today = self.a.total_expenses()
        self.n_exp_alltime, self.n_exp_today = self.a.n_expenses()
        self.h_exp_alltime, self.h_exp_today = self.a.highest_expense()
        self.l_exp_alltime, self.l_exp_today = self.a.lowest_expense()
        self.cat_list, self.most_used = self.a.list_cat()
    # Unit tests
    def test_total_expenses_alltime(self):
        self.assertAlmostEqual(self.exp_total_alltime, 4010.70, places=2)
    
    def test_total_expenses_today(self):
        self.assertEqual(self.exp_total_today, 0)
    
    def test_n_expenses_alltime(self):
        self.assertEqual(self.n_exp_alltime, 17)

    def test_n_expenses_today(self):
        self.assertEqual(self.n_exp_today, 0)
    
    def test_highest_expense_alltime(self):
        self.assertEqual(self.h_exp_alltime, 2400.00)

    def test_highest_expense_today(self):
        self.assertEqual(self.h_exp_today, 0)        

    def test_lowest_expense_alltime(self):
        self.assertEqual(self.l_exp_alltime, 5.90)      

    def test_lowest_expense_today(self):
        self.assertEqual(self.l_exp_today, 0)    
    
    def test_list_cat(self):
        self.assertCountEqual(self.cat_list, ['Loisirs', 'loisirs', 'habits', 'Sante', 'Travail', 'Transport', 'Alimentation', 'travail'])    

    def test_most_used(self):
        self.assertEqual(self.most_used, 'Loisirs')
      
    def test_set_param_currency(self):
        self.a.set_param('$', None, 'test_config.json')
        with open(self.jsonF, 'r') as f:
            self.config = json.load(f)
        self.assertEqual(self.config['currency'], '$')

    def test_set_param_email(self):
        self.a.set_param(None, 'test@test.com', 'test_config.json')
        with open(self.jsonF, 'r') as f:
            self.config = json.load(f)
        self.assertEqual(self.config['recipient'], 'test@test.com')

if __name__ == '__main__':
    unittest.main()
