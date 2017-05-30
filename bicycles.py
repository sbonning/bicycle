##Initial build file for the bicycles project, created 5/30/17 by Sam Bonning
##Will work in conjunction with main.py within the bicycles folder

class Bicycle(object):
	def __init__(self, model, weight, cost):
		self.model = model
		## i want the model to automatically default to whatever the name is??
		self.weight = weight
		self.cost = cost

class Bikeshop(object):
	def __init__(self, name, margin):
		self.name = name
		self.margin = margin
		self.inventory = {}
		self.sold = {}

	def stockbike(self, model, number):
		"""Adds X number of Y model bikes to inventory of Bikeshop object"""
		##Should pick up the model name to reference the bicycle objects, but not be comprehensive
		##I want it to be scalable so I'll try with a dictionary first and if it won't work because of immutability i'll switch to list (same as sold)
		try:
			currentStock = self.inventory[model]
			self.inventory[model] = currentStock + number
		except:
			self.inventory[model] = number
		##this may replace instead of add number, let's see what happens when I test

	def sellbike(self, model):
		"""Takes away 1 of Y model bicycle from Bikeshop object inventory"""
		try:
			currentStock = self.inventory[model]
			1/self.inventory[model]
			# this also throws an exception if inventory = 0 
			self.inventory[model] = currentStock-1
		except:
			return False
		try:			
			currentSold = self.sold[model]
			self.sold[model] = currentSold+1
		except:
			self.sold[model] = 1

	def profit(self):
		profit = 0
		for bike in self.sold:
			profit += bike.cost*(self.margin/(1 - self.margin))*self.sold[bike]
		print ("\nTotal profit of the {} shop: ${}\n".format(self.name, profit))

class Customer(object):
	def __init__(self, name, money):
		self.name = name
		self.money = money
		self.bikesOwned = []
		self.options = []

	def buybike(self, model, cost):
		self.bikesOwned.append(model)
		self.money = self.money - cost
		# couldn't get this to work just saying money

