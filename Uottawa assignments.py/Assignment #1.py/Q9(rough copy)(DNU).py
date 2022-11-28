a = str(input('Enter your first string: '))
b = str(input('Enter your second string: '))

if len(a) > len(b):
    print('no occurence in list of first string in second string; first string is longer than second one.')

def forwardfind(a,b):
    values = []
    counter = 0
    while counter < len(b):
        counter = b.find(a,counter)
        if counter != -1:
            values.append(counter)
            counter += 1
        else:
            return values
    return values

forwardlist = forwardfind(a,b)
print(forwardlist)

def reversefind(a,b):
    rstring = a[::-1]
    rvalues = []
    rcounter = 0
    while rcounter < len(b):
        rcounter = b.find(rstring, rcounter)
        if rcounter == -1:
            return rvalues
        else:
            rvalues.append(-1 * (rcounter + len(a) - 1))
            rcounter += 1
    return rvalues

reverselist = reversefind(a,b)

print(reverselist)

reslist = []
count1 = []
count2 = []

for i in range(0,len(forwardlist)):
    reslist.append(forwardlist[i])

for p in range(0,len(reverselist)):
    reslist.append(reverselist[p])

print(reslist)

def existinlist(list1, value):
    matching = False
    for j in range(0, len(list1)):
        print('value of j:', list1[j])
        print('value of input =', value)
        if list1[j] == value:
            matching = True
            break
    return matching 


        
myfinallist = []
matchinglist = []
for m in range(len(reslist)):
    matching = False
    tempvalue = reslist[m]
    if m < len(reslist):
        for n in range(m + 1, len(reslist)):
            if abs(tempvalue) == abs(reslist[n]):
                matching = True
                if tempvalue < reslist[n]:
                    myfinallist.append(tempvalue)
                    myfinallist.append(reslist[n])
                    matchinglist.append(reslist[n])
                    matchinglist.append(tempvalue)
                    print('matchinlist = ', matchinglist)
                    break
                else:
                    myfinallist.append(reslist[n])
                    myfinallist.append(tempvalue)
                    matchinglist.append(reslist[n])
                    matchinglist.append(tempvalue)
                    print('matchinglist =', matchinglist)
                    break
    exist = existinlist(matchinglist, tempvalue)
    if exist == False:
        myfinallist.append(tempvalue)
        print('myfinallist(set) = ', myfinallist)

print('matching list =', matchinglist)
print('my final list = ', myfinallist)