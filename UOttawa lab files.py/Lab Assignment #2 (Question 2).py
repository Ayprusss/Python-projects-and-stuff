a = int(input ('Enter your first integer: ')) # first integer inputed that is to be multiplied with.
q = int(input ('Enter your second integer: ')) # multiplicate that will multiply with the first number
n = int(input ('Enter your third integer: ')) # number of integers you want produced. you know the number of iterations you need; therefore, for loop.

i = 0 

for i in range (0,n):
    product = a * (q ** i)
    i = i + 1
    print(str(product), end = ',')


#for i in range(1, n):
  #  product = a * q ** i
     #print (str(product), end =',')