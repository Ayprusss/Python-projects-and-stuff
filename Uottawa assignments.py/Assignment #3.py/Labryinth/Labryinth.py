
###################################################################################
#NAME: ANTHONY_lE_300287511
# November 23rd, 2022. 
###################################################################################

n = int(input('Enter how many rows you would like to be inputed into the game: '))

maze = []
for i in range(0, n):
    print('input row no.', i + 1, 'to be added to the maze: ')
    row = input('')
    maze.append(row)

print('your maze:')
for j in range(0, n):
    print(maze[j])

def entrance(maze, n): # starting point of the maze.
    for a in range(0,n):
        startcell = maze[a][0] # to observe all rows and where the entrance is located. Known that index 0 indicates start; 
        if startcell == 'p':
            return a

def exit(maze, n): # exit point of the maze.
    for a in range(0, n):
        endcell = maze[a][15] # to observe all rows and column where exit is located. Known that index 15 is the end of the maze based on the sample
        if endcell == 'p':
            return a
    
entrance = (entrance(maze, n), 0)
exit = (exit(maze, n), 15)

########
mypath = [] # blank matrix to determine leon's path through the maze 
for a in range(0, len(maze)):
    mypath.append([])
    for j in range(len(maze[a])): # to make similar matrix with same dimensions to original maze.
        mypath[-1].append(0)

mypath[entrance[0]][entrance[1]] = 1

# creates matrix with entrance coordinate shown at (3,0)
########

def stepInMaze(k, mypath, maze): # A EQUALS ROWS, B EQUALS COLUMNS
    for a in range(len(mypath)): # representing the rows of the path matrix
        for b in range(len(mypath[a])): # calling for length of the row itself; looking at the columns that are appointed for every row. 
            if mypath[a][b] == k:
                if a > 0 and mypath[a - 1][b] == 0 and maze[a - 1][b] == 'p': # if the value is greater than 0 row, and if value on top of path matrix is zero but is a path(p) in the actual maze; change value on top value. 
                    mypath[a - 1][b] = k + 1
                if maze[a][b - 1] == 'p' and b > 0 and mypath[a][b - 1] == 0:                     #'' same thing, but is looking on to the path value on the left of the k position; what is Leon's left. 
                    mypath[a][b - 1] = k + 1
                if a < len(mypath) - 1 and mypath[a + 1][b] == 0 and maze[a + 1][b] == 'p':       # '' same thing, but Leon is now looking for what's underneath him
                    mypath[a + 1][b] = k + 1
                if b < len(mypath[a]) - 1 and mypath[a][b + 1] == 0 and maze[a][b + 1] == 'p':    # '' Leon is then looking on his right. 
                    mypath[a][b + 1] = k + 1

k = 0
while k >= 0:
    if mypath[exit[0]][exit[1]] == 0:
        k += 1
        stepInMaze(k, mypath, maze)
    else:
        break

class Unit:  #used in ordert o identify an individual unit/cell within the mazeQ
    def __init__(self, cellvalue, row, column, printvalue):
        self.cellvalue = cellvalue
        self.row = row
        self.column = column
        self.printvalue = printvalue

    def printMazeCoordinator(self):
        print( (self.row + 1, self.column + 1) )

    def print(self):
        print(self.cellvalue, '+',  self.printvalue, '+', (self.row, self.column))
    
    def set_printvalue(self, directionString):
        self.printvalue = directionString
    
    def getRow(self):
        return self.row
    
    def getColumn(self):
        return self.column
    
def populateCell(mypath, list, r, c):# r and c are current selected path cells (row and columns of selected cell.)
    p = mypath[r][c] # value at exit point. 

    newCell = Unit(p, r, c, '*')
    list.append(newCell)
        
def traceback(mypath, exitR, exitC): # r and c are current EXIT point. (row and columns of selected cell.);  ### 
    p = mypath[r][c]                # p is the value of the exit point inside mypath. the LAST VALUE in the 
    returnPathList = []             # returnpathlist contains all cells objects of the path.
    newR = exitR
    newC = exitC
    
    while p >= 1:
        populateCell(mypath, returnPathList, newR, newC) # create cell object of push into path coordinate. 
        if newR > 0 and mypath[newR - 1][newC] == p - 1: # movement upwards..
            newR, newC= newR - 1, newC
            #print('r is ', r, 'c is', c)
        elif mypath[newR][newC - 1] == p - 1 and newC >= 0: # movement to the left. 
            newR, newC = newR, newC - 1
           # print('r is ', r, 'c is', c)
        elif mypath[newR + 1][newC] == p - 1 and newR <= len(mypath) - 1: # movement downwards.
            newR, newC = newR + 1, newC
           # print('r is ', r, 'c is', c)
        elif mypath[newR][newC + 1] == p - 1 and newC <= (len(mypath[r])) - 1:  # movement to the right.
            newR, newC = r, newC + 1
          #  print('r is ', r, 'c is', c)
        p -= 1
    
    return returnPathList

def arrayConvert(list):

    for a in list: # to concatenate the strings together; since making them into lists killed the arrays.
            list2String = ''.join([str(element) for element in list])
    return list2String

r, c = exit
p = mypath[r][c] #= 24
#print('row len:', r) FOR DEBUGGING
#print('column len:', len(mypath[r])) FOR DEBUGGING

traceBackLists = traceback(mypath, r, c)

def createCopyMaze(array): # array of an list
    newMaze = []
    for z in range(len(array)):
        newMaze.append(list(array[z])) # NOTE; create an array of the list to prepare for final print out. 
    
    return newMaze

myFinalMaze = createCopyMaze(maze)

for i in range(len(traceBackLists)):
   row = traceBackLists[i].getRow() #in order to identify the values of both the row and the column
   col = traceBackLists[i].getColumn()
   
   myColumnList = list(myFinalMaze[row]) #conversion of an array to a list. 

   myColumnList.pop(col)
   myColumnList.insert(col, "*")
   myFinalMaze[row] = myColumnList #inserts and deletes off the 'p' in place of a '*'.

print('\n')
print('The Path to the exit: ')
print('\n')
for e in range( len(myFinalMaze)): # USED to print out the final list. With the array convert; fully changes it from a list to an string
    print(arrayConvert(myFinalMaze[e]))


