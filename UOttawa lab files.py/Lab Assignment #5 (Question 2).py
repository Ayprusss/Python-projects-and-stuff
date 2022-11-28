import math

n = int(input('How many numbers do you want in your data set?: '))
nums = []

for i in range (0, n):
    print('Enter value for data no.', i + 1)
    b = float(input(''))
    nums.append(b)

def average(nums):
    total = len(nums)
    average = sum(nums) / total
    return average


def eqn(nums):
    eqn = 0
    for l in range (0, n):
        x = nums[l]
        eqn = eqn + (x - average(nums)) ** 2
    
    return eqn
    
def standev(nums):
    stdev = math.sqrt(eqn(nums) / n) 
    return stdev

print('Standard Deviation:', standev(nums))