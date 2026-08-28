list1forset=input("Enter a list of numbers. Somthing like this (1 2 3 4 5)         ")
list2forset=input("Enter another list of numbers. Somthing like this (1 2 3 4 5)           ")

set1 = set(map(int, list1forset.split()))
set2 = set(map(int, list2forset.split()))
while True:
    select=int(input("Select what you want to do with these numbers. \n 1: add a number from a set.         \n 2: remove a number from a set.           \n 3: Unionise the sets together.           \n 4: Intersect the sets together.          \n 5: Difference the sets together.         \n 6: Symmetric Difference the sets together.           \n 7: End program           \n Pick one by typing the corresponding number of one.         "))
    
    if select==1:
        whichsetselect1=int(input("Which list do you want to add a number too? (1 or 2)          "))
        if whichsetselect1==1:
            print(set1)
            numberselect1option1=int(input("What number do you want to add? (ONLY ONE NUMBER)          "))
            set1.add(numberselect1option1)
        elif whichsetselect1==2:
                print(set2)
                numberselect1option2=int(input("What number do you want to add? (ONLY ONE NUMBER)          "))
                set2.add(numberselect1option2)
    elif select==2:
        whichsetselect2=int(input("Which list do you want to remove a number too? (1 or 2)          "))
        if whichsetselect2==1:
            print(set1)
            numberselect2option1=int(input("What number do you want to remove? (ONLY ONE NUMBER)          "))
            set1.discard(numberselect2option1)
        elif whichsetselect2==2:
            print(set2)
            numberselect2option2=int(input("What number do you want to remove? (ONLY ONE NUMBER)          "))
            set2.discard(numberselect2option2)
    elif select==3:
        print(set1.union(set2))
        print(set1 | set2)
    elif select==4:
        print(set1.intersection(set2))
        print(set1 & set2)
    elif select==5:
        print(set1.difference(set2))
        print(set1 - set2)
        print(set2.difference(set1))
        print(set2 - set1)
    elif select==6:
        print(set1.symmetric_difference(set2))
        print(set1 ^ set2)
    elif select==7:
        break
    else:
        print("Invalide choice")