d = 7823.1293912
temp_d = "{:.3f}".format(d) # used to round up the number to the decimal point shown.

# .3f; means that it's rounded to the third decimal place.
    # 

print(temp_d)


nums  = [1, 4, 5, 6, 7, 19, 20, 34, 12, 10]

a = nums.index(34)
print (a)   # shows which spot the number 34 is in list
nums[5] = 60
print (nums)

print('the last element =', nums [-1])
print(' the second to last element =', nums [-2]) # negative indexes indicating the values from right to left of the list instead of the usual left to right (associated by its positive values)

#REMINDER; you can make a forloop go backwards; 
# scanning an array backwards/
b = len(nums)
#for i in range( n-1, -1, -1): (start, stop, step)
    # print(nums [i], end = ' ')

for i in range
