# What is the largest n-digit pandigital prime that exists?


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


def is_prime(n):
    """Checks if an int is prime

    Args:
        n (int): The number to check

    Returns:
        bool: True if the number is prime, False otherwise
    """
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

number = NumberLexicographic(1234567)
number.get_lexicographic_permutations()
high = 0
for i in range(len(number.lexicographic_permutation)):
    if is_prime(int(number.lexicographic_permutation[i])) and int(number.lexicographic_permutation[i])>high:
        high = int(number.lexicographic_permutation[i])
print(high)