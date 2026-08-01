#Pythagorian triplet when a+b+c = 1000
import math


def is_right_triangle(a,b,c):
    """
    checks if three sides makes a right triangle

    Args:
        a (int): 0<a<=b
        b (int): a<=b<c
        c (int): b<c<inf
    """
    small_sides = a**2 + b**2
    if small_sides == c**2:
        return True
    else:
        return False
def check_pythagorian_triplet(n):
    """Finds a pythogorian triplet where a+b+c=n if it exists

    Args:
        n (int): ideally a large number

    Returns:
        prints out a,b,c if it can find them
    """
    c_start= math.ceil(n/2)
    b_start= n//2 -1
    a_start=1

    a=a_start
    b=b_start
    c=c_start

    while a_start<b_start:
        a=a_start
        b=b_start
        c=c_start
        while a<=b:
            if a+b+c!=1000:
                return print("something went wrong")
            if is_right_triangle(a,b,c):
                return print(f"{a}, {b}, {c}")
            
                
            else:
                a += 1
                b -= 1
        a_start += 1
        c_start -= 1

    return print("none found")

if __name__ == "__main__":
    check_pythagorian_triplet(1000) 