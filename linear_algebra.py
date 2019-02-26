import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def get_linear_algebra():
    dimension = input("Do you want to plot in 1:R² (2d) or 2:R³ (3d) space \n")
    try:
        if int(dimension) == 1 or 2:
            Vectors(dimension)
        else:
            get_linear_algebra()
    except ValueError:
        get_linear_algebra()


class Vectors:
    def __init__(self, dimension):

        print("If there is no x, y, or z vector enter 0")
        self.vector_num = int(input("How many vectors are you going to input \n"))
        self.dimension = dimension
        if int(dimension) == 1:
            self.coord = np.array([[0 for x in range(4)] for y in range(self.vector_num)])
            # fills numpy.array rows with 0's (vector_num = rows) and columns with 0 (4 needed to plot each vector)

        elif int(dimension) == 2:
            self.coord = np.array([[0 for x in range(6)] for y in range(self.vector_num)])
            # fills numpy.array rows with 0's (vector_num = rows) and columns with 0 (6 needed to plot each vector)

        if int(dimension) == 1:
            """ gets the 4 variables needed to plot a single vector self.vector_num times"""
            for i in range(len(self.coord)):
                self.coord[i][0] = int(input("where does the x coordinate begin \n"))
                self.coord[i][1] = int(input("where does the y coordinate begin \n"))
                self.coord[i][2] = int(input("where does the x coordinate end \n"))
                self.coord[i][3] = int(input("where does the y coordinate end \n"))

        elif int(dimension) == 2:
            """ gets the 6 variables needed to plot a single vector self.vector_num times"""
            for i in range(len(self.coord)):
                self.coord[i][0] = int(input("where does the x coordinate begin \n"))
                self.coord[i][1] = int(input("where does the y coordinate begin \n"))
                self.coord[i][2] = int(input("where does the z coordinate begin \n"))
                self.coord[i][3] = int(input("where does the x coordinate end \n"))
                self.coord[i][4] = int(input("where does the y coordinate end \n"))
                self.coord[i][5] = int(input("where does the z coordinate end \n"))

        if int(dimension) == 1:
            self.plot_2d()
        else:
            self.plot_3d()

    def plot_2d(self):
        X, Y, U, V = zip(*self.coord)
        # zip() Makes an iterator that aggregates elements from each of the iterables
        # i.e. sets X to first self.coord[0][0], Y to self.coord[0][1] etc for all of self.coord

        plt.figure()  # figure is the type of graph called (cartesian plane)
        graph = plt.gca()  # initializes the graph

        graph.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=1)
        # quiver is vector arrows, also sets up all varaiables such as the plane, unit scale

        graph.set_xlim([0, 10])  # sets initial scope of x axis, can be changed after plt.show
        graph.set_ylim([0, 10])  # sets initial scope of y axis, can be changed after plt.show
        plt.draw()  # draws the plotted points
        plt.show()  # shows the graph

    def plot_3d(self):
        # zip() Makes an iterator that aggregates elements from each of the iterables
        # i.e. sets X to first self.coord[0][0], Y to self.coord[0][1] etc for all of self.coord
        X, Y, Z, U, V, W = zip(*self.coord)
        fig = plt.figure()  # figure is the type of graph called (cartesian plane)
        graph = fig.add_subplot(111, projection='3d')  # initializes the graph as a 3d graph with projections
        graph.quiver(X, Y, Z, U, V, W)  # sets each variable to associate with a quiver's (vector arrow's) position
        # quiver is vector arrows, also sets up all variables such as the plane, unit scale
        graph.set_xlim([0, 10])  # sets initial scope of x axis, can be changed during graph
        graph.set_ylim([0, 10])  # sets initial scope of y axis, can be changed during graph
        graph.set_zlim([0, 10])  # sets initial scope of z axis, can be changed during graph
        plt.draw()  # draws the plotted points
        plt.show()  # shows the graph
