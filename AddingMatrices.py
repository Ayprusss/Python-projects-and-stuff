mat1 = []

n = int(input('Enter the number of rows of the first matrix: '))
m = int(input('Enter the number of columns of the second matrix: '))

for i in range(0, n):
    row = []
    for j in range(0, m):
        print('Enter element at [', i + 1, ',', j + 1, ']', end = '= ')
        x = int(input(''))
        row.append(x)
    
    mat1.append(row)

mat2 = []

#n = int(input('Enter the number of rows of the second matrix: '))
#m = int(input('Enter the number of columns of the second matrix: '))

for i in range(0, n):
    row = []
    for j in range(0, m):
        print('Enter element at [', i + 1, ',', j + 1, ']', end = '= ')
        x = int(input(''))
        row.append(x)
    mat2.append(row)

    
#print(mat1)

#for i in range(0, n):
#    print(mat1[i])

print('The first matrix')
for i in range(0, n):
    for j in range(0, m):
        print(mat1[i][j], end = ' ')
    print('')

print('The second matrix')
for i in range(0, n):
    for j in range(0, m):
        print(mat2[i][j], end = ' ')
    print('')

sumMat = mat1
for i in range(0, n):
    for j in range(0, m):
        sumMat[i][j] = sumMat[i][j] + mat2[i][j]

print('The sum matrix')
for i in range(0, n):
    for j in range(0, m):
        print(sumMat[i][j], end = ' ')
    print('')

    

