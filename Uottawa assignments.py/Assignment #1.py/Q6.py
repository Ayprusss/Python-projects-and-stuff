#############################################################
#Anthony Le; 300287511
#Assignment 1, Question 6 
# october 21, 2022

#############################################################


n = int(input(' Enter how many numbers you want in your data set: '))
data = []
for i in range (0,n):
    print('Enter value no.', i + 1, ':',end = '')
    y = float(input(''))
    data.append(y)      # inputing values into the data set. 
#Average:
sum = 0
for s in range(0,n):
    add = data[s]
    sum = sum + add
ave_nums = len(data)
def Average(list):
    return sum / ave_nums
print('Average:', round(Average(data),2))
# Mode:
modes = []
moderange = len(data)
for m in range(0, moderange):
    number = data [m]
    if data.count(number) > 1:
        modes.append(number)
print('Mode:', str(set(modes)))
#median.
data.sort()
medianrange = len(data)
if medianrange % 2 == 0: # shows that there are even amounts of numbers found within the list.
    middlenum1 = data[n // 2]
    middlenum2 = data[n // 2 - 1]
    median = (middlenum1 + middlenum2) / 2
    print ('Median:', median)
else:
    median = data[n // 2]
    print('Median:', median)
#Range.
data.sort()
listrange = len(data)
firstnum = data [0]
lastnum = data [listrange - 1]
range = lastnum - firstnum
print('Range:',round(range, 2))


