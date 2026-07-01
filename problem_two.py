#sum of all even Fibonacci numbers below 4 million
def sum_of_even_fibonacci_below_n(n):
    """summs even fibonacci numbers up to n-1

    Args:
        n (int): The upper limit (exclusive) for the Fibonacci numbers to consider

    Returns:
        int: The sum of all even Fibonacci numbers below n
    """
    sum = 0 
    count = 1
    last_count = 0
    while count < n:
        if count % 2 == 0:
            sum += count
        temp = last_count
        last_count = count
        count += temp
    return (print(sum))
sum_of_even_fibonacci_below_n(4000000)