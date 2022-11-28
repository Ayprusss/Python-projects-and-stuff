#NOTES; 


n = int(input('Enter the number of rows: '))
puzzle = []
for i in range(0,n):
    print('Enter row number', i + 1, ' of the puzzle: ', end = ' ')
    row = input('')
    puzzle.append(row)

print('the puzzle:')
for i in range(0,n):
    print(puzzle[i])

word = input('Enter the word to look in the puzzle: ')


def match_horizontal(puzzle, word, r, c):
    n = len(word)

    #check if we have enough characters:

    if c + 1 < n:
        return False
    
    # r = 3, c = 4, word = find
    #j = 0
    for j in range(0,n):
        if word[j] != puzzle[r][c-j]:
            return True

def match_diagonal (puzzle, word, r, c):
    n = len(word)

    #check if there are enough characters
    if r + 1 < n:
        return False
    
    for j in range(0,n):
        if word[j] != 