
n = int(input('Enter the number of students: '))
course = []

for i in range(0, n):
    print('Entering info for student', i + 1)
    firstname = input('Enter the firstname of the student: ')
    lastname = input('Enter the lastname of the student: ')
    student_ID = int(input('Enter the student ID of the student: '))
    grade = float(input('Enter the grade of the student: '))
    student = (firstname, lastname, student_ID, grade)
    course.append(student)

print(course)
                     
