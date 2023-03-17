import unittest
from the_bank import Account, Bank


class TestBank(unittest.TestCase):

    def setUp(self):
        self.bank = Bank()
        self.acc_valid_1 = Account('Sherlock Holmes',
                                   zip='NW1 6XE',
                                   addr='221B Baker street',
                                   value=1000.0)
        self.acc_valid_2 = Account('James Watson',
                                   zip='NW1 6XE',
                                   addr='221B Baker street',
                                   value=25000.0,
                                   info=None)

        self.acc_invalid_1 = Account("Adam",
                                     value=42,
                                     zip='0',
                                     addr='Somewhere')
        self.acc_invalid_2 = Account("Bender Bending Rodríguez",
                                     zip='1',
                                     addr='Mexico',
                                     value=42)
        self.acc_invalid_3 = Account("Charlotte",
                                     zip='2',
                                     addr='Somewhere in the Milky Way',
                                     value=42)
        self.acc_invalid_4 = Account("Douglass",
                                     zip='42',
                                     addr='boulevard bessieres',
                                     value=42)
        self.acc_invalid_5 = Account("Edouard",
                                     zip='3',
                                     addr='France',
                                     value=42)

    def test_valid_account(self):
        self.assertEqual(self.acc_valid_1.name, 'Sherlock Holmes')
        self.assertEqual(self.acc_valid_1.zip, 'NW1 6XE')
        self.assertEqual(self.acc_valid_1.addr, '221B Baker street')
        self.assertEqual(self.acc_valid_1.value, 1000.0)

    def test_invalid_account(self):
        with self.assertRaises(AttributeError):
            Account("Adam", value=-42, zip='12345', addr='Somewhere')
        with self.assertRaises(AttributeError):
            Account("Bender Bending Rodríguez", zip='12', addr='Mexico')
        with self.assertRaises(AttributeError):
            Account("Charlotte", zip='34', addr='Somewhere in the Milky Way',
                    value='42')
        with self.assertRaises(AttributeError):
            Account("Douglass", zip='42', addr='boulevard bessieres')
        with self.assertRaises(AttributeError):
            Account("Edouard", value='42', zip='34567')

    def test_add_valid_account(self):
        self.assertTrue(self.bank.add(self.acc_valid_1))
        self.assertEqual(len(self.bank.accounts), 1)

    def test_add_invalid_account(self):
        self.assertFalse(self.bank.add(self.acc_invalid_1))
        self.assertEqual(len(self.bank.accounts), 0)

    def test_transfer_valid_account(self):
        self.bank.add(self.acc_valid_1)
        self.bank.add(self.acc_valid_2)

        # Transfer 500 from acc_valid_2 to acc_valid_1
        self.assertTrue(self.bank.transfer(self.acc_valid_2.name, self.acc_valid_1.name, 500))
        self.assertEqual(self.acc_valid_1.value, 1500.0)
        self.assertEqual(self.acc_valid_2.value, 24500.0)

        # Transfer 1000 from acc_valid_1 to acc_valid_2
        self.assertTrue(self.bank.transfer(self.acc_valid_1.name, self.acc_valid_2.name, 1000))
        self.assertEqual(self.acc_valid_1.value, 500.0)
        self.assertEqual(self.acc_valid_2.value, 25500.0)

    def test_transfer_invalid_account(self):
        self.bank.add(self.acc_valid_1)

        # Transfer 500 from invalid account to acc_valid_1
        self.assertFalse(self.bank.transfer(self.acc_invalid_1.name, self.acc_valid_1.name, 500))
        self.assertEqual(self.acc_valid_1.value, 1000.0)
        self.assertEqual(self.acc_invalid_1.value, 42)

        # Transfer 1000 from acc_valid_1 to invalid account
        self.assertFalse(self.bank.transfer(self.acc_valid_1.name, self.acc_invalid_1.name, 1000))
        self.assertEqual(self.acc_valid_1.value, 1000.0)
        self.assertEqual(self.acc_invalid_1.value, 42)

