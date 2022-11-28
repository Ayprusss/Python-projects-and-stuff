
def num_commons(first, second):
    flen = len(first)
    slen = len(second)
    
    if flen < slen:
        m = flen
    else:
        m = slen

    for i in range(m, -1, -1):
        matched = True
        k = flen - i
        for j in range(0, i):
            if second[j] != first[k]:
                matched = False
                break
            k = k + 1
            
        if matched:
            return i

    return 0

str1 = input('Enter the first list of words: ')
str2 = input('Enter the second list of words: ')

first_list = str1.split()
second_list = str2.split()

num = num_commons(first_list, second_list)
result = []

n = len(first_list)
m = len(second_list)

for i in range(0, n):
    result.append(first_list[i])

for i in range(num, m):
    result.append(second_list[i])

print(result)
