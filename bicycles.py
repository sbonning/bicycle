##Initial build file for the bicycles project, created 5/30 by Sam Bonning
##Will work in conjunction with main.py within the bicycles folder

class Bicycle(object):
	def __init__(self, model, weight, cost)
		self.model = model
		self.weight = weight
		self.cost = cost

class Bikeshop(object):
	def __init__(self, name, margin)
		self.name = name
		self.margin = margin
		self.inventory = {}
		self.sold = {}

	def stockbike(self, model, number):
		"""Adds X number of Y model bikes to inventory of Bikeshop object"""
		##Should pick up the model name to reference the bicycle objects, but not be comprehensive
		##I want it to be scalable so I'll try with a dictionary first and if it won't work because of immutability i'll switch to list (same as sold)
		self.inventory[model] = number
		##this may replace instead of add number, let's see what happens when I test

	def sellbike(self, model):
		"""Takes away 1 of Y model bicycle from Bikeshop object inventory"""
		n = self.inventory[model]
		## i need to store the current inventory before I overwrite it
		self.inventory[model] = n-1
		## maybe there is a better way to do this - will revert
		m = self.sold[model]
		self.sold[model] = m-1 


	def profit(self):
		profit = 0
		for bikes in sold(): 