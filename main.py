##main script running the Bicycles project 
## created by Sam Bonning 5/30/17

##Here's the initialization of characters script

import random

tina = Customer("tina",200)
pete = Customer("pete",500)
sue = Customer("sue",1000)

mongoose = Bicycle("mongoose",60,780)
tokyobike = Bicycle("tokyobike",50,700)
bmx = Bicycle("bmx",70,800)
fixie = Bicycle("fixie", 90,150)
noodlebike = Bicycle("noodlebike",60,200)
basic = Bicycle("basic", 50,500)

bikeshop1 = Bikeshop("Chinatown Bike",0.2)

bikeshop1.stockbike(mongoose,1)
bikeshop1.stockbike(tokyobike,1)
bikeshop1.stockbike(bmx,0)
bikeshop1.stockbike(fixie,1)
bikeshop1.stockbike(noodlebike,2)
bikeshop1.stockbike(basic,2)

##print the name of each customer and bikes they can afford

for customer in tina, pete, sue:
	for bike in bikeshop1.inventory:
		if (bike.cost*(1+bikeshop1.margin)) <= customer.money:
			customer.options.append((bike, bike.model, bike.cost*(1+bikeshop1.margin)))
		else:
			pass

	print ("\n{} can afford:".format(customer.name))
	for f in customer.options:
		print(f[1],f[2])

#just checking the inventory
print ("\n\nInventory of the {} shop".format(bikeshop1.name))
for bike in bikeshop1.inventory:
	print (bike.model, ": ", bikeshop1.inventory[bike])

# now we're going to sell a bike
# later i'm going to add something that checks the inventory first
print ("\n")

for customer in tina, pete, sue:
	choice = random.choice(customer.options)
	while bikeshop1.sellbike(choice[0]) == False:
		choice = random.choice(customer.options)
		# I realise I could end up in an infinite loop here if there are no bikes that meet criteria - will fix later
	customer.buybike(choice[1], choice[2])
	print ("{} bought a {}, costing ${}, and has ${} left".format(customer.name, customer.bikesOwned[0], choice[2], customer.money))

#check inventory again

print ("\n\nUpdated inventory of the {} shop".format(bikeshop1.name))
for bike in bikeshop1.inventory:
	print (bike.model, ": ", bikeshop1.inventory[bike])

bikeshop1.profit()



