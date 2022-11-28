#brief on methods:

def capital(d, country): # if dictionary is an input that maps country to their captial; function is to get country and find it's capital; print.
    if country in d:
       return d[country]
    
    return 'Country is not found!'


d = {'Canada': 'Ottawa', 'Germany': 'Berlin', 'France': 'Paris'} # indexing from a dictionary uses [] brackets. But to define one, you need curly brackets.

# default arguments of a function:


def sum(a, c, b = 0): # all variables must be on the left-most side. Something with a default value must be on the right-most side: (i.e. b= 0 on the right)
    return a + b + c

p = sum(3,4)

#def range(start, end = 0, step = 1): # range function. We are allowed deafault arguments for functions

#range (0,5) --> [0, 1, 2, 3, 4]

#range(6) --> [0, 1, 2, 3, 4, 5]

#range(2,7,2) --> [2, 4, 6]

 
cap = capital(d,'Germany') # if the 'Germany' is added; country is overwritten in function and will print out Germany's captial. 
    # if not, it will be printing out the default values.

print(cap) # if function is run, program will receive error. needs two arguemnts( country and dictionary) but only receives one.

#NOTE: python documentatino that is mentioned. search up python documentation. Can look at what is accepted or not. 


#######################################################################################################################################


#New lesson: Slicing. 

#what is it?
    #specifically for lists and strings.
    #basically slicing something at certain points. 

    #i.e.:

st = str(input('Enter the list of names: '))
names= st.split()

#slicing:

slice1 = names[2:5] # slicing the list from index a to index b; from index 2 to index 5.

# names = names[2:5] can change and give a new slice of the list. if not given, then it will just print normally. don't need to directly make a new variable for it
print(names)
print(slice1)

#input: rahim john mike danny hannah susan patrick.
#output: prints out the list and then puts out the slice:
#output: mike, danny, hannah.
#      element 2 - 4

slice2 = names[1:6:2] # has a start, end and a step as well. 
    #prints out values of 1, 3, 5
    #outputs: john, danny, james.

sliec3 = names[7:3:-2] # slice function goes backwards; step back by 2. from position 7 to 3. 

slice4 = names[::] # if this is printed; nothing will happen. just prints the list.

rev_slice = names[::-1] #just prints out the list, but in reverse. must make it so the step is -1.
    #more efficient way to reverse print your lists. 

slice5 = names[-1: -6: -3] #printing of names backwards. (-) value represents the indexes from a reverse perspective. step also helps to move backwards.

part = names[0][1:4] #prints a part of the name at index 0: i.e. Rahim.
    #outputs ahi. letter 4 is exclusive. 'm' is not included.
    # can help with boring words. 

    #EVERYTHING DONE WITH SLICING CAN BE DONE WITH A FOR LOOP. [LIST IN RANGE AND THEN KEEP ADDING THEM TO NEW LIST]


#########################################################################3

#Two dimensional lists.
    #list of lists.

mat1 = []

n = int(input('Enter the number of rows: '))
m = int(input('Enter the number of columns: '))

for i in range( 0,n):
    row = []
    for j in range(0, m):
        print('Enter element at [', i + 1, ',', j + 1, ']', end = '= ')
        x = int(input(''))
        row.append(x)

    mat1.append(row)

mat2 = []


for i in range(0,n):
    for j in range(0,m):
        print(mat1[i][j], end = ' ')
    print('')

summat = mat1
for i in range(0,n):
    for j in range(0,m):
        summat[i][j] = summat[i][j] + mat2[i][j]


#ie if we went back to names:
#i.e. names[5] = james:
    #names[5][2] = 'm'
    #first index indicates name. second indicates the character in the name.



