import math

class Vector:
    def __init__(self, n = 2):
        self.n = n  # value of dimension presented would be public, since it needs to be altered and accessed by others to do the other functions(?)        
        vectorList = []
        for x in range(0, self.n):
            vectorList.append(0)
        self.valuelist = vectorList

    def dimension(self):
        dimension = self.n
        #dimension is equal to the number of elements inside the vector. 
        return dimension

    def get_dimension(self, index):
        getList = self.valuelist
            #getlist now has the value list of the initialized vector.
        dimensionvalue = getList[index]
        return dimensionvalue

    def set_dimension(self, index, value):
        list = self.valuelist
        list[index] = value

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
        list.insert(index, value)
        self.n += 1
    
    def erase_dimension(self, index):
        list = self.valuelist
        lisvalue = list[index - 1]
        list.remove(lisvalue)
        self.n -= 1
    
    def magnitude(self):
        list = self.valuelist
        squaredsum = 0
        for a in range(0, len(list)):
            squaredsum += (list[a]) ** 2
        
        return math.sqrt(squaredsum)
    def multiply(self, d):
        list = self.valuelist
        for a in range(0, len(list)):
            list[a] = d * list[a]

    def print(self):
        list = self.valuelist
        return print(list)

    # add the operators here, you should know the signature of them
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

    def nonEqualOperator(self, d2):
        lis1 = self.valuelist
        lis2 = d2.valuelist

        for a in range(0, len(lis1)):
            val1 = lis1[a]
            val2 = lis2[a]
            if val1 == val2:
                return False
        
        return True
    
    def equalOperator(self, d1, d2): #d1 and d2 = two Vectors 
        lis1 = d1.valuelist
        lis2 = d2.valuelist

        for a in range(0, len(lis1)):
            val1 = lis1[a]
            val2 = lis2[a]
            if val1 != val2:
                return False
            
        return True

# Main part of the program
da = [4.23, 5.01, 10.2, 5.51, 6.78]
db = [-1.32, 7.12, -5.55]
dc = [-1.0, 1.0, 5.0, -4.5, 3.5, 2.5, -6.0]

v1 = Vector(5)
v2 = Vector(5)
v3 = Vector(7)
v4 = Vector(7)

n = len(da)
for i in range(0, n):
    v1.set_dimension(i, da[i])

n = len(db)
for i in range(0, n):
    v2.set_dimension(i, db[i])

n = len(dc)
for i in range(0, n):
    v3.set_dimension(i, dc[i])
    v4.set_dimension(i, dc[i])

# Testing dimension
if v1.dimension() == 5:
    print('Test 1 - dimension - Passed')
else:
    print('Test 1 - dimension - Failed')
	
if v2.dimension() == 5:
    print('Test 2 - dimension - Passed')
else:
    print('Test 2 - dimension - Failed')
	
if v3.dimension() == 7:
    print('Test 3 - dimension - Passed')
else:
    print('Test 3 - dimension - Failed')

if v4.dimension() == 7:
    print('Test 4 - dimension - Passed')
else:
    print('Test 4 - dimension - Failed')

# Testing add_dimension and get_dimension
v1.add_dimension(6.45)
if v1.dimension() == 6 and v1.get_dimension(5) == 6.45:
    print('Test 1 - add_dimension - Passed')
else:
    print('Test 1 - add_dimension - Failed')

v2.add_dimension(7.81)
if v2.dimension() == 6 and v2.get_dimension(5) == 7.81:
    print('Test 2 - add_dimension - Passed')
else:
    print('Test 2 - add_dimension - Failed')
    
v4.add_dimension(5.76)
if v4.dimension() == 8 and v4.get_dimension(7) == 5.76:
    print('Test 3 - add_dimension - Passed')
else:
    print('Test 3 - add_dimension - Failed')

# Testing remove_dimension
v1.remove_dimension()
if v1.dimension() == 5:
    print('Test 1 - remove_dimension - Passed')
else:
    print('Test 1 - remove_dimension - Failed')

v4.remove_dimension()
if v4.dimension() == 7:
    print('Test 2 - remove_dimension - Passed')
else:
    print('Test 2 - remove_dimension - Failed')
    
