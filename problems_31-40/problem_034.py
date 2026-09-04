# Find the sum of all numbers which are equal to the sum of the factorial of their digit.
import math
def find_dig_factortial():
    num = 3
    total =[]

    while num<= len(str(num))*math.factorial(9):
        str_num = str(num)
        dig_factorial = 0
        for i in range(len(str_num)):
            dig_factorial+= math.factorial(int(str_num[i]))
        if num ==dig_factorial:
            total.append(num)
        num+=1
    return(total)

print(find_dig_factortial())

