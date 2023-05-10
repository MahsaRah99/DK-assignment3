#!/usr/bin/python3
#HW3_Q2_lbyf vs eafp
"""
Using EAFP style for avoiding errors during
division of two numbers.
"""
from math import inf

def numbers_division(num1: float | str, num2: float | str) -> float:
    """
    calculates division of two numbers.
    
    Args:
        num1 , num2 : float or string

    Returns:
        float: division of input numbers
    """
    
    try:
        return float(num1)/float(num2)
    
    except ZeroDivisionError:
        return inf
    
    except ValueError:
        return "you should enter numbers!"
    
    
    
def main():
    try:
        print(numbers_division(12.56,'3.14'))
    except NameError:
        print("undefined variable")
    except TypeError:
        print("you should enter 2 numbers!")
        
    
if __name__ == "__main__":
    main()
    