# Testing insert_dimension
v1.insert_dimension(3, 5.71)
if v1.get_dimension(3) == 5.71 and v1.dimension() == 6:
    print('Test 1 - insert_dimension - Passed')
else:
    print('Test 1 - insert_dimension - Failed')

v2.insert_dimension(5, 7.3);
if v2.get_dimension(5) == 7.3 and v2.dimension() == 7:
    print('Test 2 - insert_dimension - Passed')
else:
    print('Test 2 - insert_dimension - Failed')

# Testing erase_dimension
v1.erase_dimension(2)
if v1.get_dimension(2) == 5.71 and v1.dimension() == 5:
    print('Test 1 - erase_dimension - Passed')
else:
    print('Test 1 - erase_dimension - Failed')

v4.erase_dimension(5)
if v4.get_dimension(5) == -6.0 and v4.dimension() == 6:
    print('Test 2 - erase_dimension - Passed')
else:
    print('Test 2 - erase_dimension - Failed')

# Testing magnitude
if abs(v1.magnitude() - 12.325810318190038) < 1e-9:
    print('Test 1 - magnitude - Passed')
else:
    print('Test 1 - magnitude - Failed')

if abs(v2.magnitude() - 14.054372984946713) < 1e-9:
    print('Test 2 - magnitude - Passed')
else:
    print('Test 2 - magnitude - Failed')

if abs(v3.magnitude() - 10.087120500916008) < 1e-9:
    print('Test 3 - magnitude - Passed')
else:
    print('Test 3 - magnitude - Failed')

# Testing multiply
v2 = v1.multiply(5)
if (v2 == v1.multiply(5)):
    print('Test 1 - multiply - Passed')
else:
    print('Test 1 - multiply - Failed')

v3 = v1.multiply(6.43)
if v3 == v1.multiply(6.43):
    print('Test 2 - multiply - Passed')
else:
    print('Test 2 - multiply - Failed')

# Testing operator *
v4 = v2 * v3
if v4.multiplyCheck(v1, v2):
    print('Test 1 - * - Passed')
else:
    print('Test 1 - * - Failed')

v4 = v2 * v3
if (v4.valuelists).multiplyCheck(v2.vauelists, v3.valuelists):
    print('Test 2 - * - Passed')
else:
    print('Test 2 - * - Failed')

# Testing operator +
v2 = v1 + v4;
if (v2.valuelists).sumCheck(v1.valuelists, v4.valuelists):
    print('Test 1 - + - Passed')
else:
    print('Test 1 - + - Failed')

v3 = v1 + v2;
if (v3.valuelists).sumCheck(v1.valuelists, v4.valuelists):
    print('Test 2 - + - Passed')
else:
    print('Test 2 - + - Failed')

v1 = v2 + v4

if (v1.valuelists).sumCheck(v1.valuelists, v4.valuelists):
    print('Test 3 - + - Passed')
else:
    print('Test 3 - + - Failed')
          
# Testing -
v2 = v1 - v4;
if (v2.valuelists).differenceCheck(v1.valuelists, v4.valuelists):
    print('Test 1 - - - Passed')
else:
    print('Test 1 - - - Failed')
    
v3 = v1 - v2
if (v3.valuelists).differenceCheck(v1.valuelists, v2.valuelists):
    print('Test 2 - - - Passed')
else:
    print('Test 2 - - - Failed')
   
v1 = v2 - v4;
if (v1.valuelists).differenceCheck(v2.valuelists, v4.valuelists):
    print('Test 3 - - - Passed')
else:
    print('Test 3 - - - Failed')

# Testing print
v1.print()
v2.print()
v3.print()
v4.print()
'''Should be printed
[4.230000000000018, 5.009999999999991, 5.710000000000036, 5.509999999999991, 6.779999999999745]
[579.4867350000001, 811.9782149999998, 1053.9318150000001, 981.5872149999998, 1484.6640599999996]
[575.256735, 806.9682149999998, 1048.221815, 976.0772149999998, 1477.8840599999999]
[575.256735, 806.9682149999998, 1048.221815, 976.0772149999998, 1477.8840599999999]
'''