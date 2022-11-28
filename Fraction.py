
class Fraction(object):
    # num = 5
    # dnum = 6
    def __init__(self, n = 0, d = 1):
        self.__num = n
        if d == 0:
            print('The denominator cannot be 0')
            self.__dnum = 1
        else:
            self.__dnum = d

    def getNum(self):
        return self.__num

    def getDnum(self):
        return self.__dnum
    
    def setNum(self, n):
        self.__num = n
        
    def setDnum(self, d):
        if d != 0:
            self.__dnum = d

    def add(self, f):
        result = Fraction()
        result.__dnum = self.__dnum * f.__dnum
        result.__num = self.__dnum * f.__num + self.__num * f.__dnum
        return result

    def __add__(self, f):
        result = Fraction()
        result.__dnum = self.__dnum * f.__dnum
        result.__num = self.__dnum * f.__num + self.__num * f.__dnum
        gcd = result.__GCD(abs(result.__num), abs(result.__dnum))
        result.__num = result.__num // gcd
        result.__dnum = result.__dnum // gcd
        
        return result

    def __sub__(self, f):
        result = Fraction()
        result.__dnum = self.__dnum * f.__dnum
        result.__num = self.__dnum * f.__num - self.__num * f.__dnum
        gcd = result.__GCD(abs(result.__num), abs(result.__dnum))
        result.__num = result.__num // gcd
        result.__dnum = result.__dnum // gcd
        
        return result

    def __mul__(self, f):
        result = Fraction()
        result.__num = self.__num * f.__num
        result.__dnum = self.__dnum * f.__dnum
        gcd = result.__GCD(abs(result.__num), abs(result.__dnum))
        result.__num = result.__num // gcd
        result.__dnum = result.__dnum // gcd
        
        return result

    def __eq__(self, f):
        return self.__num * f.__dnum == self.__dnum * f.__num
    
    def __lt__(self, f):
        return self.__num * f.__dnum < self.__dnum * f.__num
    
    def __le__(self, f):
        return self < f or self == f

    def __gt__(self, f):
        return not(self <= f)

    def __ge__(self, f):
        return not(self < f)

    def __ne__(self, f):
        return not(self == f)

    def __GCD(self, a, b):
        # 18
        # 12
        # 18 % 12 = 6, 12 % 6 = 0
        # 100 % 70 = 30, 70 % 30 = 10, 30 % 10 = 0
        
        while(True):
            r = a % b
            a = b
            b = r
            if r == 0:
                break;
        return a
            
    def simplify(self):
        # divide both numerator and denominator by greatest common divisor
        # Greatest Common Divisor = GCD
        # 18    1, 2, 3, 6, 9, 18
        # 12    1, 2, 3, 4, 6, 12
        # Common ones = 1, 2, 3, 6   GCD = 6
        gcd = self.__GCD(abs(self.__num), abs(self.__dnum))
        self.__num = self.__num // gcd
        self.__dnum = self.__dnum // gcd

    def print(self):
        '''
        This method prints the fraction value using / in the formatting
        '''
        print(self.__num, '/', self.__dnum)

# main part of the program
f1 = Fraction(3, 5)
f2 = Fraction(2, 7)

if f1 > f2:
    print('f1 is greater')
else:
    print('f1 is not greater')

f3 = Fraction()
#intializing a wrong value but the class takes care of it
f4 = Fraction(1, 0)
f5 = Fraction(6, 5)

#adding two fractions
f6 = f1.add(f5) # f1 + f5
f7 = f1 + f5
f6.simplify()
print('f6 =', end = ' ')
f6.print()
print('f7 =', end = ' ')
f7.print()

f8 = f1 - f5
f9 = f1 * f5
f8.print()
f9.print()

f1.__dnum = 0 # It does not work because dnum is private
#changing the values using a method is under our control
f1.setDnum(7)
print(f1.getNum())
f1.print()  
f2.print()
f3.print()
