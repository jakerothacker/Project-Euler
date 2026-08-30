# number of ways to make 2 pounds with 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p)

class ChangeMaker:
    def __init__(self, coins,target):

        self.coins = coins
        self.target = target
        self.totals = {}
        for i in range(1,self.target+1):
            self.totals[i] = 0

        for coin in range(len(self.coins)):
            for value in range(1,self.target+1):
                self.totals[value] += self.ways_with_coin(value,coin)


    def ways_with_coin(self,value,coin):
        """
        only works if used by lowerst coin for all values then increase coin

        Args:
            value (int): value you want to check all lower values must be checked
            coin (int): index of deired coin in self.coins all lower coins must have been used 
        
        """
        if coin == 0:
            return 1 
        leftover = value - self.coins[coin]
        if leftover < 0:
            return 0
        elif leftover == 0:
            return 1
        else:
            return self.totals[leftover]
        

        



if __name__ == "__main__":
    values = [1,2,5,10,20,50,100,200]
    target = 200
    t = ChangeMaker(values, target)
    print(t.totals[target])
    