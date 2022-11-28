x = str(input('Enter your first string: '))
y = str(input('Enter your second string: '))

a = sorted(x)
b = sorted(y)

if a == b:
    print('The two strings are anagrams.')
else:
    print('The two strings are not anagrams.')

