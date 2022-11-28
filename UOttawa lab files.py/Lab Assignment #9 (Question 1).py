class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)
        self.marks[0] = round((self.marks[0]/10)*10,2) #total lab mark
        for i in range (1,6,1):#assignments
            self.marks[i] = round(((self.marks[i]/30)*5),2)
        #term test, midterm, and final mark remain the same
        self.marks = tuple(self.marks)

    def print(self):
        full = self.name.split()
        print("First name: " + full[0])
        print("Last name: " + full[1])
        print("Lab mark: " + str(self.marks[0]) + "%")
        for i in range(1,6,1):
            print("Assignment " + str(i) + ": " + str(self.marks[i]) + "%")
        print("Term test: " + str(self.marks[6]) + "%")
        print("Midterm: " + str(self.marks[7]) + "%")
        print("Final exam: " + str(self.marks[8]) + "%")
        final, grade = (Student.final(self))
        print("Final: " + str(final) + "%")
        print("Letter grade: " + grade)
        
    def final(self):
        final = 0
        letter = ""
        for i in range(0, 9, 1):
            final += self.marks[i]

        if(final >= 90):
            letter = "A+"
        elif(85 <= final < 90):
            letter = "A"
        elif(80 <= final < 85):
            letter = "A-"
        elif(75 <= final < 80):
            letter = "B+"
        elif(70 <= final < 75):
            letter = "B"
        elif(65 <= final < 70):
            letter = "C+"
        elif(60 <= final < 65):
            letter = "C"
        elif(55 <= final < 60):
            letter = "D+"
        elif(50 <= final < 55):
             letter = "D"   
        elif(40 <= final < 50):
            letter = "E"
        else:
            letter = "F"

        
        return final, letter
        
n = int(input("Enter number of students: "))
tstudents = []
for i in range (0,n,1):
    name = input("Name: ")
    tnums = input("Enter marks in one line: ").split()
    for j in range (0, len(tnums),1):
        tnums[j]=float(tnums[j])
    marks = tuple(tnums)
    student = Student(name,marks)
    tstudents.append(student)
students = tuple(tstudents)

for i in range(0,n,1):
    print("\nStudent " + str(i+1) + ": ")
    Student.print(students[i])