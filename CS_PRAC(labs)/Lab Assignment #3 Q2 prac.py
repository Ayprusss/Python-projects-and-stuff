n = int(input('Enter a non-negative integer n: '))
while n < 0:
    n = int(input('Enter a non-negative integer n:'))
k = int(input('Enter a non-negative integer k: '))
while k < 0:
    k = int(input('Enter a non-negative integer k: '))


for x in range(0, n):
    print('Enter no.', x + 1)
    num = int(input(''))
    newnum = num
    
    while num != 0:
        if num == k:
            print(newnum)
        num // 10
            

    
    