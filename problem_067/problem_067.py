# find the highest vaule path if moving down or down-right
import copy
from pathlib import Path

def main():
    data = get_data()
    turn_rows_zero(data)
    print(data[[0][0]])
    

def get_data():
    file = Path.cwd() /"problem_067"/ "0067_triangle.txt"
    data = []
    contents = file.read_text()
    lines = contents.splitlines()
    for line in lines: #puting data in a list of lists
        line = line.split()
        data.append(line)
    data = [[int(num) for num in list] for list in data]
    return data



def turn_rows_zero(data):
    for i in range(len(data)-2,-1,-1):
        for pos in range(len(data[i])):
            path_max = max(data[i+1][pos],data[i+1][pos+1])
            if data[i+1][pos] < data[i+1][pos+1]:
                data[i+1][pos] = 0
            data[i][pos] += path_max
    



if __name__ == "__main__":
    main()