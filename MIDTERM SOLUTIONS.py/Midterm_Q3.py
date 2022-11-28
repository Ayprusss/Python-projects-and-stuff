import math

def repeat(part, n):
    strep = ''

    for i in range(0, n):
        strep = strep + part

    return strep

def boring(word):
    n = len(word)
    m = n // 2

    for i in range(1, m + 1):
        if n % i == 0:
            part = ''
            for j in range(0, i):
                part = part + word[j]

            if repeat(part, n // i) == word:
                return True

    return False

# main part of the program
st = input('Enter the words: ')
words = st.split()
n = len(words)

for i in range(0, n):
    if boring(words[i].lower()):
        print(words[i], end = ' ')








