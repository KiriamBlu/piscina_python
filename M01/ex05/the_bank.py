import random
import string


class Account(object):
	ID_COUNT = 1
	def __init__(self, name, **kwargs):
		self.__dict__.update(kwargs)

		self.id = self.ID_COUNT
		Account.ID_COUNT += 1
		self.name = name
		if not hasattr(self, "value"):
			self.value = 0

		if self.value < 0:
			raise AttributeError("Attribute value cannot be negative.")
		if not isinstance(self.name, str):
			raise AttributeError("Attribute name must be a str object.")

	def transfer(self, amount):
		self.value += amount

##################################################################################

class Bank(object):
	def __init__(self):
		self.accounts = []
		self._list = [	
						"name",
						"ref",
						"zip",
						"value",
						"info",
						"other",
						"address"
						]

		self.damaged_accounts = []
		self.keys_ = {}

	def add(self, new_account):
		if isinstance(new_account, Account):
			self.accounts.append(new_account)
			if any(account.name == new_account.name for account in self.accounts):
				return False
			self.keys_[new_account.name]= list(new_account.__dict__.keys())
			self.damaged_accounts.append(0)
			if self.parse_acc(new_account) == True:
				return True
		self.damaged_accounts.append(1)
		return False

	def parse_acc(self, new_account):
		if len(new_account.__dict__) % 2 != 0:
			return False
		if not any(key.startswith('b') for key in new_account.__dict__):
			return False
		if any(key.startswith('zip') or key.startswith('addr') for key in new_account.__dict__):
			return False
		if any(key in ['name', 'id', 'value'] for key in new_account.__dict__):
			return False
		if not isinstance(new_account.name, str):
			return False
		if not isinstance(new_account.id, int):
			return False
		if not isinstance(new_account.value, (int, float)):
			return False
		return True



	def random_string(self, y):
		return ''.join(random.choice(string.ascii_letters) for i in range(y))


	def transfer(self, origin, dest, amount):
		""" Perform the fund transfer
		@origin: str(name) of the first account
		@dest: str(name) of the destination account
		@amount: float(amount) amount to transfer
		@return True if success, False if an error occured
		"""
		if origin in self.accounts and dest in self.accounts and parse_acc(origin) == True and parse_acc(dest) == True:
			if self.accounts[origin].value - amount >= 0 and amount > 0:
				self.accounts[origin].transfer(amount * -1)
				self.accounts[dest].transfer(amount)
				return True
		return False

	def fix_account(self, name):
		var = 0
		string = ""
		for values, elements in enumerate(self.damaged_accounts):
			if self.accounts[values].__dict__["name"] == name:
				var += 1
				if elements == 1:
					if var != 0:
						string = name + str(var)
						while string in self.keys_:
							var += 1
							string = name + str(var)
						setattr(self.accounts[values], "name", string)
						var = self.keys_[name]
						del self.keys_[name]
						setattr(self.keys_, string, var)
					count = [0, 0]
					for y, key in enumerate(self.keys_[name]):
						if key.startswith('b'):
							self.keys_[name][y] = key[1:]
							var = self.accounts.__dict__[key]
							del self.accounts[values].__dict__[key]
							setattr(self.accounts[values], self.keys_[name][y], var)
						if key.startswith('zip'):
							count[0] += 1
						if key.startswith('addr'):
							count[1] += 1
						if key == "name" and not isinstance(self.accounts[values].__dict__[key], str):
							setattr(self.accounts[values], "name", f"user_{values}")
						if key == "id" and not isinstance(self.accounts[values].__dict__[key], int):
							setattr(self.accounts[values], "id",  values)
						if key == "value" and not isinstance(self.accounts[values].__dict__[key], (int, float)):
							setattr(self.accounts[values], "value", 0)
					if count[0] == 0:
						setattr(self.accounts[values], "zip", "")
					if count[1] == 0:
						setattr(self.accounts[values], "address", "")
					if len(self.accounts[values].__dict__) % 2 == 0:
						new_string = self.random_string(15)
						while hasattr(self.accounts[values], new_string):
							new_string = self.random_string(15)
						setattr(self.accounts[values], new_string, "Auxiliary attribute")
					self.damaged_accounts[self.accounts.index(elements)] = 0
					return True
		return False		
	# ... Your code ... 

##################################################################################

'''
bref
zip
value
info
other
address
'''