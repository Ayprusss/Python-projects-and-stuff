
class Student:
    def __init__(self, firstname, lastname, student_ID, grade):
        self.firstname = firstname
        self.lastname = lastname
        self.student_ID = student_ID
        self.grade = grade

    def print(self):
        print('firstname = ' + self.firstname)
        print('lastname = ' + self.lastname)
        print('Student ID = ' + str(self.student_ID))
        print('Grade = ' + str(self.grade))

s1 = Student('Mark', 'Armstrong', 7821, 90.21)
s2 = Student('John', 'James', 7912, 92.21)
s3 = Student('Rahim', 'Bahrami', 8338, 70.12)

s1.firstname = 'Mike'

#print(s1.toString())
s1.print() #self is s1
s2.print() #self is s2
s3.print() #self is s3


