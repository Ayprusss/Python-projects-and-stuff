
def Union(setA, setB):
    result = []
    for x in setA:
        if not(x in result):
            result.append(x)
        
    for x in setB:
        if not(x in result):
            result.append(x)

    return result
            
def Intersection(setA, setB):
    '''
    ([int], [int]) -> [int]
    The function returns a list of integers which contains
    the common elements of the two given lists
    '''
    result = []
    for x in setA:
        if (x in setB) and not(x in result):
            result.append(x)

    return result

def Difference(setA, setB):
    result = []
    for x in setA:
        if not(x in setB) and not(x in result):
            result.append(x)

    return result

def Mutual_Difference(setA, setB):
    return Union(Difference(setA, setB), Difference(setB, setA))

def Print_Set(setA, message):
    '''
    ([int], str) --> None
    It prints the given list of integers starting with the given message
    '''
    print(message, end = '')
    size = len(setA)
    for i in range(0, size):
        if i == size - 1:
            print(setA[i], end = '')
        else:
            print(setA[i], end = ', ')
    print('}')

n = int(input('Enter the number of elements in the universal set: '))
universal = []

for i in range(0, n):
    print('Enter element', i + 1, 'in the universal set:', end = ' ')
    x = int(input(''))
    if not(x in universal):
        universal.append(x)

numA = int(input('Enter the number of elements in set A: '))
A = []

for i in range(0, numA):
    print('Enter element', i + 1, 'in set A :', end = ' ')
    x = int(input(''))
    if not(x in A):
        A.append(x)

numB = int(input('Enter the number of elements in set B: '))
B = []

for i in range(0, numB):
    print('Enter element', i + 1, 'in set B:', end = ' ')
    x = int(input(''))
    if not(x in B):
        B.append(x)

union = Union(A, B)
intersection = Intersection(A, B)
AdiffB = Difference(A, B)
BdiffA = Difference(B, A)
Acomp = Difference(universal, A)
Bcomp = Difference(universal, B)
AxorB = Mutual_Difference(A, B)

union.sort()
intersection.sort()
AdiffB.sort()
BdiffA.sort()
Acomp.sort()
Bcomp.sort()
AxorB.sort()

Print_Set(union, 'A Union B = {')
Print_Set(Intersection, 'A Intersection B = {')
Print_Set(AdiffB, 'A - B = {')
Print_Set(BdiffA, 'B - A = {')
Print_Set(Acomp, 'A Complement = {')
Print_Set(Bcomp, 'B Complement = {')
Print_Set(AxorB, 'A ^ B = {')

























