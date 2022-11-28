# Question #2: wrtie a program that receives two positive integers n & k; your program should receive n integers as shown. must receive inputs in a loop now. among numbers;
# need to print those numbers that starts with k.
# not allowed to use strings in program. Just integers. 

n = int(input(' Enter how many numbers you want in your list: '))
while n < 0:
    n = int(input(' Enter how many numbers you want in your list: '))

k = int(input('Enter a non-negative number to compare: '))
while n < 0:
    k = int(input('Enter a non-negative number to compare (k): '))

num = 0
list = []
listnum = 0
for i in range (1, n+1):
    print('For integer', i, end = ',')
    x = int(input('enter a non-negative number to the list: '))
    num = x
    while num != 0:
        if num == k:
            list.append(x)
            listnum = listnum + 1
        num = num // 10

for z in range (listnum):
    print(list[z], end = ' ')





