##main script running the Bicycles project 
## created by Sam Bonning 5/30/17

##here are the scenarios accounted for (white box):
##customer can't afford bicycles
##customer can afford bicycles but there are none in stock
##didn't create any error scenarios because I am programming the inputs 

##Here's the initialization of characters script

import random
from bicycles import Customer, Bikeshop, Bicycle, Wheels, Frames

print ("You have initialized the Bike Shop program!\n")

tina = Customer("tina",200)
pete = Customer("pete",500)
sue = Customer("sue",1000)

wheel1 = Wheels("round",40,50)
wheel2 = Wheels("square",20,150)
wheel3 = Wheels("oval",30,200)

frame1 = Frames("steel",100,100)
frame2 = Frames("carbon",100,500)
frame3 = Frames("aluminum",80,50) 

mongoose = Bicycle("mongoose",wheel1,frame2)
tokyobike = Bicycle("tokyobike",wheel2,frame3)
bmx = Bicycle("bmx",wheel3,frame1)
fixie = Bicycle("fixie", wheel1,frame3)
noodlebike = Bicycle("noodlebike",wheel2,frame1)
basic = Bicycle("basic",wheel3,frame3)

for b in mongoose, tokyobike,bmx,fixie,noodlebike,basic:
	print (b.cost)

bikeshop1 = Bikeshop("Chinatown Bike",0.2)

bikeshop1.stockbike(mongoose,2)
bikeshop1.stockbike(tokyobike,2)
bikeshop1.stockbike(bmx,2)
bikeshop1.stockbike(fixie,1)
bikeshop1.stockbike(noodlebike,2)
bikeshop1.stockbike(basic,2)

##print the name of each customer and bikes they can afford

for customer in tina, pete, sue:
	for bike in bikeshop1.inventory:
		if (bike.cost*(1+bikeshop1.margin)) <= customer.money and bikeshop1.inventory[bike]>0:
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

# now we're going to sell a bike, but check the inventory first

print ("\n")

for customer in tina, pete, sue:
	try:
		choice = random.choice(customer.options)
		while bikeshop1.sellbike(choice[0]) == False:
			choice = random.choice(customer.options)
		customer.buybike(choice[1], choice[2])
		print ("{} bought a {}, costing ${}, and has ${} left".format(customer.name, customer.bikesOwned[0], choice[2], customer.money))
	except:
		print ("{} can't afford any of the bikes in stock.".format(customer.name))

print()

#check inventory again

print ("\n\nUpdated inventory of the {} shop".format(bikeshop1.name))
for bike in bikeshop1.inventory:
	print (bike.model, ": ", bikeshop1.inventory[bike])

bikeshop1.profit()



