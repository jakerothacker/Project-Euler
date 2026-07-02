def is_prime(n):
    """Checks if an int is prime

    Args:
        n (int): The number to check

    Returns:
        bool: True if the number is prime, False otherwise
    """
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

