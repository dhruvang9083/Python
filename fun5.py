a=1
b=2
def main():
    swap()
    print("swap number is",a,b)
def swap():
    global a
    global b
    temp=a
    a=b
    b=temp
main()
