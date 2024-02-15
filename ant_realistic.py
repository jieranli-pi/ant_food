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

ant_loc = [0, 0]
scenario = input("Please enter scenario 1, 2, or 3")
if scenario == "1":
    food_pts = [[-20, 20], [-10, 20], [0, 20], [10, 20], [20, 20], [-20, -20], [-10, -20], [0, -20], [10, -20], [20, -20], [20, 10], [20, 0], [20, -10], [-20, 10], [-20, 0], [-20, -10]]
if scenario == "2":
    food_pts=function_to_food_pts(my_function1)
if scenario == "3":
    food_pts=function_to_food_pts(my_function2)

# Extract x and y coordinates for visualization
x_coords, y_coords = zip(*food_pts)


# Highlight the ant location
ant_text = plt.annotate('Ant', (ant_loc[0], ant_loc[1]), textcoords="offset points", xytext=(0, 10), ha='center')

def ant_plot(ant_loc, x_coords, y_coords, sec):
    # Plot the points
    plt.scatter(x_coords, y_coords, marker='o', color='blue', label='Food Points')
    ant_marker = plt.scatter(ant_loc[0], ant_loc[1], marker='x', color='red', label='Ant Location')
    plt.xlabel('EW')
    plt.ylabel('SN')
    plt.title('Time(s)=' + str(sec))

    # Display the plot
    plt.show()

ant_plot(ant_loc, x_coords, y_coords,0)

# Update ant location every second
for sec in range(1,50):  # Adjust the number of seconds as needed
    direction = random.choice(['north', 'south', 'east', 'west'])

    if direction == 'north':
        ant_loc[1] += 10
    elif direction == 'south':
        ant_loc[1] -= 10
    elif direction == 'east':
        ant_loc[0] += 10
    elif direction == 'west':
        ant_loc[0] -= 10
    
    ant_plot(ant_loc, x_coords, y_coords, sec)

    # Check if the ant found food
    if ant_loc in food_pts:
        print("Ant found food")
        break

    # Pause for one second
    time.sleep(1)

# Close the plot window after the updates
plt.close()
