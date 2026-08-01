#first 10 digits of the sum of these numbers
from pathlib import Path

file = Path.cwd() /"problems_11-20"/ "problem_013" / "problem_013.txt"

contents = file.read_text()
lines = contents.splitlines()
sum = 0
for line in lines: 
    sum += int(line)

sum = list(str(sum))

print(sum[0:10])
