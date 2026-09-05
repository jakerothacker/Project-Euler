# Triangle number = 1/2 *n(n+1)
from pathlib import Path

class TriangleWords():

    def __init__(self):
        self.file = Path.cwd() /"problems_41-50"/ "problem_042" / "0042_words.txt"
        self.triangle_numbers = [1]
        self.count = 0


    def  get_data(self):
        contents = self.file.read_text()
        self.data = contents.split(",")
        
    def letter_to_sum(self):
        for i in range(len(self.data)):
            self.data[i] = self.data[i].replace('"','')
            total = 0
            for j in range(len(self.data[i])):
                letter = self.data[i][j]
                total += ord(letter.upper()) - 64
            self.data[i] = total

    def check_triangle_numbers(self):
        
        for i in range(len(self.data)):
            if self.data[i] > self.triangle_numbers[-1]:
                self.find_triangle_number_upto(self.data[i])

            if self.data[i] in self.triangle_numbers:
                self.count+=1
            


    def find_triangle_number_upto(self,n):
        while self.triangle_numbers[-1] < n:
            x =len(self.triangle_numbers)+1
            self.triangle_numbers.append(x*(x+1)//2)


        



test = TriangleWords()
test.get_data()
test.letter_to_sum()
test.check_triangle_numbers()
print(test.count)