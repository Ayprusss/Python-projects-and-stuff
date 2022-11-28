
# Functions defined to perform Row echelon form; determine solutions using functions.

def noSol(row):  # noSolution function
    print('no solution function', row)
    if row[0] == 0 and row[1] == 0 and row[2] == 0 and row[3] != 0:
        print('no solution = true')
        return True # row echelon form has no solution.
    else:
        print('no solution = false')
        return False # row echelon form has a unique solution or infinitely many solutions.

def infiniteSol(row): # infinitesolution function
    if row[0] == 0 and row[1] == 0 and row[2] == 0 and row[3] == 0:
        return True # row echelon form has infinite solutions
    else:
        return False # row echelon form has a unique or no exception
    
def xReady(row):
    if row[0] == 1 and row[1] == 0 and row [2] == 0 and row[3] != 0:
        return True # row echelon form has a unique solution
    else:
        return False 


def yReady(row):
    if row[0] == 0 and row[1] == 1 and row [2] == 0 and row[3] != 0:
        return True # row echelon form has a unique solution
    else:
        return False 

def zReady(row):
    if row[0] == 0 and row[1] == 0 and row [2] == 1 and row[3] != 0:
        return True # row echelon form has a unique solution
    else:
        return False 


#start of program.
row1 = []
row2 = []
row3 = []

newRow21 = []
newRow31 = []
newRow32 = []

while len(row1) != 4:
    row1 = list(map(float, input("Enter the first row's coefficients(seperated by spaces): ").split()))
    
while len(row2) != 4:
    row2 = list(map(float, input("Enter the second row's coefficients(seperated by spaces): ").split()))


while len(row3) != 4:
    row3 = list(map(float, input("Enter the third row's coefficients(seperated by spaces): ").split()))

print(row1)
print(row2)
print(row3)

#quick check to see if there is inifinite many solutions or no solution:
if noSol(row1) or noSol(row2) or noSol(row3):
    print('There is no solution!')
    quit()

if infiniteSol(row1) or infiniteSol(row2) or infiniteSol(row3):
    print('There are an infinite number of solutions!')
    quit()

# program to begin process of determining a unique solution:

# finding similarities between x-coefficients:
#row1 is kept the same 
#row 2 and row 1
if (row1[0] > 0 and row2[0] > 0) or (row1[0] < 0 and row2[0] < 0):
    newRow21.append(row1[0] * row2[0] - row2[0] * row1[0]) # x = 0
    newRow21.append(row1[1] * row2[0] - row2[1] * row1[0])
    newRow21.append(row1[2] * row2[0] - row2[2] * row1[0])
    newRow21.append(row1[3] * row2[0] - row2[3] * row1[0])
elif (row1[0] > 0 and row2[0] < 0) or (row1[0] < 0 and row2[0] > 0):
    newRow21.append(row1[0] * row2[0] + row2[0] * row1[0]) # x = 0
    newRow21.append(row1[1] * row2[0] + row2[1] * row1[0])
    newRow21.append(row1[2] * row2[0] + row2[2] * row1[0])
    newRow21.append(row1[3] * row2[0] + row2[3] * row1[0])
if noSol(newRow21):
    print('There is no solution!')
    quit()
elif infiniteSol(newRow21):
    print('There are an infinite number of solutions!')
    quit()


#row 3 and row 1:
newRow31.append(row1[0] * row3[0] - row3[0] * row1[0])
newRow31.append(row1[1] * row3[0] - row3[1] * row1[0])
newRow31.append(row1[2] * row3[0] - row3[2] * row1[0])
newRow31.append(row1[3] * row3[0] - row3[3] * row1[0])

if noSol(newRow31):
    print('There is no solution!')
    quit()
elif infiniteSol(newRow31):
    print('There are an infinite number of solutions!')
    quit()
#row 3 and row 2:

newRow32.append(newRow21[0]*newRow31[1] - newRow31[0]*newRow21[1])
newRow32.append(newRow21[1]*newRow31[1] - newRow31[1]*newRow21[1])
newRow32.append(newRow21[2]*newRow31[1] - newRow31[2]*newRow21[1])
newRow32.append(newRow21[3]*newRow31[1] - newRow31[3]*newRow21[1])

if noSol(newRow32):
    print('There is no solution!')
    quit()
elif infiniteSol(newRow32):
    print('There are an infinite number of solutions!')
    quit()

z = newRow32[3] / newRow32[2]
y = (newRow21[3] - newRow21[2] * z) / newRow21[1]
x = (row1[3] - row1[2] * z - row1[1] * y) / row1[0]

print('X = ', round(x, 2))
print('Y = ', round(y, 2))
print('Z = ', round(z, 2))
    



    
