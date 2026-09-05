


class NumberLexicographic:

    def __init__(self,num):
        self.num = num
        self.list = [int(n) for n in str(num)]
        # self.list_origional = self.list.copy()
        self.lexicographic_permutation = [self.num]
        self.prime_list = [2,3,5,7,11,13,17,19]
        # self.current_list = self.list.copy()
        self.len = len(self.list)
        self.i = 0
        self.j = 0
        self.divisible_list = []

    def get_lexicographic_permutations(self):
        while self.find_first():
            self.find_second()
            self.swap_i_j()
            self.reverse_end()
            self.store_permutation()
         
    def find_first(self):
        for i in range(1,self.len):
            if self.list[-i-1]<self.list[-i]:
                self.i = -i-1
                return True
        return False

    def find_second(self):
        for j in range(1,self.len):
            if self.list[-j]>self.list[self.i]:
                self.j = -j
                return

    def swap_i_j(self):
        self.list[self.i],self.list[self.j] = self.list[self.j],self.list[self.i]

    def reverse_end(self):
        n = -1
        while n > self.i - n:
            self.list[n],self.list[self.i - n] = self.list[self.i - n],self.list[n]
            n-=1


    def store_permutation(self):
        number = "".join(map(str, self.list))
        self.lexicographic_permutation.append(number)
        # print(number)
        

    def print_list(self):
        print(self.list)

    def print_perms(self):
        print(self.lexicographic_permutation)

    def print_perms_specific(self,n):
            print(self.lexicographic_permutation[n-1])

    def checks_sub_string_divisibility(self):
        for i in range(len(self.lexicographic_permutation)):
            truth = True
            check = str(self.lexicographic_permutation[i])
            for j in range(1,8):
                if int(check[j]+check[j+1]+check[j+2]) % self.prime_list[j-1] != 0:
                    truth = False
            if truth == True:
                self.divisible_list.append(self.lexicographic_permutation[i])



if __name__ == "__main__":
    test = NumberLexicographic("0123456789")
    test.get_lexicographic_permutations()
    test.checks_sub_string_divisibility()
    total = 0
    for i in range(len(test.divisible_list)):
        total += int(test.divisible_list[i])
    print(total)
    