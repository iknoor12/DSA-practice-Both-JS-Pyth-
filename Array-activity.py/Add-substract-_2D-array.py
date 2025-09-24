#   16 July 

#  1. Given two 2D matrices, implement functions to perform addition . Ensure the matrices are of 
# compatible dimensions before processing.

matrix1 = [
    [1, 6, 3],
    [7, 9, 2]
]

matrix2 = [
    [4, 3, 2],
    [5, 8, 7]
]

result = []

for i in range(len(matrix1)):
    row = []

    for j in range(len(matrix1[0])):
        sum = matrix1[i][j] + matrix2[i][j]
        row.append(sum)
    
    result.append(row)

print("Addition:")
for row in result:
    print(row)





#  2.   Substraction 

result1 = []

for i in range(len(matrix1)):
    row = []

    for j in range(len(matrix1[0])):
        subtract = matrix1[i][j] - matrix2[i][j] 
        row.append(subtract)

    result1.append(row)

print("Substraction:")
for row in result1:
    print(row)