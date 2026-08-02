#sum of the digits of 2^1000


def sum_of_digits(n):
    tot = 0
    for digit in str(n):
        tot += int(digit)
    return tot

print(sum_of_digits(2**1000))
