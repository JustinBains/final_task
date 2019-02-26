from math import *


def get_data_management():
    print("What would you like to do?")
    print("1: Input data points")
    print("2: Manipulate data points")

    choice = int(input())

    if choice == 1:
        write()
    elif choice == 2:
        Functions()
    else:
        get_data_management()


def write():
    with open("data_x.txt", "a+") as fx:
        with open("data_y.txt", "a+") as fy:
            amount = int(input("How many sets of data will you be using \n"))

            for i in range(amount):
                data = input("please input an x and y coordinate separated using a space i.e. '3 9'. \n")
                test = data.split(" ")
                try:
                    if int(test[0]) and int(test[1]):
                        fy.write(" ")
                        fx.write(" ")

                        to_write_x = test[0]
                        fx.write(to_write_x)  # writes x data to a separate text document

                        to_write_y = test[1]
                        fy.write(to_write_y)  # writes y data to a separate text document
                    else:  # if there is an unknown character entered goes through the loop 1 more time
                        i -= 1
                        print("please input another set of coordinates")
                except ValueError and IndexError:  # if there is a value error, goes through the loop 1 more time
                    i -= 1
                    print("please input another set of coordinates")
    Functions()


class Functions:
    """ initializes all the variables for data management """
    def __init__(self):
        with open("data_x.txt", "r+") as fx:
            with open("data_y.txt", "r+") as fy:
                self.separate_x = fx.read().split(" ")  # takes data from the data_x document and writes it into a list
                self.separate_y = fy.read().split(" ")  # takes data from the data_y document and writes it into a list

        # stores a sorted version of the separated list's
        self.sorted_x = sorted(self.separate_x)
        self.sorted_y = sorted(self.separate_y)
        self.length = len(self.separate_x)  # stores the length of the list's

        # initializes variables for averages
        self.sum_x = 0
        self.sum_y = 0
        self.mean_x = 0
        self.mean_y = 0
        self.median_x = 0
        self.median_y = 0
        self.mode_counter = 0
        self.mode_x = 0
        self.mode_y = 0

        # initializes variables for pearson and least square's line (line of best fit)
        self.num_data = 0
        self.x_square = 0
        self.y_square = 0
        self.xy = 0
        self.pearson = 0
        self.line_best = 0
        self.slope = 0
        self.y_int = 0

        print("What would you like to do")
        print("1: find mean median and mode")
        print("2: find line of best fit, and Pearson's correlation coefficient")
        self.choose = int(input())

        if self.choose == 1:
            self.averages()
        elif self.choose == 2:
            self.lin_reg()
        else:
            Functions()

    def averages(self):
        """ finds mean by adding all the values and dividing by the length of the list"""
        for i in range(len(self.separate_x)):  # sums all the data
            self.sum_x += int(self.separate_x[i])
            self.sum_y += int(self.separate_y[i])
        self.mean_x = self.sum_x / len(self.separate_x)  # divides the sum by the length of the list
        self.mean_y = self.sum_y / len(self.separate_y)

        """ finds median by finding the middle-ith value"""
        if len(self.separate_x) % 2 == 0:
            self.median_x = self.sorted_x[self.length // 2 - 1]
            self.median_y = self.sorted_y[self.length // 2 - 1]
        else:  # if it is an odd index number sums both middle numbers and averages them
            self.median_x = int(self.sorted_x[self.length // 2 - 1] + self.sorted_x[self.length // 2]) / 2
            self.median_y = int(self.sorted_y[self.length // 2 - 1] + self.sorted_y[self.length // 2]) / 2

        """ finds mode """
        # searches through the list and finds the values that occur the most
        self.mode_counter = max([self.separate_x.count(a) for a in self.separate_x])
        # finds the mode of x using the value found in mode_counter
        self.mode_x = ([i for i in self.separate_x if self.separate_x.count(i) == self.mode_counter][0]
                       if self.mode_counter > 1 else None)

        # applies the same algorithm from above
        self.mode_counter = max([self.separate_y.count(a) for a in self.separate_y])
        self.mode_y = ([j for j in self.separate_y if self.separate_y.count(j) == self.mode_counter][0]
                       if self.mode_counter > 1 else None)

        print("the mean of the X and Y variables are:", self.mean_x, "and", self.mean_y)
        print("the median of the X and Y variables are:", self.median_x, "and", self.median_y)
        print("the mode of the X and Y variables are:", self.mode_x, "and", self.mode_y)

    def lin_reg(self):

        for i in range(self.length):
            # finds all the values needed to find the linear regression
            self.xy += int(self.separate_x[i]) * int(self.separate_y[i])  # sums the value of x[i] * y[i]
            self.sum_x += int(self.separate_x[i])
            self.sum_y += int(self.separate_y[i])
            self.x_square += int(self.separate_x[i]) ** 2  # finds the value of x[i] squared
            self.y_square += int(self.separate_y[i]) ** 2  # finds the value of y[i] squared

        # find the Pearson's correlation coefficient
        self.pearson = round(((self.length * self.xy) - (self.sum_x * self.sum_y)) / sqrt(((self.length * self.x_square) - self.sum_x ** 2) * ((self.length * self.y_square) - self.sum_y ** 2)), 3)

        # find the slope of the line of best fit
        self.slope = round(((self.length * self.xy - self.sum_x * self.sum_y) / (self.length * self.x_square - self.sum_x ** 2)), 3)

        # using the slope and the mean of x-values and y-values finds the y-intercept
        self.y_int = round(((self.sum_y - self.slope * self.sum_x) / self.length), 3)
        print("the equation of the linear regression is:", str(self.slope) + "x", "+", self.y_int)
        print("Pearson's correlation coefficient and the R^2 values are:", "R=" + str(self.pearson), "R^2=" + str(round(self.pearson ** 2, 3)))
