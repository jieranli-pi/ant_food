import numpy as np
import random
import matplotlib.pyplot as plt
import time

# Define the function
def my_function1(x, y):
    return x+y-10

def my_function2(x, y):
    return ((x - 2.5) / 30)**2 + ((y - 2.5) / 40)**2 - 1

def function_to_food_pts(my_function):
    food_pts = []
    for x in range(-5, 6):
        for y in range(-5, 6):
            if my_function(x*10, y*10)>=0:
                food_pts.append([x*10, y*10])
    return food_pts

scenario = input("Please enter scenario 1, or 3, 1 is 40cmx40cm box, 3 is circle")
if scenario == "1":
    food_pts = [[-20, 20], [-10, 20], [0, 20], [10, 20], [20, 20], [-20, -20], [-10, -20], [0, -20], [10, -20], [20, -20], [20, 10], [20, 0], [20, -10], [-20, 10], [-20, 0], [-20, -10]]
if scenario == "2":
    food_pts=function_to_food_pts(my_function1)
if scenario == "3":
    food_pts=function_to_food_pts(my_function2)

# Extract x and y coordinates for visualization
x_coords, y_coords = zip(*food_pts)


ant_loc = [0, 0]

# Highlight the ant location

def ant_plot(ant_loc, x_coords, y_coords, sec):
    # Plot the points
    plt.scatter(x_coords, y_coords, marker='o', color='blue', label='Food Points')
    ant_text = plt.annotate('Ant', (ant_loc[0], ant_loc[1]), textcoords="offset points", xytext=(0, 10), ha='center')
    ant_marker = plt.scatter(ant_loc[0], ant_loc[1], marker='x', color='red', label='Ant Location')
    plt.xlabel('EW')
    plt.ylabel('SN')
    plt.title('Time(s)=' + str(sec))

    # Display the plot
    plt.show()

#ant_plot(ant_loc, x_coords, y_coords,0)

seclist=[]
num_simlulation=100000

for i in range(num_simlulation):
    # Update ant location every second
    ant_loc = [0, 0]
    for sec in range(1,50000):  # Adjust the number of seconds as needed
        direction = random.choice(['north', 'south', 'east', 'west'])
    
        if direction == 'north':
            ant_loc[1] += 10
        elif direction == 'south':
            ant_loc[1] -= 10
        elif direction == 'east':
            ant_loc[0] += 10
        elif direction == 'west':
            ant_loc[0] -= 10
        
        #ant_plot(ant_loc, x_coords, y_coords, sec)
    
        # Check if the ant found food
        if ant_loc in food_pts:
            #print("Ant found food at", "second", str(sec))
            seclist.append(sec)
            break

# Close the plot window after the updates
plt.close()

print('The average time spent for the ant to find food in', num_simlulation, 'numbers of simulation is', str(np.mean(seclist)), 'seconds')