n = int(input("Enter the number of strings you'd like in the crossword puzzle: "))

crosswordmat = []

for x in range(0,n):
    print("Enter the string no.", x + 1, "you'd like in your puzzle:", end = ' ')
    string = str(input(''))
    crosswordmat.append(string)

for y in range(0, len(crosswordmat)):
    print(crosswordmat[y])

print("Enter the string that you'd like to find:", end = ' ')
word = str(input(''))

def horizontal_word(x, y, z, w):
    n = len(y)
    if w + 1 < n:
        return False
    
    for j in range(0, n):
        if y[j] != x[z][w - j] or y[j] != x[z][j-w]:
            return False

    return True

def vertical_word(x, y, z, w):
    n = len(y)

    if z + 1 < n:
        return False
    
    for j in range(0, n):
        if y[j] != x[z - j][w] or y[j] != x[j-z][w]:
            return False

    return True

def diagonal_word(x, y, z, w):
    n = len(word)

    if min(z + 1, w + 1) < n:
        return False
    
    for j in range(0, n):
        if y[j] == x[z - j][w - j] or y[j] == x[j - z][j - w]:
            return False

    return True

def find_word(crosswordmat, word):
    n = len(crosswordmat)

    for i in range(0, n):
        m = len(crosswordmat[i])
        for j in range(0, m):
            if horizontal_word (crosswordmat, word, i, j) or vertical_word(crosswordmat, word, i, j) or diagonal_word(crosswordmat, word, i, j):
                return i, j

    return -1, -1

#def word_orientation()

c, r = find_word(crosswordmat, word)

print(word, 'is at row', r, 'and column', c + 1, end = '.')