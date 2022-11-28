import math
    
class Vector:
    def __init__(self, n = 2):
        self.n = n  # value of dimension presented would be public, since it needs to be altered and accessed by others to do the other functions(?)        
        vectorList = []
        for x in range(0, self.n):
            vectorList.append(0)
        print(vectorList)
        self.valuelist = vectorList

    def dimension(self):
        dimension = self.n
        #dimension is equal to the number of elements inside the vector. 
        return dimension

    def get_dimension(self, index):
        getList = self.valuelist
            #getlist now has the value list of the initialized vector.
        dimensionvalue = getList[index - 1]
        print(dimensionvalue)
        return dimensionvalue

    def set_dimension(self, index, value):
        list = self.valuelist
        list[index - 1] = value

    def add_dimension(self, value):
        list = self.valuelist
        list.append(value)
        self.n += 1

    def remove_dimension(self):
        list = self.valuelist
        list.pop()
        self.n -= 1

    def insert_dimension(self, index, value):
        list = self.valuelist
        list.insert(value, index)
        self.n += 1
    def erase_dimension(self, index):
        list = self.valuelist
        list.remove(index)
        self.n -= 1

    def magnitude(self):
        list = self.valuelist
        squaredsum = 0
        for a in range(0, len(list)):
            squaredsum += ((list[a]) ** 2)
        
        return math.sqrt(squaredsum)
    def multiply(self, d):
        list = self.valuelist
        for a in range(0, len(list)):
            list[a] = d * list[a]
        #for a in range(0, len(list)):
    
    def print(self):
        list = self.valuelist
        return print(list)
        
    def equalOperator(self, d1, d2): #d1 and d2 = two Vectors 
        lis1 = d1.valuelist
        lis2 = d2.valuelist

        for a in range(0, len(lis1)):
            val1 = lis1[a]
            val2 = lis2[a]
            if val1 != val2:
                return False
            
        return True
    
    def nonEqualOperator(self, d2):
        lis1 = self.valuelist
        lis2 = d2.valuelist

        for a in range(0, len(lis1)):
            val1 = lis1[a]
            val2 = lis2[a]
            if val1 == val2:
                return False
        
        return True
    
    
                

    def multiplyCheck(self, b, c): # let b, c be the vectors for v1, v2, v3, v4, etc. let a be the one to compare. 
        # check if b and c have the same length.
        Bgreater = False
        Cgreater = False
        if len(b) != len(c): # make changes to make sure they're both equal. 
            if len(b) > len(c): # b is of greater length than c:
                BGreater = True
                x = len(c)
                while x != len(c):
                    c.add_dimension(0)
                    x += 1
            elif len(b) < len(c): #b is of lesser length than c:
                CGreater = True
                x = len(b)
                while x != len(c):
                    b.add_dimension(0)
                    x += 1
        
        productList = []
        for p in range(0, len(c)): # to multiply two of the lists together. 
            val1 = b[p]
            val2 = c[p]
            productnum = val1 * val2
            productList.append(productnum)
        
        def productCheck(self, m, lis):
            for q in range(0, len(m)):
                check1 = self.valueList[q]
                check2 = lis[q]
                if check1 == check2:
                    return True
                else:
                    return False
        
        if BGreater:
            if len(self.valueList) == len(b):
                self.productCheck(b)
        elif CGreater:
            if len(self.valueList) == len(c):
                self.productCheck(c)
            
        if productCheck(self, c, productList):
            return True

    def sumCheck(self, b, c): # let b, c be the two vectors to check.

        if len(b) != len(c): # make changes to make sure they're both equal. 
            if len(b) > len(c): # b is of greater length than c:
                x = len(c)
                while x != len(c):
                    c.add_dimension(0)
                    x += 1
            elif len(b) < len(c): #b is of lesser length than c:
                x = len(b)
                while x != len(c):
                    b.add_dimension(0)
                    x += 1
        

        sumList = []
        for p in range(0, len(c)):
            val1 = b[p]
            val2 = c[p]
            sumnum = val1 + val2
            sumList.appent(sumnum)

        def AddCheck(self, m, lis):
            for q in range(0, len(m)):
                check1 = self.valueList[q]
                check2 = lis[q]
                if check1 == check2:
                    return True
                else:
                    return False
        
        if AddCheck(self, c, sumList):
            return True
        else:
            return False
    
    def differenceCheck(self, b, c):

        if len(b) != len(c): # make changes to make sure they're both equal. 
            if len(b) > len(c): # b is of greater length than c:
                x = len(c)
                while x != len(c):
                    c.add_dimension(0)
                    x += 1
            elif len(b) < len(c): #b is of lesser length than c:
                x = len(b)
                while x != len(c):
                    b.add_dimension(0)
                    x += 1

        differenceList = []
        for p in range(0, len(c)):
            val1 = b[p]
            val2 = c[p]
            diffnum = val1 - val2
            differenceList.appent(diffnum)

        def diffCheck(self, m, lis):
            for q in range(0, len(m)):
                check1 = self.valueList[q]
                check2 = lis[q]
                if check1 == check2:
                    return True
                else:
                    return False
        
        if diffCheck(self, c, differenceList):
            return True
        else:
            return False


    




    


        





            



v1 = Vector(5)

v1.set_dimension(3, 25)
magnitude = v1.magnitude()
v1.multiply(5)
print(magnitude)
v1.print()
    





