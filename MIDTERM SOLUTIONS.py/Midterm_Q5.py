
# main part of the program
n = int(input('Enter the number of numbers in the first list: '))
first = []

for i in range(0, n):
    print('Enter number', i + 1, end = ': ')
    x = float(input(''))
    first.append(x)

m = int(input('Enter the number of numbers in the second list: '))
second = []

for i in range(0, m):
    print('Enter number', i + 1, end = ': ')
    x = float(input(''))
    second.append(x)

result = []

i = 0
j = 0

while i < n and j < m:
    if first[i] < second[j]:
        result.append(first[i])
        i = i + 1
    elif first[i] > second[j]:
        result.append(second[j])
        j = j + 1
    else:
        result.append(first[i])
        result.append(second[j])
        i = i + 1
        j = j + 1

if i < n:
    while i < n:
        result.append(first[i])
        i = i + 1
else:
    while j < m:
        result.append(second[j])
        j = j + 1

print(result)


    





