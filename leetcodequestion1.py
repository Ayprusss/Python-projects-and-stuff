#check in arrays if there are duplicates; if true, then print 'true', else, pring 'false'; they are disctinct numbers
nums = list(map(int, input("Enter all the numbers you would like to add into your list(seperated by spaces): ").split()))

distinct = True
for i in range(len(nums)):
    distinct = True
    value1 = nums [i]
    for l in range(1, len(nums)):
        value2 = nums [l]
        if value1 == value2:
            distinct == False
            print('True')
            quit()
        else: 
            break
    if distinct:
        print('False')
        quit()
        
