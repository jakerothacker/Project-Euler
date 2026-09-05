# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.


def main(upper_limit):
    group = []
    count = 1
    while count<=upper_limit:
        if is_palindrome(count):
            binary = base_10_to_base_2(count)
            if is_palindrome(binary):
                group.append(count)
        count+=1
    return(group)


def base_10_to_base_2(n):
    num = ""
    if n == 0:
        return 0
    while n!=0:
        num = str(n%2) + num
        n = n//2
    return int(num)
    
def is_palindrome(n):
    """
    This function checks if a given number is a palindrome.

    Parameters:
    n (int): The number to check.

    Returns:
    bool: True if the number is a palindrome, False otherwise.
    """
    return str(n) == str(n)[::-1]

group = main(1000000)
total = 0
for i in range(len(group)):
    total += group[i]
print (total)
