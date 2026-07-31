videogames=["Minecraft","Roblox","Poppy Playtime","Garthen of Banban","Microsoft flight simulator 2024","Bendy and the ink machine","Little nightmares","Project Playtime","Meccha Chameleon","Portal","Portal 2","Undertale"]
matrix = [[1, 2, 3, 4, 5],[6, 7, 8, 9, 10],[11, 12, 13, 14, 15],[16, 17, 18, 19, 20],[21, 22, 23, 24, 25]]
print(matrix)
print(matrix[1][1])
print("Number of rows :",len(matrix))
print("Number of collum :",len(matrix[0]))
for i in range (5):
    for j in range (5):
        print(matrix[i][j],end=" ")
    print()