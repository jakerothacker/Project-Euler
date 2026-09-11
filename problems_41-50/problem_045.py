# Find the second number that is triangular pentagonal and hexagonal

class TripenhexNumber:
    def __init__(self):
        self.tri_set = {1}
        self.tri_max = 1
        self.tri_count = 1

        self.pen_set = {1}
        self.pen_max = 1
        self.pen_count = 1

        self.hex_set = {1}
        self.hex_max = 1
        self.hex_count = 1

        self.all_set = {1}


    def make_nums(self,upperlimit):
        while self.tri_max < upperlimit:
            self.tri_count += 1
            new_tri = self.tri_count*(self.tri_count+1)//2
            self.tri_max = new_tri
            self.tri_set.add(new_tri)
        while self.pen_max < upperlimit:
            self.pen_count += 1
            new_pen = self.pen_count*(3*self.pen_count-1)//2
            self.pen_max = new_pen
            self.pen_set.add(new_pen)
        while self.hex_max < upperlimit:
            self.hex_count += 1
            new_hex = self.hex_count*(2*self.hex_count-1)
            self.hex_max = new_hex
            self.hex_set.add(new_hex)

    def compare_sets(self):
        for i in self.hex_set:
            if i in self.tri_set and i in self.pen_set:
                self.all_set.add(i)

        #clear set so no checking repeats
        self.tri_set.clear()
        self.tri_set.add(self.tri_max)
        self.pen_set.clear()
        self.pen_set.add(self.pen_max)
        self.hex_set.clear()
        self.hex_set.add(self.hex_max)

            

if __name__ =="__main__":
    test = TripenhexNumber()
    count = 1
    while len(test.all_set)<3:
        test.make_nums(count*5000000)
        test.compare_sets()
        count+=1

    print(test.all_set)
