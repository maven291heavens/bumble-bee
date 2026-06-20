matrix = [
    [1, 2, 3]
    [4, 5, 6]
    [7, 8, 9]
    ]


print matrix([0][0])
print matrix([1][2])

matrix[2][1] = 88
print(matrix)

for row in matrix:
    for col in row:
        print(col, end = " ")
    print(" ")

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of coloumns"))
matrix = []
for i in range(rows):
    row = []
    for j in range(cols): 
        val = int(input("Enter element at {}, {}: ").format(i,j))
        row.append(val)
    matrix.append(row)

print("Your 2D List: ")
for row in matrix:
    print(row)