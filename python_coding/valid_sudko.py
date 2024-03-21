def rotate(matrix):
    n = len(matrix)
    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()

# Example usage
matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

rotate(matrix)
print(matrix)
