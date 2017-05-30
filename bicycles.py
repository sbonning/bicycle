##Initial build file for the bicycles project, created 5/30 by Sam Bonning
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
			## i need to store the current inventory before I overwrite it
			self.inventory[model] = currentStock-1
		except:
			print ("Can't sell that model, don't have it in stock.")
		try:			
			currentSold = self.sold[model]
			self.sold[model] = currentSold+1
		except:
			self.sold[model] = 1

	def profit(self):
		profit = 0
		#for models in self.sold:
		#	self.sold[models]
		#I'll finish coding this later

class Customer(object):
	def __init__(self, name, money):
		self.name = name
		self.money = money
		self.bikesOwned = []

	def buybike(self, model, cost):
		self.bikesOwned.append(model)
		self.money = money - cost

##Here's the initialization of characters script

tina = Customer("tina",200)
pete = Customer("pete", 500)
sue = Customer("sue", 1000)

mongoose = Bicycle("mongoose",60,800)
tokyobike = Bicycle("tokyobike",50,700)
bmx = Bicycle("bmx",70,800)
fixie = Bicycle("fixie", 90,150)
noodlebike = Bicycle("noodlebike",60,200)
basic = Bicycle("basic", 50,500)

bikeshop1 = Bikeshop("Chinatown Bike",0.2)

bikeshop1.stockbike(mongoose,2)
bikeshop1.stockbike(tokyobike,2)
bikeshop1.stockbike(bmx,2)
bikeshop1.stockbike(fixie,2)
bikeshop1.stockbike(noodlebike,2)
bikeshop1.stockbike(basic,2)

##print the name of each customer and bikes they can afford

options = []
for bike in bikeshop1.inventory:
	if (bike.cost*(1+bikeshop1.margin)) <= tina.money:
		options.append((bike.model, bike.cost*(1+bikeshop1.margin)))
	else:
		pass

print ("\n{} can afford:\n {}".format(tina.name,options))

options = []
for bike in bikeshop1.inventory:
	if (bike.cost*(1+bikeshop1.margin)) <= pete.money:
		options.append((bike.model, bike.cost*(1+bikeshop1.margin)))
	else:
		pass

print ("{} can afford:\n {}".format(pete.name,options))

options = []
for bike in bikeshop1.inventory:
	if (bike.cost*(1+bikeshop1.margin)) <= sue.money:
		options.append((bike.model, bike.cost*(1+bikeshop1.margin)))
	else:
		pass

print ("{} can afford:\n {}".format(sue.name,options))

#just checking the inventory
print ("\n\nInventory of the {} shop".format(bikeshop1.name))
for bike in bikeshop1.inventory:
	print (bike.model, ": ", bikeshop1.inventory[bike])

# now we're going to sell a bike



# bikeshop1.sellbike(bmx)

# for bike in bikeshop1.inventory:
# 	print (bike.model)
# 	print (bikeshop1.inventory[bike])

# for bike in bikeshop1.sold:
# 	print (bike.model)
# 	print (bikeshop1.sold[bike])





