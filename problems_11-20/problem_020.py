#sum of digits of 100!
import math
fact_100 = math.factorial(100)
total = 0
for digit in str(fact_100):
    total += int(digit)

print(total)