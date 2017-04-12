def prime(n):
    if n==1:
        print("1 number is special")
        return 0
    for x in range(2,n):
        if n % x == 0:
            print(n,"this number is not prime")
            break
        else:
            print(n,"this number is prime")
            return 0
        
for n in range(1,20):
    prime(n)
