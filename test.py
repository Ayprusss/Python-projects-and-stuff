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