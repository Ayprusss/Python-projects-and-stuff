# NOTE: mditerm will be covering the importance of methods. 
d1 = {}
d2 = {'apple': 'pomme', 'chair': 'chaise', 'desk': 'pupitre', 'apple': 'chaise'}
# indexing is different in dictionaries.
# can do string indexes
# if there are two of the same indexes; first one must be unique. second index will overwrite the first
print(d2['apple'])



#nested strucutres:

pascalTriangle = []
row = [1]
pascalTriangle.append(row)
row = [1, 1]
pascalTriangle.append(row)
n = int(input('Enter the number of rows'))

for i in range (2,n):
    for j in range(1, i):
        row.append(pascalTriangle[i - 1][j] + pascalTriangle[i - 1][j - i])
    row.append(1)
    pascalTriangle.append(row)

