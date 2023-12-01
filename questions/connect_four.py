import random

# Define the dimensions of the Connect Four game board
rows = 6
cols = 7

player_1_row_win = '1' * 4
player_2_row_win = '2' * 4
gameOver = False

# Create an empty game board
connect_four_board = [[0 for _ in range(cols)] for _ in range(rows)]
# print(connect_four_board)
# print([[0] * 7 for i in range(6)])
# Randomly populate the game board with player pieces (1 and 2) and empty spaces (0)
for row in range(rows):
    for col in range(cols):
        # Generate a random number to represent player pieces (1 or 2) or empty space (0)
        random_value = random.choice([0, 1, 2])
        connect_four_board[row][col] = random_value

def column_or_row_win(entry):
    if player_1_row_win in entry:
        return {"game_over": True, "msg": "player 1 won!"}
    elif player_2_row_win in entry:
        return {"game_over": True, "msg": "player 2 won!"}
    else:
        return {"game_over": False, "msg": "game still in progress"}

for row in connect_four_board:
    print(row)

# # Print the random Connect Four game board
for row in connect_four_board:
    str_array = list(map(str, row))
    current_row = ''.join(str_array)
    result = column_or_row_win(current_row)
    if result['game_over'] is True:
        print(result['msg'])
        gameOver = True
        break
# check columns
print(connect_four_board)
for col in zip(*connect_four_board):
    column = list(col)
    data = ''.join(str(c) for c in column)
    result = column_or_row_win(data)
    if result['game_over'] is True:
        print(result['msg'])
        gameOver = True
        break

if not gameOver:
    print("Tie!")
    
'''
matrix = [
    [1, 2, 3, 4, 5, 6, 7],
    [8, 9, 10, 11, 12, 13, 14],
    [15, 16, 17, 18, 19, 20, 21],
    [22, 23, 24, 25, 26, 27, 28],
    [29, 30, 31, 32, 33, 34, 35],
    [36, 37, 38, 39, 40, 41, 42]
]

# Get every row
print("Rows:")
for row in matrix:
    print(row)

# Get every column
print("\nColumns:")
for col in zip(*matrix):
    print(list(col))

# Get main diagonal (this is not applicable for non-square matrices, but let's get the diagonal from the top-left to the bottom-right as far as possible)
print("\nMain Diagonal:")
main_diagonal = [matrix[i][i] for i in range(min(len(matrix), len(matrix[0])))]
print(main_diagonal)

# Get secondary diagonal (top-right to bottom-left, as far as possible)
print("\nSecondary Diagonal:")
secondary_diagonal = [matrix[i][len(matrix[0]) - 1 - i] for i in range(min(len(matrix), len(matrix[0])))]
print(secondary_diagonal)

'''