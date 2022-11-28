# Question 1: write a program that receives three digits (can use integers for them), your output should be the leargest and the smallest number you can make with those three digits.

a =int(input (' Enter your first number: '))
b = int(input (' Enter your second number: '))
c = int(input ('Enter your third number: '))
# for number sets that are unique and are bigger or smaller than one another
if a > b and a > c and b > c:       
    big_1 = a * (100) + b * (10) + c   #abc
    print (' your biggest number is', big_1)
    small_1 = c * (100) + b * (10) + a  #cba()
    print ('your smallest number is', small_1)
    
elif a > b and a < c and c > b:
    big_2 = c * (100) + a * 10 + b      #cab
    print (' your biggest number is', big_2)
    small_2 = b * (100) + a * 10 + c    #bac()
    print ('your smallest number is', small_2)

elif a < b and a < c and b > c:
    big_3 = b * (100) + c * 10 + a      #bca
    print (' your biggest number is', big_3)
    small_3 = a * (100) + c * 10 + b        #acb()
    print ('your smallest number is ', small_3)

elif a < b and a < c and b < c:
    big_4 = c * (100) + b * 10 + a      #cba
    print (' your biggest number is', big_4)
    small_4 = a + b * 10 + c * 100          #abc()
    print ('your smallest number is', small_4)

elif a > c and b < c and b < a:
    big_5 = a * (100) + c * 10 + b      #acb
    print (' your biggest number is', big_5)
    small_5 = b * 100 + c * 10 + a      #bca()
    print ('your smallest number is', small_5)

elif b > a and b > c and a > c:
    big_6 = b * (10 ** 2) + a * 10 + c     #bac
    print (' your biggest number is', big_6)
    small_6 = c * 100 + a * 10 + b          #cab()
    print ('your smallest number is', small_6)

# for number sets that are not unique and that have the same values
if b == a and a == c:
    same = a * 100 + b * 10 + c
    print ('your biggest and smallest number is', same)

# for number sets that are slightly unique; two values of the set are identical but one is unique.
if a == b and a > c and b > c:
    bs = a * 100 + b * 10 + c
    print ('your biggest number is ', bs)
    sb = c * 100 + a * 10 + b
    print ('your smallest number is', sb)
elif a == c and a > b and c > b:
    bs_2 = a * 100 + c * 10 + b
    print ('your biggest number is ', bs_2)
    sb_2 =  b * 100 + c * 10 + a 
    print ('your smallest number is', sb_2)
elif b == c and b > a and c > a:
    bs_3 = b * 100 + c * 10 + a
    print ('your biggest number is ', bs_3)
    sb_3 =  a * 100 + c * 10 + b 
    print ('your smallest number is', sb_3)