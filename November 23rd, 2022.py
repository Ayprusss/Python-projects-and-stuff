#Python inheritance: allows us to define a class with all methods and properties from another class.

#parent class is class being inherited from; base class/
#child class is class inheriting other class; derived class.

#child is a prent:
    #student is a person

#inheritence code:


import math

class Triangle: 
    def __init__(self, s1 = 1.0, s2 = 1.0, s3 = 1.0):
        self.__side1 = s1
        self.__side2 = s2   #adding the __ before the self initialization allows for the variable to be private. (what does that mean?)
        self.__side3 = s3

        m = max(s1, s2, s3) # used to determine the greatest values among the three sides.

        if s3 == m and s1 + s2 > s3: # user is being allowed to give the length of the three sides in any order. # INTHIS CASE; s3 is largest triangle side.
            if s1 < s2: #this is going to order them in a way that s1 is the smallest to the biggest (s3)
                self.__side1 = s1 
                self.__side2 = s2 # greater sides in ascending order
            else:
                self.__side1 = s2# ''
                self.__side2 = s1
        else:
            self.__side1 = self.__side2 = self.__side3 = 1.0 # if they do not follow the right-angle triangle validity; it will put up just an equilateral triangle. 
        

        if s2 == m and s1 + s3 > s2: # user is being allowed to give the length of the three sides in any order. # INTHIS CASE; s3 is largest triangle side.
            if s1 < s3: #this is going to order them in a way that s1 is the smallest to the biggest (s3)
                self.__side1 = s1 
                self.__side3 = s3 # greater sides in ascending order
            else:
                self.__side1 = s3# ''
                self.__side3 = s1
        else:
            self.__side1 = self.__side2 = self.__side3 = 1.0

        if s1 == m and s2 + s3 > s1: # user is being allowed to give the length of the three sides in any order. # INTHIS CASE; s3 is largest triangle side.
            if s2 < s3: #this is going to order them in a way that s1 is the smallest to the biggest (s3)
                self.__side2 = s2
                self.__side3 = s3 # greater sides in ascending order
            else:
                self.__side2 = s3# ''
                self.__side3 = s2
        else:
            self.__side1 = self.__side2 = self.__side3 = 1.0
        
        def perimeter():
            return self.__side1 + self.__side2 + self.__side3
        
        def area(self):
            p = self.perimeter() / 2
            return math.sqrt(p * (p- self.__side1) * (p*(p - self.__side2)) * (p * (p-self.__side3)))

        def getSmallestSide():
            return self.__side1

        def getLargestSide():
            return self.__side3
        
        def GetMidlleSide():
            return self.__side2

        def Print():
            return print('side 1 = ', self.__side1, 'side 2 = ', self.__side2, 'side 3 = ', self.__side3)


class Isoceles(Triangle): # indicates how we want something that is a triangle but with new properties (calls for Triangle class but would prob change it.)
    #with super() this term refers to the parent class; sub() would refer to the child class. # stops us from having to write .self... etc. 
    #Triangle with two equal sides. 
    def __init__(self, s1 = 1.0, s2 = 1.0, s3 = 1.0):
        #question; can I jsut do super and do this with the parent class?
        if s1 == s2:
            super().__init(s1,s2,s3) # using the functions from the parent cell to check whether or not a side is bigger or larger than the other two. 
        else:
            super().__init__() # the parent cell asks the values to just set the side values to their default values and to print back all 1's.






#main part of program.
t = Triangle(5.0, 7.0, 8.0)
print('Triangle t:')
t.Print()
t2 = Triangle (5, 3,8)
print('Triangle 2:')
t2.Print()

it = Isoceles(5, 7, 8)
print('Iscoeles it:')
it.Print()


it2 = Isoceles(9,4,9):
print('Isoceles it2:')
it2.print()

it3 = Isoceles(9,4, 9):
print('Isoceles it3: ')
it3.print()
y = it3.perimeter()
print(y)


class RightAngledTriangle(Triangle):
    def __init(self, s1 =1, s2 = 4, s3 = 5):
        if s1 * s1 _ s2 * s2 -- s3 * s3 or s1 * s1 + s3 * s3 == s2* s2:
            super().__init__(s1, s2, s3)
        else:
            super().__init__(3, 4, 5)

    
    #overriding the method area in the patent:
    def area(self):
        return (self.__side1 * self.__side2) / 2


rt = RightAngledTriangle( 5, 12 ,13)
x = rt.perimeter()
print(x)