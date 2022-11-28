list = []

x = int(input('Enter the first number: '))
list.append(x)
y = int(input('Enter the second number: '))
list.append(y)
z = int(input('Enter the third number: '))
list.append(z)

print(list)

list.sort()
print(list) 
multiple = 100
bignum = 0
print('biggest: ', end = '')

for i in range(len(list) - 1, -1 , -1):
    bignum = bignum + list[i] * multiple
    multiple = multiple // 10
print(bignum)

print('smallest: ', end = '')

smolnum = 0
multiple2 = 100
for j in range(len(list)):    
    smolnum = smolnum + list[j] * multiple2
    multiple2 = multiple2 // 10
print(smolnum)





'''if (x > y and x > z) and y > z: # x biggest number:
    print ( 'biggest:', x * 100 + y * 10 + z)
    print ('smallest:', z * 100 + y * 10 + x)
elif (x > y and x > z) and y < z:
    print ('biggest:', x * 100 + z * 10 + y)
    print('smallest:', y + 10 * z + x * 100)

if ( y > x and y > z) and x > z: # y biggest number
    print('biggest', y * 100 + x * 10 + z)
    print('smallest: ', z * 100 + x * 10 + y)
elif (y > x and y > z) and x < z:
    print('biggest: ', y * 100 + z * 10 + x)
    print('smallest:', x * 100 + z * 10 + y)'''





