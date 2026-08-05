#sum of all amicable pairs under 10,000
#amicable pair when the sum of propor divisors of A equals B where the sum of B's propor divisors equal A
#propor divisor all number less than A that divide evenly into A

def main(upper_limit):
    number_pair = {}
    sum = 0
    for num in range(2,upper_limit):
        sum_of_propor_divisors = sum_propor_divisors(num)
        number_pair[num] = sum_of_propor_divisors
        if number_pair.get(sum_of_propor_divisors) == num and num!=sum_of_propor_divisors:
            sum += num + sum_of_propor_divisors

    return sum

        

def sum_propor_divisors(n):
    sum = 0
    try:
        n = int(n)
    except (ValueError,TypeError):
        print("only ints have propor divisors")
    else:
        if n <=1:
            raise ValueError("The lowest number with a propor divisor is 2")
        for num in range (1,n//2 +1):
            if n % num == 0:
                sum += num
    return(sum)

print(main(10000))