#Agent Framework---------------------------------------------------------------

import random 


#Building Agent class that moves, eats, stores and shares with the environment
#all agents need to know about each other and the environment
#agents are initialised with random starting point restricted by the environment
class Agent:
    def __init__ (self, environment, agents):  
        self._x = random.randint(0,len(environment[0]))    #initialising x
        self._y = random.randint(0,len(environment))       #initialising y   
        self.environment = environment  #instance variable: the environment
        self.agents = agents            #instance variable: all agents
        self.store = 0                  #creates a new 0 store for each Agent
    
    #below is not necessary, just to protect self.x and self.y
    #for self.x
    @property
    def x(self):
        """I am the 'x' dimension."""
        return self._x    
    @x.setter
    def x(self, value):
        self._x = value    
    @x.deleter
    def x(self):
        del self._x   
    
    #for self.y
    @property
    def y(self):
        """I am the 'y' dimension."""
        return self._y    
    @y.setter
    def y(self, value):
        self._y = value    
    @y.deleter
    def y(self):
        del self._y
    #end of protection
    
    #Create a move method
    #by randomising the movement of each agent 
    #using 'Torus' to allow agents leaving at top or right 
    #to come back through down or left respectively
    def move(self):
        if random.random() < 0.5:
            self._x = (self._x + 1) % len(self.environment[0]) 
        else:
            self._x = (self._x - 1) % len(self.environment[0])
        
        if random.random() < 0.5:
            self._y = (self._y + 1) % len(self.environment)
        else:
            self._y = (self._y - 1) % len(self.environment)
            
    
    #Create an eat method    
    #eating the environment 10 at a time
    def eat(self):
        if self.environment[self._y][self._x] > 10:
           self.environment[self._y][self._x] -= 10
           self.store += 10
    
    #check the location of an Agent and total storage
    def __str__(self):
        return "This agent is located in x:" + str(self._x) + " and y:" 
        + str(self._y) + " and store is " + str(self.store)
        
   
    #Create a share_with_neighbours method
    #to enable sharing resources with close agents
    #first create a distance_between method to know how close agents are             
    def distance_between(self, agentB): 
        return (((self._x - agentB._x)**2) + ((self._y - agentB._y)**2))**0.5
       
    
    #then share resources with close neighbours
    def share_with_neighbours(self, neighbourhood):
        self.neighbourhood = neighbourhood
        for agentB in self.agents:  
            distance = self.distance_between(agentB)
            if distance <= self.neighbourhood:
                add = sum([self.store, agentB.store])
                average = (int(add)/2)  
                self.store = average          
                agentB.store = average 

#End---------------------------------------------------------------------------

    
       
      