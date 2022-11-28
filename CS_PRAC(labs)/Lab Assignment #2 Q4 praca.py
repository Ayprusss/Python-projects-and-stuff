n = int(input('Enter a non-negative number: '))

print(n, end = ', ')
odd = True
while n != 1:
    
    if n % 2 != 0:
        n = (3 * n) + 1
        print(n, end = ', ')
    

    elif n % 2 == 0:
        odd = False
        n = (n // 2)
        print(n, end = ', ')




