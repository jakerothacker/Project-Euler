import math
class PentagonalNumber():

    def __init__(self):
        self.pentagonal_list =[]
        self.special_pentagonal = []
        self.special_pentagonal_sum = []
        self.special_pentagonal_dif = []
        

    def list_pentagonal_numbers(self,n):
        
        for i in range(1,n+1):
            self.pentagonal_list.append(i*((3*i)-1)//2)


    def special_pentagonal_check(self):
        for i in range(1,len(self.pentagonal_list)):
            for j in range(i):
                trial_sum = self.pentagonal_list[i]+self.pentagonal_list[j]
                trial_dif = self.pentagonal_list[i]-self.pentagonal_list[j]
                if (math.sqrt(24*trial_sum+1)+1)%6 == 0 : 
                    self.special_pentagonal_sum.append((self.pentagonal_list[i],self.pentagonal_list[j]))
                if (math.sqrt(24*trial_dif+1)+1)%6 == 0:
                    self.special_pentagonal_dif.append((self.pentagonal_list[i],self.pentagonal_list[j]))

    def run_special_pent(self):
        
        for i in range(len(self.special_pentagonal_dif)):
            if self.special_pentagonal_dif[i] in self.special_pentagonal_sum:
                self.special_pentagonal.append(self.special_pentagonal_dif[i])







if __name__ == "__main__":
    test = PentagonalNumber()
    test.list_pentagonal_numbers(3000)
    test.special_pentagonal_check()
    print(test.special_pentagonal)
    
    