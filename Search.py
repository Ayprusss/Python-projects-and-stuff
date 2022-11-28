s
# 7
# 15 18 19 20 7 6 12
# 19

n = int(input('Enter the number of elements: '))
nums = [ ]

for i in range(0, n):
    print('Enter element', i + 1, ':', end = ' ')
    x = int(input(''))
    nums.append(x)
    
#Just to see that we read the list correctly
#print(nums)

a = int(input('Enter the element you are looking for in the list:'))

#ind = nums.index(a)

#print(a, 'is at index', ind + 1)

found = False

for i in range(0, n):
    if nums[i] == a:
        print(a, 'is at index', i + 1)
        found = True
        break

if not(found):
    print(a, 'is not in this list')

