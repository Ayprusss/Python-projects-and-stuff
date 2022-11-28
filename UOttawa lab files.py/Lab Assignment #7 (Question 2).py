dict = {}

num = int(input('Enter how many playes to teams would you want to input?: '))

for x in range(num):
    name = str(input('Enter player name: '))
    team = str(input('Enter team name: '))
    dict[name] = team

print(dict)

newDict = {}

values = set(dict.values())

print(values)

for n in values:
    newDict[n] = [k for k in dict.keys() if dict[k] == n]


print(newDict)
