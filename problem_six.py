#sum square difference

def sum_square(n):
    """Finds the sum of the squares of the first n natural numbers"""
    sum_of_squares = 0
    for i in range(1,n+1):
        sum_of_squares += i**2
    return sum_of_squares

def square_sum(n):
    """Finds the square of the sum of the first n natural numbers"""
    square_of_sum = 0
    for i in range(1,n+1):
        square_of_sum += i
    return square_of_sum**2

def sum_square_difference(n):
    """Finds the difference between the sum of the squares and the square of the sum of the first n natural numbers
    
    Rquires:
        sum_square(n): from problem_six.py
        square_sum(n): from problem_six.py
    """
    return square_sum(n) - sum_square(n)

print(sum_square_difference(100))