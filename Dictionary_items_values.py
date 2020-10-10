inventory = {'mouse': 430, 'desktop': 312, 'keyboard': 525,
             'headphones': 217}

#syntax: dictionary.values()
#this will like keys here will return the values only
#as a list
print(list(inventory.values())) 

#syntax: dictionary.items()
#this will return key-value pair in the form of tuples list
print(list(inventory.items()))

for k in inventory:
    print("the quantity of ",k," in inventory is ",inventory[k])
print(type(inventory.keys()))
print(type(inventory.items()))
print(type(inventory.values()))
lit=['12']
print(type(lit))