a = int(input ('enter your first mark '))
b = int(input ('enter your second mark '))
c = int(input ('enter your third mark '))

if a > b and a > c:
    print ('your first highest mark is', a)
elif a > b and a < c or a < b and a > c:
    print ('your second highest mark is', a)
elif a < b and a < c:
     print ('your lowest mark is ', a)

if b > a and b > c:
    print ('your first highest mark is', b)
elif b > a and b < c or b < a and b > c:
        print ('your second highest mark is', b)
elif b < a and b < c:
    print ('your lowest mark is', b)

if c > a and c > b:
    print ('your first highest mark is', c)
elif c > a and c < b or c < a and c > b:
    print ('your second highest mark is', c)
elif c < a and c < b:
    print ('your lowest mark is', c)
