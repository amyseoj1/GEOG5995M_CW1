
# In this practical, we're going to build a main 'Model' program, 
# containing variables representing two agents' locations (y and x coordinates for each), 
# and we're going to start to build code to move them around.

import random 
import matplotlib
matplotlib.use('macosx')
import matplotlib.animation as manimation
import matplotlib.pyplot as plt
import time
import csv
import agentframework

# Define number of agents

num_of_agents =  input("Enter the number of agents  ")
num_of_agents = int(num_of_agents)
num_of_iterations = input("Enter the number of iterations  ")
num_of_iterations = int(num_of_iterations)

neighborhood = 20
# Create empty lists

agents=[]
environment = []
rowlist = []

# Define Fig Size
    
fig = plt.figure(figsize=(10, 10))
ax = fig.add_axes([0, 0, 1, 1])

# read dataset

with open('in.txt',newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        environment.append(row)
        for value in row: 
            rowlist.append(value)

        
# Check to see if the data is read correctly 

#plt.imshow(environment)
#plt.show()

# creates new set of coordinates using for-loop 

for i in range(num_of_agents):
    
    agents.append(agentframework.Agent(environment, agents))

#print(agents[i]._y, agents[i]._x)


carry_on = True	

# optimise the random movement using for-loop for every agents

#for j in range(num_of_iterations): # all agents move one step at a time
    #for i in range(num_of_agents):
    
        #agents[i].move()
        #agents[i].eat()
        #agents[i].share_with_neighbors(neighborhood)
        #agents[i].distance_between()
        

def update(frame_number):
    
    fig.clear()   
    global carry_on
    plt.imshow(environment)
    plt.ylim(0, 300)
    plt.xlim(0, 300)
    plt.title('Displaying Multiple Agents Moving')
    plt.xlabel('X coordinates')
    plt.ylabel('Y coordinates')
    
    random.shuffle(agents)
    
    for i in range(num_of_agents):
    
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbors(neighborhood)
        
        if agents[i].store > 100:
            carry_on = False
            print("stopping condition")   

        
    for i in range(num_of_agents):
        
        plt.scatter(agents[i]._x,agents[i]._y)   
        print(agents[i]._x,agents[i]._y)
        

# In order to have a stopping condition, create a generator function.
#  (e.g. all the sheep have at least some amount in their stomachs)
        
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1        

		

# Animation 

#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)
animation = manimation.FuncAnimation(fig, update, frames=gen_function, repeat=False)

plt.show()             

# Write out the environment as a file at the end
   
f2 = open('environmentout.csv', 'w', newline='') 
writer = csv.writer(f2, delimiter=' ')
for row in environment: 
    writer.writerow(row) # List of values.
f2.close()




