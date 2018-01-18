import unittest
from atm_machine import ATMMachine
from sub_atm import SubATMTest


class ATMTest(unittest.TestCase):

    def setUp(self):
        self.notes_dict = {20: 100, 50: 75}
        self.sum_notes = 5750
        self.currency = '$'
        self.atm = ATMMachine(self.notes_dict, self.sum_notes, self.currency)
        self.sub_atm = SubATMTest()

    def test_split_amount_to_notes(self):
        amount = 70
        expected = {50: 1, 20: 1}
        result = self.sub_atm.split_amount_to_notes(amount)
        self.assertEqual(result, expected, 'Result {} and expected dont match {}'.format(result, expected))

    def test_amount_fully_withdrawable(self):
        amount = 70
        expected = True
        result = self.sub_atm.is_amount_fully_withdrawable(amount)
        self.assertEqual(result, expected, 'Result {} and expected dont match {}'.format(result, expected))

    def test_amount_not_withdrawable_decimal(self):
        amount = 70.4
        expected = False
        result = self.sub_atm.is_amount_fully_withdrawable(amount)
        self.assertEqual(result, expected, 'Result {} and expected dont match {}'.format(result, expected))

    def test_amount_not_withdrawable_integer(self):
        amount = 71
        expected = False
        result = self.sub_atm.is_amount_fully_withdrawable(amount)
        self.assertEqual(result, expected, 'Result {} and expected dont match {}'.format(result, expected))

    def test_withdraw_amount_not_fully_withdrawale(self):
        amount = 59
        expected = {}
        result = self.atm.withdraw(amount)
        self.assertEqual(result, expected, 'Result {} and expected dont match {}'.format(result, expected))
        
    def test_withdraw_balance_not_sufficient(self):
        amount = 6000
        expected = {}
        result = self.atm.withdraw(amount)
        self.assertEqual(result, expected, 'Result {} and expected dont match {}'.format(result, expected))

    def test_withdraw_succesful(self):
        amount = 90
        expected = {50: 1,  20: 2}
        result = self.atm.withdraw(amount)
        self.assertEqual(result, expected, 'Result {} and expected dont match {}'.format(result, expected))