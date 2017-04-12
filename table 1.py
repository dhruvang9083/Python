for row in range(1,11):
    print(row, end=" ")
    for column in range (1,11):
        product=row*column
        if product<100:
            print(end=" ")
        if product<10:
            print(end=" ")
        print(product,end=" ")
    print()
