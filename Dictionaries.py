
#empty dictionary
d1 = {}

#mapping an English word to a French word
d2 = {'apple': 'pomme', 'desk': 'pupitre', 'chair': 'chaise' }

#mapping an English word to a list of French words
d3 = {'apple': ['pomme'], 'chair': ['chaise'], 'desk': ['pupitre'],
      'work': ['devoir', 'travaille']}

#print(d3)
#print(d2['screen'])

# The number of elements in a dictionary
n = len(d2)

#checking if an element is in the dictionary
if 'chair' in d2:
    print(d2['chair'])

#changing a word in a dictionary
d2['apple'] = 'pome'

#adding a new word to the dictionary
d2['screen'] = 'ecran'

#looping over elements in a dictionary
for x in d2:
    print(x, '=', d2[x])

#adding to a dictionary when we are dealing with a list
#d3['screen'] = [ ]
#d3['screen'].append('ecran')

#adding to a dictionary when we are dealing with a list(another way)
d3['screen'] = ['ecran']

#adding to the list of meanings of 'desk'
d3['desk'].append('xyz')
print(d3)

'''
print(d2['apple'])
print(d2)
'''
print('******')

#Going over the keys(the first part of the pair) of the dictionary
for x in d2.keys():
    print(x)
    
print('******')
#Going over the values(the second part of the pair) of the dictionary
for x in d2.values():
    print(x)

print('******')
#printing elements in pairs
print(d2.items())







