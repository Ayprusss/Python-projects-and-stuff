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

print('entrance: ', entrance)
print('exit: ', exit)
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

for x in range(len(mypath)):
    print(mypath[x])

endpointval = k

#def pathback (k, mypath, pathcoordinates): # code to move backwards to find the path back to Leon's starting point. 



class Cell: 
    def __init__(self, cellvalue, row, column, printvalue):
        self.cellvalue = cellvalue
        self.row = row
        self.column = column
        self.printvalue = printvalue
    


    def printMazeCoordinator(self):
        print( (self.row + 1, self.column + 1) )

    def print(self):
        print(self.cellvalue, '+',  self.printvalue, '+', (self.row, self.column))
    
    def setPrintValue(self, directionString):
        self.printvalue = directionString
    
    def getRow(self):
        return self.row
    
    def getColumn(self):
        return self.column
    
    def getPrintValue(self):
        return self.printvalue
    
    def getCellValue(self):
        return self.cellvalue


def populateCell(mypath, list, r, c, cellPrintValue): # r and c are current selected path cells (row and columns of selected cell.)
    p = mypath[r][c] # value at exit point. 

    newCell = Cell(p, r, c, cellPrintValue)
    list.append(newCell)
    return newCell   

def traceback(mypath, exitR, exitC): # r and c are current EXIT point. (row and columns of selected cell.);  ### 
    p = mypath[r][c]                # p is the value of the exit point inside mypath. the LAST VALUE in the 
    returnPathList = []             # returnpathlist contains all cells objects of the path.
    newR = exitR
    newC = exitC
    
    while p >= 1:
        print('IN TRACEBACK FUNCTION: p is', p,', r is ', newR, 'c is ', newC)
        
        newCell = populateCell(mypath, returnPathList, newR, newC, "*") # create cell object of push into path coordinate. 
        if newR > 0 and mypath[newR - 1][newC] == p - 1: # movement upwards..
            newR, newC= newR - 1, newC
            newCell.setPrintValue('v')
            #print('r is ', r, 'c is', c)
        elif mypath[newR][newC - 1] == p - 1 and newC >= 0: # movement to the left. 
            newR, newC = newR, newC - 1
            newCell.setPrintValue('>')
           # print('r is ', r, 'c is', c)
        elif mypath[newR + 1][newC] == p - 1 and newR <= len(mypath) - 1: # movement downwards........
            newR, newC = newR + 1, newC
            newCell.setPrintValue('^')
           # print('r is ', r, 'c is', c)
        elif mypath[newR][newC + 1] == p - 1 and newC <= (len(mypath[r])) - 1:  # movement to the right.
            newR, newC = r, newC + 1
            newCell.setPrintValue('<')
          #  print('r is ', r, 'c is', c)
        p -= 1
    
    return returnPathList

def reverseList(list):
    reverseList = []
    for i in range(len(list), 0, - 1):
        reverseList.append(list[len(list) - 1])
    
    return reverseList

r, c = exit
p = mypath[r][c] #= 24
print('row len:', r)
print('column len:', len(mypath[r]))

traceBackLists = traceback(mypath, r, c)
reverseBackList = reverseList(traceBackLists)
print('reverseBackList:', end = ' ')
for i in range(len(reverseBackList ) - 1):
    print(reverseBackList[i].getCellValue)

def createCopyMaze(array): # array of an list
    newMaze = []
    for z in range(len(array)):
        newMaze.append(list(array[z])) # NOTE; create an array of the list to prepare for final print out. 
    
    return newMaze

myFinalMaze = createCopyMaze(maze)

for k in range(len(myFinalMaze)):
    print(myFinalMaze[k])

#normal path. asterisks. 
for i in range(len(traceBackLists)):
   row = traceBackLists[i].getRow()
   col = traceBackLists[i].getColumn()
   myColumnList = list(myFinalMaze[row])

   myColumnList.pop(col)
   myColumnList.insert(col, '*')
   myFinalMaze[row] = myColumnList

print('')

#LOOP FOR BONUS MARKSSSS DIRECTION PATH
for i in range(len(traceBackLists)):
   row = traceBackLists[i].getRow()
   col = traceBackLists[i].getColumn()
   printvalue = traceBackLists[i].getPrintValue()
   myColumnList = list(myFinalMaze[row])

   myColumnList.pop(col)
   myColumnList.insert(col, printvalue)
   myFinalMaze[row] = myColumnList

for e in range( len(myFinalMaze)):
    print(myFinalMaze[e])



   # tracebacklists[i].print()
    #  tracebacklists[i].printMazeCoordinator()

