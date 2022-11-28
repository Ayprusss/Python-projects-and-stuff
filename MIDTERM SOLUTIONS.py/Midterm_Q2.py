
def combine(midterm, final):
    overall = { }
    for x in final:
        if x in midterm:
            overall[x] = midterm[x] + final[x]
        else:
            overall[x] = final[x]

    for x in midterm:
        if not(x in overall):
            overall[x] = 0

    return overall

# main program
n = int(input('Enter the number of students in the midterm: '))
midterm = { }

for i in range(0, n):
    print('Enter the name of student', i + 1, end = ': ')
    name = input('')
    print('Enter the midterm grade of student', i + 1, end = ': ')
    m = int(input(''))
    midterm[name] = m
    
n = int(input('Enter the number of students in the final: '))
final = { }

for i in range(0, n):
    print('Enter the name of student', i + 1, end = ': ')
    name = input('')
    print('Enter the final grade of student', i + 1, end = ': ')
    m = int(input(''))
    final[name] = m

ovrl = combine(midterm, final)
print(ovrl)
