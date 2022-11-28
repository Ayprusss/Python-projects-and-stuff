a = str(input ('Enter the first string: '))
b = str(input ('Enter the second string you want to compare: '))

d = len(b)
def substring (a,b):
    result = b.rfind(a)
    return result

if substring (a,b) > -1:
    print('The first string,', a, 'is a substring occuring at position', substring(a,b))
if substring (a,b) == -1:
    print('the first string,',a,',is not a substring of the second string.')
    print('the length of the second string is', d)