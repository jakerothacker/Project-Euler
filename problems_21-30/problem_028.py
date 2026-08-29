
def main(n):
    locations = make_spiral(n)
    sum_of_products =  eval_diagonals(n,locations)
    # print_grid(n,locations)
    return sum_of_products

def make_spiral(n):
    start_x = int((n-1)/2)
    start_y = int((n-1)/2)
    locations = {}
    growth_factor = 1
    direction = 1
    x = start_x
    y = start_y
    count = 1
    locations[(x,y)]= count
    while True:
        for i in range(growth_factor):
            x+=1*direction
            count+=1
            locations[(x,y)]= count
            if count >= n**2:
                return locations
        for i in range(growth_factor):
            y+=1*direction
            count+=1
            locations[(x,y)]= count
            if count >= n**2:
                return locations
        growth_factor+=1
        direction *= -1


def eval_diagonals(n,locations):
    left_diagonal_sum = 0
    right_diagonal_sum = 0
    for i in range(n):
        left_diagonal_sum += locations[(i,i)]
        right_diagonal_sum +=locations[(i,n-1-i)]
    return(left_diagonal_sum+right_diagonal_sum-1)

def print_grid(n,locations):
    for y in range(n):
        for x in range(n):
            print(locations[(x,y)], end=" ")
        print(" ")

if __name__ == "__main__":
    print(main(1001))
    
    