#largest product of n consecutive digits in a string of numbers
from pathlib import Path

def largest_product_from_string(num_string:str, n:int):
    if n <= 0:
        return 0
    if n > len(num_string):
        return 0
    
    num_list = [int(digit) for digit in num_string]
    if n == len(num_list):
        product = 1
        for digit in num_list:
            product *= digit
        return product
    if n == 1:
        return max(num_list)
    
    max_product = 0 
    for i in range(len(num_list) - n + 1):
        product = 1
        for j in range(n):
            product *= num_list[i + j]
        if product > max_product:
            max_product = product
    return max_product

file = Path.cwd() / "problem_eight" / "1000_digits.txt"

num = file.read_text()
num = num.rstrip()

print(largest_product_from_string(num, 13))
