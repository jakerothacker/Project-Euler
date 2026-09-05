# For which value of perimeter, p <= 1000 is the number of integer right triangles maximised?

def main(upper_limit):
    num = 10
    max = 0
    max_perimeter=0
    while num < upper_limit:
        count,perimeter = count_right_triangles(num) , num
        if count>max:
            max = count
            max_perimeter = perimeter
        num+=1
    return max, max_perimeter

def count_right_triangles(perimeter):
    count = 0
    middle = 2
    while middle <=perimeter//2:
        smallest = 1
        while smallest < middle and perimeter-middle-smallest>middle:
            if check_right_triangle(smallest,middle,perimeter-middle-smallest):
                count+=1
            smallest+=1
        middle+=1
    return count
            

def check_right_triangle(a,b,c):
    if not(c>b and c>a):
        raise ValueError("c must be greater than a and b")
    if c**2 == ((a**2) + (b**2)):
        return True
    return False

print(main(1000))