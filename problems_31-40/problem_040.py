

string = ""
count = 1
while len(string)<=1000000:
    string = string+str(count)
    count +=1

final = [string[0] ,string[9] , string[99] , string[999] , string[9999] ,string[99999] , string[999999]]
total = 1
for i in range(len(final)):
    total *= int(final[i])

print(total)