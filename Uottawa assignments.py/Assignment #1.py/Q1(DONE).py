# Enter function that enters positive integer greater than 1. program should analyze this number into prime elements.

n = int(input('Enter a non-negative integer:'))
newnum = n
myresults = []
resStr = str('')
while newnum != 1:
    for i in range (2,n+1):    
        while (newnum % i) == 0:
            myresults.append(i)
            newnum = (newnum // i) + (newnum % i)            
            if newnum % i > 0:
                break

listlength = len(myresults)

if len(myresults) == 1:
    resStr = str(myresults[0])
for m in range (0, listlength):
    currentnum = myresults[m]
    occurnum = myresults.count(currentnum)
    if occurnum > 1 and myresults[m] == myresults [m + 1]:
        resStr = str(resStr) + str(currentnum) + '^' + str(occurnum) + ' * '
        if currentnum ** occurnum == n:
            break
    else:
        if myresults[m] != myresults [m - 1]:
            resStr = str(resStr) + str(currentnum) + ' * '
    
print(resStr)


    