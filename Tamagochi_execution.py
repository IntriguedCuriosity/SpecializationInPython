import Tamagochi
import random
#import sys
#sys.setExecutionLimit(60000)

def whichone(petlist,name):
    for pet in petlist:
        if pet.name == name:
            return pet
    return None

def play():
    animals=[]
    option=""
    base_prompt = """
        Quit
        Adopt <petname_with_no_spaces_please>
        Greet <petname>
        Teach <petname> <word>
        Feed <petname>

        Choice: """
    
    feedback =""
    while True:
        action=input(feedback + "\n" + base_prompt)
        feedback=""
        words=action.split()
        if len(words) > 0:
            command= words[0]
            
        else:
            command = None
        
        if command == "Quit":
            print("Exiting")
            return 
        elif command == "Adopt" and len(words) == 2:
            if whichone(animals, words[1]):
                feedback += "you already have that name in list"
                
            else:
                animals.append(Pet(words[1]))
            
        elif command =="Greet" and len(words) == 2:
            pet=whichone(animals, words[1])
            if not pet:
                feedback += "I didn't recognize that name, please try again"
                print()
            else:
                pet.hi()
                
        elif command =="Teach" and len(words) == 3:
            pet=whichone(animals, words[1])
            if not pet:
                feedback += "I didn't recognize that name, please try again"
                print()
            else:
                pet.teach(words[2])
            
        elif command == "Feed" and len(words) ==2:
            pet  = whichone(animals, words[1])
            if not pet:
                feedback += "I didn't recognize that name, please try again"
            
            else:
                pet.feed()

        else:
                feedback += "I didn't recognize that name, please try again"
        
        for pet in animals:
            pet.clock_tick()
            feedback += "\n" + pet.__str__()

play()