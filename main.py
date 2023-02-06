# Author: Aubrey Floyd
# GitHub username: aubreyfloyd2
# Date: 2/6/2023
# Description: Recursive function that takes two positive integers as parameters and returns
#              the product of those two numbers

def multiply(x, y):
    """Returns the product of two positive integers"""
    if y == 1:
        return x
    return x + multiply(x, y - 1)

# print(multiply(7, 4))