n = int(input('how many numbers do you want to input? '))
k = int(input('what is the number you want to compare it to? ' ))

list = []

for i in range( 0, n):
    print('Enter value no.', i + 1)
    num = int(input(''))
    while 


same = True
for a in range (len(list)):
    value1 = list[a]
    while value1 > 0:
        div = value1 // 10
        if div != k:
            same = False
    if same:
        print(list[a])

    
