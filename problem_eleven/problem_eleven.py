#largest product of 4 surrounding numbers
from pathlib import Path

file = Path.cwd() / "problem_eleven" / "problem_eleven.txt"
data=[]

contents = file.read_text()
lines = contents.splitlines()
row = 1
for line in lines: #puting data in a dictionary with numbered rows.
    line = line.split()
    for num in line:
        num = int(num)

    data.append(line)
    row += 1

n = 4

max_product = 0
 
final_row = len(data)
final_column = len(data[0])
column = 0
while column < final_column - n:  #down right diagonal
    row = 0
    while row < final_row - n:
        
        product = 1
        for i in range(n):
                val = int(data[row+i][column+i])
                product *= val
        if product > max_product:
             max_product = product
        row += 1
    column += 1 

#up right diagonal
column = 0
while column < final_column - n:  #down right diagonal
    row = final_row - 1
    while row >= n:
        
        product = 1
        for i in range(n):
                val = int(data[row-i][column+i])
                product *= val
        if product > max_product:
             max_product = product
        row -= 1
    column += 1 

#right
column = 0
while column < final_column - n:
    row = 0
    while row < final_row:
          
        product = 1
        for i in range(n):
                val = int(data[row][column+i])
                product *= val
        if product > max_product:
             max_product = product
        row += 1
    column += 1 

#down
column = 0
while column < final_column:
    row = 0
    while row < final_row - n:
          
        product = 1
        for i in range(n):
                val = int(data[row+i][column])
                product *= val
        if product > max_product:
             max_product = product
        row += 1
    column += 1 

print(max_product)