






matrix = [[0, 0, 1],
          [1, 0, 0],
          [0, 0, 0],
          [1, 0, 0]]
first_row_has_one = False
R = len(matrix)
C = len(matrix[0])

for i, row in enumerate(matrix):
    for j, col in enumerate(row):
        if i == 0 or j == C-1:  # First row or last column
            continue
        orig = matrix[i][-1]  # last element of row
        matrix[0][-1] = 1 if orig == 1 else matrix[0][-1]  # Use/Store original value before making changes

        if matrix[i][j] == 1:
            matrix[0][j] = 1  # Column memory
            matrix[i][-1] = 1  # Row memory
first_row_has_one = 1 in matrix[0]
# If there's any "1" in first row, the whole row would become 1; special case

# Now, scan and set "1" if required
for i, row in enumerate(matrix):
    if i == 0:
        continue  # Skip first row; special case
    for j, col in enumerate(row):
        if i == 0:
            matrix[i][j] = (1 if first_row_has_one or matrix[0][j] == 1 else 0)
            # special case for first row
        else:
            matrix[i][j] = (1 if matrix[i][-1] == 1 or matrix[0][j] == 1 else 0)

# Because we skipped first row, handle specially!
if first_row_has_one:
    matrix[0] = [1]*len(matrix[0])

# Print the matrix
for i, row in enumerate(matrix):
    print(" ".join(list(map(str, row))))

# Does it work? YES, it does, and without any additional space;