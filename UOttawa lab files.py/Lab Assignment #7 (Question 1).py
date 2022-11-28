
u = []
a = []
b = []

num = int(input('Enter the length of the Universal Set: '))

for x in range(num):
    s = int(input('Enter number: '))
    u.append(s)

num = int(input(' Enter the length of Set A: '))

for y in range(num):
    s = int(input('Enter Number: '))
    a.append(s)

num = int(input('Enter the length of Set B: '))

for z in range(num):
    s = int(input('Enter Number: '))
    b.append(s)

a = set(a)
b = set(b)
u = set(u)

print('A Union B =', sorted(a.union(b)))
print('A Intersection B =',sorted(a.intersection(b)))
print('A - B =', sorted(a.difference(b)))
print('B - A =', sorted(b.difference(a)))
print('A Complement =', sorted(u.difference(a)))
print('B Complement =', sorted(u.difference(b)))
print('A ^ B =', a^b)


if a.issubset(b) == True:
    print('A is subset of B')
elif b.issubset(a) == True:
    print('B is subset of A')
elif b.issubset(a) == True and a.issubset(b) == True:
    print('A is equal to B')
else:
    print('A is not a subset of B and vice versa.')