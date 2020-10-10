#remember dictionary did  not output the values in sequence before 3.7
#you might see random order with big dictionaries 
#but it will print all key-item pairs

#post 3.7 it will always come in sequence and from 3.8 you can even
#reverse a dictionary

zoo = {"lion":12, "tiger":6, "elephant":23}

for anim in zoo: #Dictionary variable is considered same as
                # dictionary.keys()  method
    print(anim)
    print("there are " + str(zoo[anim]) + " " + anim + " in the zoo")
    
    
for anim in zoo.keys(): # this method does not take any parameter 
    print(anim)
    print("there are " + str(zoo[anim]) + " " + anim + " in the zoo")

    
#in above program zoo is the dictionary
# zoo.keys is the method object
#zoo.keys() is the way we will invoke the method.
#always remember () invokes the method

zoo_list= zoo.keys()
print(zoo_list)