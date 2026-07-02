# largest palindrome that is the product of two 3-digit numbers
import math



def is_palindrome(n):
    """
    This function checks if a given number is a palindrome.

    Parameters:
    n (int): The number to check.

    Returns:
    bool: True if the number is a palindrome, False otherwise.
    """
    return str(n) == str(n)[::-1]
             

def largest_palindrome_product_2_factor(n):
    guess_1 = 10**n -1
    guess_2 = guess_1
    while True:
        if is_palindrome(guess_1 * guess_2):
            return(guess_1*guess_2)
        else:
             guess_2 -=1

print(largest_palindrome_product_2_factor(3))