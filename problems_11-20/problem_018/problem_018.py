# find the highest vaule path if moving down or down-right
import copy
from pathlib import Path

def main():
    data = get_data()
#    data_copy = copy.deepcopy(data)
    # turn_bottom_zero(data)
    turn_rows_zero(data)
    print(data)
    

def get_data():
    file = Path.cwd() /"problems_11-20"/ "problem_018" / "problem_018.txt"
    data = []
    contents = file.read_text()
    lines = contents.splitlines()
    for line in lines: #puting data in a list of lists
        line = line.split()
        data.append(line)
    data = [[int(num) for num in list] for list in data]
    return data


# def turn_bottom_zero(data):
#     list = data[-1]
#     pos = 1
#     if list[0] <= list[1]:
#         list[0] = 0
#     if list[-1] <= list[-2]:
#         list[-1] = 0
#     for num in list[1:-1]:
#         if num <= list[pos-1] and num <= int(list[pos+1]):
#             list[pos] = 0
#         pos += 1


def turn_rows_zero(data):
    for i in range(len(data)-2,-1,-1):
        for pos in range(len(data[i])):
            path_max = max(data[i+1][pos],data[i+1][pos+1])
            if data[i+1][pos] < data[i+1][pos+1]:
                data[i+1][pos] = 0
            data[i][pos] += path_max
        

def check_paths(data):
    pass



if __name__ == "__main__":
    main()