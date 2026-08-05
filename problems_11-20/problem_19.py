
class Date:

    def __init__(self,day,day_of_month,month,year):
        self.day = day # 1 is sunday, 2 is monday ... 
        self.day_of_month = day_of_month
        self.month = month
        self.year = year
        self.sunday_the_first_count = 0

    def fast_forward_to(self,day_of_month,month,year):
        if year < self.year:
            return print("Can't go back in time")
        elif year == self.year and month < self.month:
            return print("Can't go back in time")
        elif year == self.year and month == self.month and day_of_month <= self.day:
            return print("Can't go back in time")
        while [day_of_month,month,year] != [self.day_of_month,self.month,self.year]:
            self.new_day()
        
    def _check_year(self):
        if self.month == 12 and self.day_of_month == 31:
            self.year += 1
            self.month = 1
            self.day_of_month = 0

    def _check_month(self):
        if self.month in (1,3,5,7,8,10) and self.day_of_month == 31:
            self._next_month()
        elif self.month in (4,6,9,11) and self.day_of_month == 30:
            self._next_month()
        elif self.month == 2 and self.day_of_month == 28:
            if self.year%4!=0 or (self.year%100==0 and self.year%400!=0):
                self._next_month()
        elif self.month == 2 and self.day_of_month == 29:
            self._next_month()

    def _change_day(self):
        self.day_of_month += 1
        if self.day <= 6:
            self.day +=1
        else:
            self.day = 1

    def _next_month(self):
        self.month += 1
        self.day_of_month = 0

    def new_day(self):
        self._check_year()
        self._check_month()
        self._change_day()
        self.count_sunday_the_first()

    def count_sunday_the_first(self):
        if self.day == 1 and self.day_of_month == 1:
            self.sunday_the_first_count += 1

    def print_date(self):
        print(f"{self.month}/{self.day_of_month}/{self.year}")

    def print_count(self):
        print(f"There are {self.sunday_the_first_count} Sundays at the begining of the month since the start date")

    def print_day(self):
        print(self.day)



if __name__ == "__main__":
    date = Date(3,1,1,1901)
    date.fast_forward_to(31,12,2000)
    date.print_date()
    date.print_day()
    date.print_count()