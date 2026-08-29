

def main(n):
    a=2
    
    group = []
    while a<=n:
        b=2
        while b<=n:
            if a**b not in group:
                group.append(a**b)
            b+=1
        a+=1
    print (len(group))

if __name__ == "__main__":
    main(100)