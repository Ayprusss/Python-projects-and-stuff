
from bisect import bisect_right


patient_name = 'John Smith'
patient_age = '20'
patient_status_new = True 

print('patient is'+ patient_name)
print('patient age recorded ', patient_age)
print('individual is a new patient:', patient_status_new)

birth_year = input(' Enter your birth year: ')

age = 2022 - int(birth_year)
print ('your age is ', age)

a = float(input ('First number: '))
b = float(input ('Second number: '))

sum = int(a) +int(b)

print('your sum is:', sum)
