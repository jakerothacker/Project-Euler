def main(n):
    numbers = []
    digits = [2]
    while len(digits)<n+2:
        numbers = check_digits(digits,numbers,n)
        digits = change_digits(digits)

    return(numbers)


def check_digits(digits,numbers,n):
    sum = 0 
    for digit in digits:
        sum += digit**n
    if int("".join(map(str, digits))) == sum:
        numbers.append(sum)
    return numbers

def change_digits(digits):
    num = int("".join(map(str, digits)))
    num +=1
    return [int(x) for x in str(num)]




if __name__ == "__main__":

    numbers = main(5)
    total = sum(numbers)
    print (total)