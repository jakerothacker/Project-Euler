#longest coatzal chain under 1 million

def coatzal_chain_count(n):
    count = 1
    num = n
    while num > 1:
        if num % 2 == 0:
            num /= 2
        else:
            num *= 3
            num += 1
        count += 1
    return count

def largest_coatzal_chain(n):
    num = n
    high_count_num = 0
    high_count = 0
    while num > 0:
        count = coatzal_chain_count(num)
        if count > high_count:
            high_count_num = num
            high_count = count
        num -= 1
    return (high_count_num)

print(largest_coatzal_chain(999999))