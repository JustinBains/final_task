from calculus import get_calculus_function
from linear_algebra import get_linear_algebra
from data_management import get_data_management

"""
@author: Justin Bains
Date: December 18th 2018
Description: Can graph 2D/3D vectors, Estimates Integral values, and Derivative Values, Finds averages, and linear regression
"""


def instruction():
    print("What mathematically command would you like to do")
    print("1: Calculus")
    print("2: Vectors/Linear Algebra")
    print("3: Data Management")
    choice = input()

    if choice == "1":
        get_calculus_function()
    elif choice == "2":
        get_linear_algebra()
    elif choice == "3":
        get_data_management()
    else:
        print("That is not valid")
        instruction()


if __name__ == '__main__':
    instruction()
