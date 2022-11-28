a = int(input('Enter a non-negative integer: '))
newnum = 0
num = a
while  a != 0:
    newval = a % 10
    newnum = (newnum * 10) + newval
    a = a // 10
    if a == 0:
        break


print(newnum)
    
