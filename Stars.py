# *********
# ****
# ************

for i in range( 1,6):
    for j in range(i):
    print ('*', end = '')


        # *
        # **
        # ***

for i in range(1,6):
    for j in range(1, i + 1):
        print('*', end = '')
    print('')



# *
# **
# ***
# ****
# *****

for i in range(1,6):
    for j in range(1, 6 - i + 1):
        print('*', end = '')
    print('')

            
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1

# pascal's triangle

