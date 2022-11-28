n = int(input('Enter a non-negative number: '))

list = []
if n < 1:
    input('please input a number that is greater or equal to one.')
    quit()

diffylist = []

for m in range (0,n):
    print('Enter number no.', m + 1, ':', end = '')
    x = float(input(''))
    list.append(x)

for l in range (len(list)):
    i = list [l]
    for o in range (1, len(list)):
        p = list [o]
        difference = i - p
        if difference < 0: 
            difference = difference * - 1
        if difference == 0:
            break
        diffylist.append(difference)

diffylist.sort()

y = diffylist [0]

for t in range (0, n):
    u = list[t]
    for a in range (1, n):
        q = list[a]
        if u - q == y:
            print (q, u)
