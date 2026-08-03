competition_info = ()

print("Hello and welcome to the school competition record you can win a prize by filling this, please answer the following questions seriously. (:")

for number in range(5):
    name = input("Group name: ")
    size = int(input("Size of group: "))
    date = input("Competition date: ")
    venue = input("Venue: ")
    medal = input("Medal won: ")
    record = (name, size, date, venue, medal)
    print(record)