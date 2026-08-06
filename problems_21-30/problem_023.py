#sum of all ints that cannot be written as the sum of two abundant numbers
#abundant: sum of propor divisors > nummber 
#all numbers greater than 28123 can be written as sum of two abundant numbers

def main():
    sum = 0
    dict_of_nums = {}
    abundant_list = []
    for n in range(1,28124):
        dict_of_nums[n] = True
        if sum_propor_divisors(n) > n:
            abundant_list.append(n)

    for n in abundant_list.copy():
        abundant_list.pop(0)
        dict_of_nums[n*2] = None
        for n_2 in abundant_list:
            dict_of_nums[n+n_2] = None

    for key in dict_of_nums:
        if dict_of_nums[key]:
            sum += key

    return(sum)



def sum_propor_divisors(n):
    sum = 0
    try:
        n = int(n)
    except (ValueError,TypeError):
        print("only ints have propor divisors")
    else:
        if n <=1:
            return 0
        for num in range (1,n//2 +1):
            if n % num == 0:
                sum += num
    return(sum)

if __name__ == "__main__":
    print(main())