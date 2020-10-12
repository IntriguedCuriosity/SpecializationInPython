import random
class Pet:
    
    threshold_hunger=5
    threshold_boredom=10
    sounds=['Mrrp']
    boredom_decrement=3
    hunger_decrement=1
    
    def __init__(self,name='Kitty'):
        self.name= name
        self.hunger=random.randrange(self.threshold_hunger)
        print('hunger state is ',self.hunger)
        self.boredom=random.randrange(self.threshold_boredom)
        print('boredom state is ',self.boredom)
        self.sounds=self.sounds[:]
        print('sounds value is', self.sounds)
        
    def clock_tick(self):
        self.boredom += 1
        print('current boredom is',self.boredom)
        self.hunger += 1
        print('current hunger is',self.hunger)
        
    def reduce_boredom(self):
        self.boredom = max(0,self.boredom - self.boredom_decrement)
        print('reduce_boredom function returned ',self.boredom)
        #         if self.boredom - boredom_decrement > 0:
#             self.boredom = self.boredom - self.boredom_decrement
    
    def reduce_hunger(self):
        self.hunger = max(0, self.hunger - self.hunger_decrement)
        print('reduce_boredom function returned ',self.boredom)
    
    def teach(self,word):
        self.sounds.append(word)
        self.reduce_boredom()
        
    def hi(self):
        print(self.sounds[random.randrange(len(self.sounds))])
        self.reduce_boredom()
        
    
    def feed(self):
        self.reduce_hunger()
        
    def mood(self):
        if self.hunger <= self.threshold_hunger and self.boredom <= self.threshold_boredom:
            return "Happy"
        elif self.hunger > self.threshold_hunger:
            return "Hungry"
        else:
            return "Bored"
        
    
    def __str__(self):
        return "i am {} and i am currently {}".format(self.name, self.mood())
