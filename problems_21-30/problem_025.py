# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

def fibonacci_1000_digits():
    dig_1 = 1
    dig_2 = 1
    index = 1 
    fib_list=[1,1]
    while len(str(dig_2)) <1000:
        dig_1,dig_2 = next_fibonacci(dig_1,dig_2)
        index += 1
        fib_list.append(dig_2)

    return index



def next_fibonacci(dig_1,dig_2):
    store = dig_2
    dig_2 += dig_1
    dig_1 = store
    return dig_1,dig_2

if __name__ == "__main__":
    print(fibonacci_1000_digits())