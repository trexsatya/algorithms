

board = [[0, 100] for _ in range(31)]

# Populate snakes and ladders
board[7][0] = 9
board[8][0] = 18
# board[16][0] = 26
# board[20][0] = 29
# board[27][0] = 1
# board[21][0] = 9

print(board[29])

board[1][1] = 0
# Second info in cell is the minimum steps to reach there
for i in range(1, 30):
    for j in range(1, 7):  # possible dice outcomes
        if i+j > 30:
            continue
        target = board[i+j]
        target[1] = min(target[1], board[i][1]+1)
        if target[0] > 0:  # A ladder
            target = board[target[0]]
            target[1] = min(target[1], board[i][1]+1)

for i, val in enumerate(board[1:]):
    print(i+1, val)

#