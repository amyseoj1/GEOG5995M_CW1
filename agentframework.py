
import random 


class Agent:
    
#__init__ method
    
    def __init__(self, environment, agents): 
        
        self._x = random.randint(0,300)
        self._y = random.randint(0,300)
        self.environment = environment
        self.agents = agents
        self.store = 0 
    
    @property
    def x(self):
        return self._x
    
    def y(self): 
        return self._y        
    
        
# Make the move() method
    def move(self):
        if random.random() < 0.5:
            self._y = (self._y + 1) % 299
        else:
            self._y = (self._y - 1) % 299

        if random.random() < 0.5:
            self._x = (self._x + 1) % 299
        else:
            self._x = (self._x - 1) % 299
    
    
    
    def eat(self): # can you make it eat what is left?
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10
            
        # Get agents to eat the last few bits, if there's less than 10 left, without leaving negative values?
        else:
            self.store += self.environment[self.y][self.x]
            self.environment[self.y_position][self.x_position] = 0
            
    def distance_between(self, another_agent): 
        # filter out agents comparing with themselves
        for agent in self.agents:
             for agent in another_agent.agents:
                 return(((self._x-another_agent._x)**2 + (self._y-another_agent._y)**2)**0.5)
        
        
# Share resources with agents within neighborhood range

    def share_with_neighbors(self, neighborhood):
        # Loop through the agents in self.agents
        for agent in self.agents:
            # Calculate the distance between self and the current other agent:
            distance = self.distance_between(agent)
             # If distance is less than or equal to the neighbourhood
            if distance <= neighborhood:
                 # Sum self.store and agent.store
                sum = self.store + agent.store
                 # Divide sum by two to calculate average.
                ave = sum / 2
                self.store = ave
                agent.store = ave      
                #print("sharing " + str(dist) + " " + str(ave))


        
        
        