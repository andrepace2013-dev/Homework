c_c={'physics book':15,'Math book':10,'Science book':12}
while True:
    print("1. Insert book")
    print("2. Display all books")
    print("3. Display all price")
    print("4. Get price")
    print("5. Delete")
    print("6. show all")
    print("7. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        book=input('Enter the book name')
        price=input('Enter the book price')
        c_c[book]=price
    if choice==2:
        print(c_c.keys())
    if choice==3:
        print(c_c.values())
    if choice==4:
        cfc=input('Enter a book')
        print(c_c[cfc])
    if choice==5:
        cd=input('what book do you want to delete')
        del c_c[cd]
        print('Sucsessfully Deleted')
    if choice==6:
        print(c_c)
    if choice==7:
        break