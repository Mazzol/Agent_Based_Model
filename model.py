"""Agent Based Model

This model provides the building block for an interactive agent environment.
The agents have been built to interact with each other - eating, storing, sharing and moving around
The generated animation illustrates this interaction

Code was developed through practicals delivered by Andrew Evans of LIDA, in fulfilment of
GEOG5995: Programming for Social Scientist: Core Skills

References:
http://www.geog.leeds.ac.uk/courses/computing/study/core-python-phd/
"""
#MODEL-------------------------------------------------------------------------------------------------------------------------------

#Required Python Packages
import random
import matplotlib.pyplot
import matplotlib.animation
import agentframework
import csv


#Parametise the model
num_of_agents = 10                 #controls how many agents we have
num_of_iterations = 100            #changes agent cordinates an arbitrary number of times
neighbourhood = 5                  #guides who agents share resources with
agents = []                        #create an empty list
carry_on = True                    #used in stopping the agent movement
environment = []                    #create an empty list to read file in

              
#Filling the list to form the enviroment using data from a in.txt file              
f = open('in.txt', newline='')      #read the text a line at a time
dataset = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC) #convert to numbers

for row in dataset:				     #reading in the rows a row at a time
    rowlist = []                    
    for value in row:
        rowlist.append(value) 
    environment.append(rowlist)
    
f.close()                           #always close the worksheet 
               
#Make agents
for i in range(num_of_agents):  #create a set of agents
    agents.append(agentframework.Agent(environment, agents))
  

#Move, eat and share points with neighbours
#the agent movement is random
for j in range(num_of_iterations):    
    random.shuffle(agents)        #shuffles each agent list at each iteration
    for item in range(num_of_agents):
        agents[item].move()
        agents[item].eat()
        agents[item].share_with_neighbours(neighbourhood)

        
#What is the total amount stored by an agent?
stored = 0
for agent in agents:
    stored += agent.store
    
#writing to a file total stored at each iteration
f2 = open('sum_of_stored.csv', 'a', newline='')
f2.write(str(stored) + "\n")
f2.close()
    

#Plot graph of initial positions of each agent
matplotlib.pyplot.xlim(0, len(environment[0]))
matplotlib.pyplot.ylim(0, len(environment))
matplotlib.pyplot.imshow(environment)
for agent in range(num_of_agents): 
        matplotlib.pyplot.scatter(agents[agent].x,agents[agent].y)  
matplotlib.pyplot.show()


#Write the changed enviroment to a file
f3 = open('env.csv', 'w', newline='') 
writer = csv.writer(f3, delimiter=' ')
for row in environment:		
    writer.writerow(row)		
f3.close


#Show Animation of agents eating and moving
#includes a stopping condition to prevent animation from working in an infinte loop
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

#stopping condition is triggeres by class update
def update(frame_work):
    fig.clear()    
    global carry_on
    
    for item in range(num_of_agents):
        agents[item].move()
    
    if random.random() < 0.1: #this condition decides when the agents stop working
        carry_on = False
        print("stopping condition")

    for item in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[item].x,agents[item].y)       
    matplotlib.pyplot.imshow(environment)
    
def gen_function(b = [0]): #determines number of iteration shown
    a = 0
    global carry_on 
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1


animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
fig.show()

#To transform animation into a video, use next line of code 
#animation.save('ABM_animation.mp4', fps=30)
#So as to play independent of the code 
#this works without error when the code is left to run in an infinite loop i.e. without the stopping condition

#End----------------------------------------------------------------------------------------------------------------------------

