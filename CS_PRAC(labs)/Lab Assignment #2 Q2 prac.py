a = int(input('Enter a non-neagtive integer: '))
b = int(input('Enter the number to multiple with integer: '))
c = int(input('how many times you want it to be multipled with the integer?: '))

for x in range(0,c - 1):
    product = a * (b ** x)
    print(product, end = ', ' )

print(a * (b ** (c - 1)))