from math import *


def get_calculus_function():
    print("The following program takes in a function in the form of (ax+b)^n or standard form i.e. ax^3 + bx^2 + cx + d"
          "and differentiates, as well as integrates it"
          "Do you want to:")
    print("1: Integrate")
    print("2: Differentiate")

    choice = input()

    print("please input the equation using python syntax")
    global equation
    equation = input()

    if choice == "1":
        Integration()
    elif choice == "2":
        Differentiation()
    else:
        print("Invalid response")
        get_calculus_function()


class Integration:
    """ Uses the 'Rectangular Integration' or the 'Midpoint Rule' to approximate area"""

    def __init__(self):
        self.N = int(input("How many rectangles under the curve would you like to take (more is more accurate) \n"))
        self.a = int(input("where would you like to start integrating (value of a) \n"))  # ends area bounds
        self.b = int(input("where would you like to stop integrating (value of b) \n"))  # starts area bounds

        self.area_of_rect = 0
        self.midpoint_of_rect = 0  # finds midpoint of rectangle

        print(self.area(), "is the area under the curve of")

    def area(self):
        for n in range(1, self.N+1):  # loops for every rectangle under the curve
            self.area_of_rect += f(self.a+((n - (1/2))*((self.b-self.a)/self.N)))
            # finds the area of N amount of rectangles of size (b-a)
            self.midpoint_of_rect = ((self.b-self.a)/self.N)*self.area_of_rect
            # finds the midpoint of the rectangle (which is the point the rectangle intersects the curve)

        return self.midpoint_of_rect  # returns approximated value of the area


class Differentiation:
    """ Takes the derivative at a value using the limit approximation of the function """

    def __init__(self):
        self.h = 0.0000000000001
        self.value = int(input("At what point would you like to find the derivative \n"))
        self.numerator = f(self.value + self.h) - f(self.value)  # uses limit approximation with a very small h value
        self.denominator = self.h
        self.slope = 0

        self.derive()

    def derive(self):
        self.slope = self.numerator/self.denominator  # Returns the slope to the third decimal
        print("the derivative of", str(equation), "at", self.value, "is approximately", float("%.3f" % self.slope))


def f(x):  # is the equation for the integral calculator
    x
    return eval(equation)  # takes the equation with the parameter and inputs it into the equation
