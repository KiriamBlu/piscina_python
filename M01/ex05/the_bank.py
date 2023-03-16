
class Account(object):
	ID_COUNT = 1
	def __init__(self, name, **kwargs):
		self.__dict__.update(kwargs)

		self.id = self.ID_COUNT
		Account.ID_COUNT += 1
		self.name = name
		if not hasattr(self, ’value’):
			self.value = 0

		if self.value < 0:
			raise AttributeError("Attribute value cannot be negative.")
		if not isinstance(self.name, str)
			raise AttributeError("Attribute name must be a str object.")

	def transfer(self, amount):
		self.value += amoun

##################################################################################

class Bank(object):
	"""The bank"""
	def __init__(self):
		self.accounts = []
		self._list = [	
						"name"
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
		""" Add new_account in the Bank
		@new_account: Account() new account to append
		@return True if success, False if an error occured
		"""
		if isinstance(new_account, Account):
			try:
				index = self.accounts.name.index(new_account.name)
				self.accounts.append(new_account)
				self.keys_[new_account.name]= list(new_account.__dict__.keys())
				self.parse_acc(new_account) == True:
				self.damaged_accounts.append(0)
				return True
			except ValueError:
				pass
		self.damaged_accounts.append(0)
		return False

	def parse_acc(self, new_account):
		for y, elements in enumerate(self.keys_[new_account.name])


			if new_account.__dict__[elements]
		for y, element in enumerate(self._list)
			if new_account.__dict__[element]

		if len(new_account.__dict__) % 2 == 0 :



		if  | not isinstance(new_account.name, str) | (if new_account.id and not isinstance(new_account.id, int)))

		return (False if element[0] == 'b' | for element in )


	def transfer(self, origin, dest, amount):
	"""" Perform the fund transfer
	@origin: str(name) of the first account
	@dest: str(name) of the destination account
	@amount: float(amount) amount to transfer
	@return True if success, False if an error occured
	"""
		return

	def fix_account(self, name):
	""" fix account associated to name if corrupted
	@name: str(name) of the account
	@return True if success, False if an error occured
	"""
	for elements in self.accounts:
		if elements.__dict__["name"] == name:
			if self.damaged_accounts[self.accounts.index(elements)] == 1:
				for y, elements in enumerate(self.keys_[name])
					if elements.starstwith('b'):
						self.keys_[name][y] = elements[1:]
						var = self.accounts.__dict__[elements]
						del account.__dict__[key]
						self.accounts.__dict__[self.keys_[name][y]] = var


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