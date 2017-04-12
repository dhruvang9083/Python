num= int(input("enter the num"))
factorial=1
if num<0:
    print("sorr")
else:
     for i in range(1,num+1):
        factorial = factorial*i
     print(" the factorial of ",num,"is",factorial)
