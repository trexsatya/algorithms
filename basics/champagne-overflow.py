R = 6  # Number of rows we are interested in
water = 9



# Notice that although it looks like a tree, we do not actually
# need a tree. We can simply use a matrix
matrix = [[0] * i for i in range(1, R + 3)]

# Edge means leftmost or rightmost glasses
# Inner means glasses between them

# Step-1: Find which row/level will be completely filled,
#  it is 3rd row in the example on the left side
last_row_full = 0
water_filled = 0
X = water
for i in range(1, R+1):
    if (X-1)/2 < 0:
        break  # It means last row found
    # We are calculating water flowing to the Edge glasses
    X = (X-1)/2
    last_row_full = i
    water_filled += i

water_left = water - water_filled
num_inner_glasses = (last_row_full - 2)

if num_inner_glasses > 0:
    overflowing_from_inner_glasses = (water_left - 4*X) / (2*num_inner_glasses)
#     To prevent math divide by zero error

# Step-2: Find out how much of water will be overflown
#  from the Inner glasses from that last filled row
edge_flow = X
inner_flow = overflowing_from_inner_glasses

row = last_row_full
glasses = row
for i in range(glasses):
    if i == 0 or i == glasses-1:  # First or las
        matrix[row + 1][i] += edge_flow
        matrix[row + 1][i + 1] += edge_flow
    else:
        matrix[row + 1][i] += inner_flow
        matrix[row + 1][i + 1] += inner_flow

for r in range(row+1, R):
    for j in range(r):
        if matrix[r][j] > 1:
            matrix[r + 1][j] += (matrix[r][j] - 1)/2
            matrix[r + 1][j + 1] += (matrix[r][j] - 1)/2



for row in enumerate(matrix):
    print(row)

# Remember that all the glasses till 3rd row will
# contain 1 Litre water, even though matrix has 0 in them