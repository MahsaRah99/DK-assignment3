#!/usr/bin/python3
#HW3_Q3_discount code

"""
using AssertionError to check if final price
after a dicount amount is correct
"""

def apply_discount(price: int, discount:float = 0.0) -> int:
    """
    Args:
        price (int): input price
        discount (float, optional): discount amount on a price. Defaults to 0.0.

    Returns:
        int: rounded final price after discount
    """
    try:
        final_price = int(price*(1 - discount))
        assert 0 < final_price <= price, "dicount should be in range of [0,1)"
        return final_price
        
    except AssertionError as msg:
        return msg
    
def main():
    print(apply_discount(120,1.8))
#python3 -O Q3.py -> in terminal for avoiding AssertionError

if __name__ == "__main__":
    main()