#problem sum of first n square numbers that are odd

def sum_of_odd_first_n_square_numbers(n):
    """
    This function calculates the sum of the odd first n square numbers.

    Parameters:
    n (int): The number of square numbers to consider.

    Returns:
    int: The sum of the odd first n square numbers.
    """
    sum = 0
    count = 1
    for i in range(n):
        square = count ** 2
        if square % 2 != 0:
            sum += square   
        count += 1
    return print(sum) 

sum_of_odd_first_n_square_numbers(829000)
