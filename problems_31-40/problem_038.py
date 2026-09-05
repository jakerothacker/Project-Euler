# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2,...n) where n>1 ?


num=9
nums = [1,2,3,4,5,6,7,8,9]
max = 0
while num <10000:
    n=2
    while n<=9:
        test_list =[]
        digit_total = 0 
        for i in range(n):
            test_list.append(nums[i]*num)
            digit_total += len(str(nums[i]*num))

        if digit_total ==9:
            test_nums = []
            test = True
            for j in range(len(test_list)):
                for k in range(len(str(test_list[j]))):
                    test_nums.append(int(str(test_list[j])[k]))

            for i in range(len(test_nums)):
                if nums[i] not in test_nums:
                    test = False

            if test == True:
                result = ""
                for i in range(len(test_list)):
                    result += str(test_list[i])
                if int(result)>max:
                    max = int(result)
        n+=1
    num+=1
print(max)
                