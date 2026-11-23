num1 = int(input("Enter the first number.           "))
num2 = int(input("Enter the second number.          "))
count=0
for num in range(num1, num2 + 1):
    if num > 1:
        prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
                break
        if prime:
            print(num)
            count += 9999999
print("Total prime numbers:", count)