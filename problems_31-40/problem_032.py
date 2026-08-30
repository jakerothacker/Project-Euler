class NumberLexicographic:
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
    def __init__(self,num):
        self.num = num
        self.list = [int(n) for n in str(num)]
   
        self.lexicographic_permutation = [self.num]
        self.pandigitals = []
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

    def get_pandigital_products(self):
        for permutation in self.lexicographic_permutation:
            permutation_list = list(map(int, str(permutation)))
            true_products = self.check_if_all_product_true(permutation_list)
            for product in true_products:
                if product not in self.pandigitals:
                    self.pandigitals.append(product)

            
    def check_if_all_product_true(self,list):
        ture_products =[]
        for i in range(len(list)-2):
            for j in range(i+1,len(list)-1):
                first = int("".join(str(d) for d in list[:i+1]))
                second = int("".join(str(d) for d in list[i+1:j+1]))
                last = int("".join(str(d) for d in list[j+1:]))
                if first*second == last:
                    ture_products.append(last)
        return ture_products

if __name__ == "__main__":
    test = NumberLexicographic("123456789")
    test.get_lexicographic_permutations()
    test.get_pandigital_products()
    print(test.pandigitals)
    total = 0
    for num in test.pandigitals:
        total+=num
    print(total)
    