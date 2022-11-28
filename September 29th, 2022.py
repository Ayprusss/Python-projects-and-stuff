
# data structures???? and some more content on nested loops
# positive integer n 
# n = postiive integers (input)
# i.e. n = 5
# want to receive five integers.
# 1021 909 8811 11011 8712
# we will read n; find out how many integers are there; going to read a looop and then print out all numbers that are palindromic./.
# output = 909 11011

# 8821 rev = rev * 10 + r ; x = x // 10
# r = 8821 % 10 = 1 (unit number); rev = 0; x = 8821
#  r = 8821 % 10 = 1; rev - 1 x = 882
# r = 88 % 10 = 8, rev = 12; x = 88
# r = 8 % 10 = 8l rev = 12* 10 + 8 = 128; x = 8
# r = 0 % 10 = 0; rev - 1288; x = 0

# rev = reverse of 8821 ; 1288

# if we go back to observe x; x will be zero because nested loop has destroyed x.


# INTRO TO DATA STRUCTURE

n = int(input(' Enter the number of positive integers: '))  # we ask how many integers the for loop will read

for i in range (1, n+1):
    x = int(input('Enter a positive integer: ')) # this is used to read the inputs to gain all n numbers.
    temp = x # to keep and save the original value of the integer (x)
    rev = 0 
    while x != 0:
        r = x % 10
        rev = rev * 10 + r
        x = x // 10
    if temp == rev:
        print(temp,' is a palindrome number.')     # if equal; number is palindromic


# data structure; known as array or list.
# in different langauges; array or list are different terms
# known as just arrays in python
# arrays; which are also called lists in python, are groups of elements taht have the same name and the same data type. 
# the name of the array is the same nae they use; each element has a number (index)

palindromes = []


# near end of program:

if temp == rev:
    palindromes.append(temp)

print('Palindrome nummbers are:', end =' ')
for num in palindromes:
    print(x, end = ' ')
print(')')
print(palindromes)


l = len(palindromes)    # len function gives you number of elements you have in list [use this for lab 3 question 1]

print('palindrome numbers:  (', end = ' '))
for l in range (0, l):
    print(palindromes[l], end =' ')
print(')')


# for loops and lists will be seen together most of the time