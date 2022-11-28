u = int(input('How many numbers do you want in list #1?: '))
listu = []
unionlist = []
for x in range(0, u):
    print('input value', x + 1,':', end = '')
    val1 =int(input(''))
    listu.append(val1)
    unionlist.append(val1)
a = int(input('How many numbers do you want in list #2?: '))
#############################################################
#Anthony Le; 300287511
#Assignment 1, Question 8
# october 21, 2022

#############################################################
list1 = []
for y in range(0, a):
    print('input value',y + 1,':', end = '')
    val2 = int(input(''))
    list1.append(val2)
b = int(input('How many numbers do you want in list #3?: '))
list2 = []
for z in range(0, b):
    print('input value:', z + 1,':', end = '')
    val3 = int(input(''))
    list2.append(val3)
# A Union B: 
unionrange = len(listu)
for l in range (0, unionrange):
    unionnum = listu[l]
    if list1.count(unionnum) == 0 and list2.count(unionnum) == 0: # number does not exist in both lists; is not A union B
        unionlist.remove(unionnum)
        unionrange = len(unionlist)
unionlist.sort()
print('A Union B =',unionlist)
l1r=len(list1)
l2r=len(list2)
# A intersection B:
same = []
for m in range(0,l1r):
    for n in range(0, l2r):
        if list1[m] == list2[n]:
            same.append(list1[m])
            break
same.sort()
print('A Intersection B =', same)
# A - B:
onlya = []
l1r=len(list1)
l2r=len(list2)
for ar in range(0,l1r):
    aminb = list1[ar]
    if list2.count(aminb) == 0 and onlya.count(aminb) == 0:
        onlya.append(aminb)
if len(onlya) > 1:
    aminb.sort()
print('A - B =',onlya)
# B - A:
onlyb = []
for cr in range(0,l2r):
    bmina = list2[cr]
    if list1.count(bmina) == 0 and onlyb.count(bmina) == 0:
        onlyb.append(bmina)
if len(onlyb) > 1:
    onlyb.sort()
print('B - A =', onlyb)
# A complement: all elements in U bot not in A:
acomp = []
for er in range(0,len(listu)):
    aonly = listu[er]
    if list1.count(aonly) == 0 and acomp.count(aonly) == 0:
        acomp.append(aonly)
if len(acomp) > 1:
    acomp.sort()
print('A Complement =', acomp)
# B Complement:
bcomp = []
for gr in range(0,len(listu)):
    bonly = listu[gr]
    if list2.count(bonly) == 0 and bcomp.count(bonly) == 0:
        bcomp.append(bonly)
if len(bcomp) > 1:
    bcomp.sort()
print('B Complement =', bcomp)
# A ^ B:
aplusb = []
for hr in range(0,len(listu)):
    unique = listu[hr]
    if list1.count(unique) > 0 and list2.count(unique) == 0 and aplusb.count(unique) == 0: # finding unique numbers in list 1. in listu but not shared with list 2.
        aplusb.append(unique)
    if list1.count(unique) == 0 and list2.count(unique) > 0 and aplusb.count(unique) == 0:
        aplusb.append(unique)
if len(aplusb) > 1:
    aplusb.sort()
print('A ^ B =', aplusb)