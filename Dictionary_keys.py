zoo = {"lion":12, "tiger":6, "elephant":23}

zoo_list= zoo.keys() #here the zoo_list directly takes 

zoo_list=zoo.keys() #this will call dist_key object
#the dict.keys() method returns a dictionary view object, 
#which acts as a set. Iterating over the dictionary 
#directly also yields keys, so turning a dictionary into
#a list results in a list of all
#we will learn about sets in later part

print(zoo_list)

zoo_list=list(zoo.keys())
print(zoo_list)