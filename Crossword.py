
def match_horizontal(puzzle, word, r, c):
    n = len(word)

    #Check if we have enough characters
    if c + 1 < n:
        return False

    # r = 3, c = 4, word = find
    # j = 0, word[0] = f == puzzle[3][4] = f
    # j = 1, word[1] = i == puzzle[3][3] = i
    # j = 2, word[2] = n == puzzle[3][2] = n
    # j = 3, word[3] = d == puzzle[3][1] = d
    
    for j in range(0, n):
        if word[j] != puzzle[r][c - j]:
            return False

    return True
    
def match_vertical(puzzle, word, r, c):
    n = len(word)

    #Check if we have enough characters
    if r + 1 < n:
        return False

    # r = 5, c = 4, word = find
    # j = 0, word[0] = f == puzzle[5][4] = f
    # j = 1, word[1] = i == puzzle[4][4] = f at this check we return False
    # j = 2, word[2] = n == puzzle[3][4] = d
    # j = 3, word[3] = d == puzzle[2][4] = s
    
    for j in range(0, n):
        if word[j] != puzzle[r - j][c]:
            return False

    return True

def match_diagonal(puzzle, word, r, c):
    n = len(word)

    #Check if we have enough characters
    if min(r + 1, c + 1) < n:
        return False

    # r = 5, c = 4, word = find
    # j = 0, word[0] = f == puzzle[5][4] = f
    # j = 1, word[1] = i == puzzle[4][3] = a at this check we return False
    # j = 2, word[2] = n == puzzle[3][2] = n
    # j = 3, word[3] = d == puzzle[2][1] = k
    
    for j in range(0, n):
        if word[j] != puzzle[r - j][c - j]:
            return False

    return True

def find_word(puzzle, word):
    n = len(puzzle)

    for i in range(0, n):
        m = len(puzzle[0])
        for j in range(0, m):
            if match_horizontal(puzzle, word, i, j) or match_vertical(puzzle, word, i, j) or match_diagonal(puzzle, word, i, j):
                return i, j

    return -1, -1

n = int(input('Enter the number of rows: '))

puzzle = []

for i in range(0, n):
    print('Enter row number', i + 1, 'of the puzzle:', end = ' ')
    row = input('')
    puzzle.append(row)

print('The puzzle:')
for i in range(0, n):
    print(puzzle[i])

word = input('Enter the word to look in the puzzle: ')

r, c = find_word(puzzle, word)

print(word, 'is at row', r + 1, 'and column', c + 1, end = '.')







