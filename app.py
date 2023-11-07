from random import random

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/pi')
def pi():  # application's code here
#makes random numbers
    total_points = 10000
    x_axis = []
    y_axis = []
    for items in range(total_points):
        x = round(random(),5) #new random number
        y = round(random(), 5)

        x_axis.append(x) #adds to list
        y_axis.append(y)

#calculates pie
    points_inside = 0
    for x,y in zip(x_axis,y_axis):
        if (x * x) + (y * y) <= 1:  # number of points inside the circle
             points_inside += 1

    estimated_pi = 4 * (points_inside/total_points)
    return render_template("display.html", pi = estimated_pi)


if __name__ == '__main__':
    app.run()
