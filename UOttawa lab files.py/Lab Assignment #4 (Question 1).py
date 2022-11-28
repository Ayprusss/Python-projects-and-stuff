
a = int(input('How many numbers do you want in your list?: '))

nums = []
uniquenums = []
for i in range (0, a):
    print('Enter element no.', i + 1, ':', end = ' ')
    b = int(input(''))
    nums.append(b)

for l in range (0, a):
    m = nums [l]
    x = nums.count(m)
    if x == 1:
        unique = True
        uniquenums.append(m)
    if x > 1:
        unique = False

print('your unique numbers are:', end = ' ')
print(*uniquenums, sep = ', ')

