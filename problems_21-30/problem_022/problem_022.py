#Turn each letter in the name to a number then sum the name, then mulipty by the place in the list, then sum the list. 
from pathlib import Path


def main():
    file = Path.cwd() /"problems_21-30"/ "problem_022" / "problem_022.txt"

    with open(file) as file:
        list = file.read().replace('"',"").split(",")
    list.sort()

    tot = 0
    count = 0
    for name in list:
        count += 1
        name_tot = 0
        for char in name:
            char_num = alpha_num(char)
            name_tot += char_num
        tot += (name_tot*count)

    return(tot)

def alpha_num(char):
    if char == "A" or char == "a":
        return 1
    elif char == "B" or char == "b":
        return 2
    elif char == "C" or char == "c":
        return 3
    elif char == "D" or char == "d":
        return 4
    elif char == "E" or char == "e":
        return 5
    elif char == "F" or char == "f":
        return 6
    elif char == "G" or char == "g":
        return 7
    elif char == "H" or char == "h":
        return 8
    elif char == "I" or char == "i":
        return 9
    elif char == "J" or char == "j":
        return 10
    elif char == "K" or char == "k":
        return 11
    elif char == "L" or char == "l":
        return 12
    elif char == "M" or char == "m":
        return 13
    elif char == "N" or char == "n":
        return 14
    elif char == "O" or char == "o":
        return 15
    elif char == "P" or char == "p":
        return 16
    elif char == "Q" or char == "q":
        return 17
    elif char == "R" or char == "r":
        return 18
    elif char == "S" or char == "s":
        return 19
    elif char == "T" or char == "t":
        return 20
    elif char == "U" or char == "u":
        return 21
    elif char == "V" or char == "v":
        return 22
    elif char == "W" or char == "w":
        return 23
    elif char == "X" or char == "x":
        return 24
    elif char == "Y" or char == "y":
        return 25
    elif char == "Z" or char == "z":
        return 26
    
    


if __name__ == "__main__":
    print(main())