#one millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9
#lexicographic: numerical order

class NumberLexicographic:

    def __init__(self,num):
        self.num = num
        self.list = [int(n) for n in str(num)]
        # self.list_origional = self.list.copy()
        self.lexicographic_permutation = [self.num]
        # self.current_list = self.list.copy()
        self.len = len(self.list)
        self.i = 0
        self.j = 0

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


    # def recursive_permuations(self,len_of_number):
    #     self.current_list[-len_of_number:] = self.list[-len_of_number:]
    #     if len_of_number == 2:
    #         self.last_two()
    #     else:
    #         for n in range(1,len_of_number):
    #             self.recursive_permuations(len_of_number-1)
    #             self.n_digit_revert_current(len_of_number)
    #             self.n_digit_shift(n,(-1*len_of_number)+n,-1)
    #             self.store_permutation()
    #         self.recursive_permuations(len_of_number-1)

    # def last_four(self):
    #     for n in range(1,4):
    #         self.last_three()
    #         self.n_digit_revert(4)
    #         self.n_digit_shift(n,-4+n,-1)
    #         self.store_permutation()
    #     self.last_three()

    # def last_three(self):
    #     self.last_two()

    #     self.n_digit_shift(2,-1,-1)
    #     self.store_permutation()

    #     self.last_two()

    #     self.n_digit_shift(2,-3,1)
    #     self.store_permutation()

    #     self.last_two()

    # def last_two(self):
    #     self.list[-1],self.list[-2] = self.list[-2],self.list[-1]
    #     self.store_permutation()

    # def n_digit_shift(self,n,start,direction):
    #     for num in range(n):
    #         num = direction*num + start
    #         self.list[num],self.list[num+direction] = self.list[num+direction],self.list[num]

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

    # def n_digit_revert(self,n):
    #     for pos in range(n):
    #         pos = -1*pos -1
    #         self.list[pos] = self.list_origional[pos]

    # def n_digit_revert_current(self,n):
    #     for pos in range(n):
    #         pos = -1*pos -1
    #         self.list[pos] = self.current_list[pos]
    


if __name__ == "__main__":
    test = NumberLexicographic("0123456789")
    test.get_lexicographic_permutations()
    test.print_perms_specific(1000000)
