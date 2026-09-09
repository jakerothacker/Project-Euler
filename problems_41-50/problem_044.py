import math
class PentagonalNumber():

    def __init__(self):
        self.pentagonal_list =[]
        self.special_pentagonal = []
        self.special_pentagonal_sum = []
        self.special_pentagonal_dif = []
        self.pentagonal_set = set()
        

    def list_pentagonal_numbers(self,n):
        
        for i in range(1,n+1):
            self.pentagonal_list.append(i*((3*i)-1)//2)


    def special_pentagonal_check(self):
        for i in range(1,len(self.pentagonal_list)):
            for j in range(i):
                trial_sum = self.pentagonal_list[i]+self.pentagonal_list[j]
                if (math.sqrt(24*trial_sum+1)+1)%6 == 0 : 
                    self.special_pentagonal_sum.append((self.pentagonal_list[i],self.pentagonal_list[j]))
                trial_dif = self.pentagonal_list[i]-self.pentagonal_list[j]
                if (math.sqrt(24*trial_dif+1)+1)%6 == 0:
                    self.special_pentagonal_dif.append((self.pentagonal_list[i],self.pentagonal_list[j]))

    def run_special_pent(self):
        
        for i in range(len(self.special_pentagonal_dif)):
            if self.special_pentagonal_dif[i] in self.special_pentagonal_sum:
                self.special_pentagonal.append(self.special_pentagonal_dif[i])


    def set_pentagonal_numbers(self,n):

        for i in range(1,n+1):
            self.pentagonal_set.add(i*((3*i)-1)//2)
        self.pentagonal_list = list(self.pentagonal_set)

    def special_pentagonal_check_set(self):
        for i in self.pentagonal_set:
            for j in self.pentagonal_set:
                trial_dif = abs(i-j)
                if trial_dif in self.pentagonal_set:
                    trial_sum = i+j
                    if trial_sum in self.pentagonal_set or (math.sqrt(24*trial_sum+1)+1)%6 == 0 : 
                        self.special_pentagonal.append((i,j))
                    

if __name__ == "__main__":
    test = PentagonalNumber()

    # test.list_pentagonal_numbers(3000)
    # test.special_pentagonal_check()
    # test.run_special_pent()

    test.set_pentagonal_numbers(3000)
    test.special_pentagonal_check_set()

    print(test.special_pentagonal)
    print(abs(test.special_pentagonal[0][0]-test.special_pentagonal[0][1]))
    