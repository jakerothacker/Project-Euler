# largest palindrome that is the product of two 3-digit numbers

def check_palindrome(n):
    """
    This function checks if a given number is a palindrome.

    Parameters:
    n (int): The number to check.

    Returns:
    bool: True if the number is a palindrome, False otherwise.
    """
    return str(n) == str(n)[::-1]

