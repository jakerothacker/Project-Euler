#sum of all multiples of 3 and 5 below 1000

def sum_of_multiples_of_3_and_5_below_n(n):
    sum = 0
    count = 0
    for i in range(n):
        if count % 3 == 0:
            sum += count
        elif count % 5 == 0:
            sum += count
        count += 1
    return (sum)

print(sum_of_multiples_of_3_and_5_below_n(1000))
