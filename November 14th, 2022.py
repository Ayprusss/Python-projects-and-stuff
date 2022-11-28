# LECTURE ON PYTHON TUPLES:

# tuple: used to store multiple items in single variable; collection is ordered and unchangeable. 
x = 2 

y = 20

x = 12.45
print('x is', x, 'y is', y)
print('x is:'+ str(x), 'y is:' + str(y))

names = ('John', 'Mark', 'Tim')

print(names[0])
print(names[1])
print(names[2])

# names[0] - 'Alex - Immutable; cant change it. just like lists but you can't change it. 

n = len(names)
for i in range(n - 1):
    print(names[n])


tuple1 = ('a', 'b', 'c')
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
#can add tuples togehter; a lot of the commands of lists can be done  onto tuples

# UNPACKING TUPLES
 #essentially printing out the elements in the typles
 # if 
fruits = ('apple', 'banana', 'cherry', 'strawberry', 'rasberry')

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red) #will ignore the rest of the fruits printed and will print out every other element in the tuple



student = ('Mark', 'Armstrong', 671282, 87.56)

fristname, lastname, student_ID, grade = student


n = int(input('Enter the number of students: '))
course = []

for i in range(0,n):
    print('Entering info for student', i + 1)
    firstname = input('Enter the first name of student:')
    lastname = input('Enter the last name of the student: ')
    student_ID = int(input("Enter the stduent's ID: " ))
    grade = int(input('Enter the grade of the student: '))
    student = firstname, lastname, student_ID, grade
    course.append(student)

print(course)


class student:
    def __init__(self, firstname, lastname, student_ID, grade): #__init__ short for initialize
        self.firstname - firstname
        self.lastname = lastname
        self.student_ID = student_ID
        self.grade = grade
        self.print = print(self)
    
    def print(self):
        print('firstname = ' + self.firstname)
        print('lastname = ' + self.lastname)
        print('Student ID = ' + str(self.student_ID))
        print('Grade = ' + str(self.grade))


s1 = student('Mark', 'Armstrong',' 7821', '90.21')
s2 = student('John', 'James', 8012, 92.21)


s1.print()

#what does self mean???? what object is calling this function?. Self refers to the object that called for this function.
# s1.print() ; self = s1. 
#s2.print() ; self = s2. 
#etc.