#MODEL-------------------------------------------------------------------------

import random
import matplotlib.pyplot
import matplotlib.animation
import agentframework
import csv


#Creating the enviroment using data from a text file
environment = []                    #create an empty list 

f = open('in.txt', newline='')      #read the text a line at a time
dataset = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC) #convert to numbers

for row in dataset:				     #calling the rows a row at a time
    rowlist = []                    
    for value in row:
        rowlist.append(value) 
    environment.append(rowlist)
    
f.close()                           #always close the worksheet 

         
#Parametise the models 
num_of_agents = 10                 #controls how many agents we have
num_of_iterations = 5            #changes agent cordinates an arbitrary number of times
neighbourhood = 5                  #guides who agents share resources with

#Make agents
agents = [] #create an empty list
for i in range(num_of_agents):  #create a set of agents
    agents.append(agentframework.Agent(environment, agents))
    

#move, eat and share points with neighbours
for j in range(num_of_iterations):    
    random.shuffle(agents)        #shuffles each agent list at each iteration
    for item in range(num_of_agents):
        agents[item].move()
        agents[item].eat()
        agents[item].share_with_neighbours(neighbourhood)

#what is the total amount stored by an agent?
stored = 0
for agent in agents:
    stored += agent.store
#writing to a file
f2 = open('sum_of_stored.csv', 'a', newline='')
f2.write(str(stored) + "\n")
f2.close()
    

#plot graph of initial position of eah agent
matplotlib.pyplot.xlim(0, len(environment[0]))
matplotlib.pyplot.ylim(0, len(environment))
matplotlib.pyplot.imshow(environment)
for agent in range(num_of_agents): 
        matplotlib.pyplot.scatter(agents[agent].x,agents[agent].y)  
matplotlib.pyplot.show()

#write new enviroment
f3 = open('env.csv', 'w', newline='') 
writer = csv.writer(f3, delimiter=' ')
for row in environment:		
    writer.writerow(row)		
f3.close()


#Show Animation of agents eating and moving
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

def update(frame_work):
    fig.clear()    
    for item in range(num_of_agents):
        agents[item].move()
    for item in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[item].x,agents[item].y)       
    matplotlib.pyplot.imshow(environment)
animation = matplotlib.animation.FuncAnimation(fig, update, interval=1)
fig.show()

#transform animatiion into a video
#to play independent of the code and so attach to a webpage
animation.save('ABM_animation.mp4', fps=30)


#End---------------------------------------------------------------------

