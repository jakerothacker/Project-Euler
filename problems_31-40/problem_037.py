# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

class Num:

    def __init__(self):
        self.truncatable_primes = []
        self.potential= [3,7]
        self.possible_addons = [1,3,5,7,9]
        self.possible_end = [2,3,5,7]
        

    def build_nums(self):
        i = 0
        while i< len(self.potential):
            for j in range(len(self.possible_addons)):
                test = int(str(self.possible_addons[j])+str(self.potential[i]))
                if check_truncatable_left(test):
                    self.potential.append(test)
            i+=1

        for i in range(len(self.potential)):
            if check_truncatable(self.potential[i]):
                self.truncatable_primes.append(self.potential[i])
            if check_truncatable(int("2"+str(self.potential[i]))):
                self.truncatable_primes.append(int("2"+str(self.potential[i])))

    

    



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

def check_truncatable(n):
    if n ==3 or n==7:
        return False
    elif check_truncatable_left(n) and check_truncatable_right(n):
        return True
    return False

def check_truncatable_left(n):
    for i in range(len(str(n))-1):
        test = int(str(n)[i:])
        if not is_prime(test):
            return False
    return True

def check_truncatable_right(n):
    for i in range(1,len(str(n))):
        test = int(str(n)[:-i])
        if not is_prime(test):
            return False
    return True

trial = Num()
trial.build_nums()
print(trial.truncatable_primes)
count =0
for i in range(len(trial.truncatable_primes)):
    count+=trial.truncatable_primes[i]
print(count)