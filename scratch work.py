#makes random numbers
from random import random

total_points = 10
x_axis = []
y_axis = []
for items in range(total_points):
    x = round(random(),2) #new random number
    x_axis.append(x) #adds to list x_axis
for items in range(total_points):
    y = round(random(),2) #new random number
    y_axis.append(y) #adds to list y_axis

#combined_dict = dict(zip(x_axis,y_axis)) # combines x and y into dictionary
#print(combined_dict)

#calculates pie
points_inside = 0
for x in x_axis:
    key = x*x
    for y in y_axis:
        value = y*y
        if key+value <= 0.25:
            points_inside +=1
#        if (x*x) + (y*y) <= 0.25: #number of points inside the circle
#            points_inside += 1
 #   pi = 4 * (points_inside/ total_points)

print(points_inside)