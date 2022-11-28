# program receives two positive integers; n and b. n is number is base 10; must convert it to base b.
# conversion; take n and divide by until quotient is equal to 0. take remainders 
n = int(input('Enter a non-negative integer: '))
b = int(input('Enter the base you want to convert the number to: '))

num = n 
remainderlist = []
remaindernum = -1
reverse_r = 0
while n != 0:
    remainder = n % b
    remainderlist.append(remainder) 
    remaindernum += 1
    n = n // b
    
while remaindernum != -1:
    reverse_r = reverse_r * 10 + remainderlist[remaindernum]
    remaindernum -= 1
    if remaindernum == -1:
        break

print(reverse_r) 

    




