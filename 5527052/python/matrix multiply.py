def matrix_multiply(matrix1, matrix2):
    rows_matrix1 = len(matrix1)
    cols_matrix1 = len(matrix1[0])
    rows_matrix2 = len(matrix2)
    cols_matrix2 = len(matrix2[0])

    if cols_matrix1 != rows_matrix2:
        raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix.")
    result = [[0 for _ in range(cols_matrix2)] for _ in range(rows_matrix1)]

    for i in range(rows_matrix1):
        for j in range(cols_matrix2):
            for k in range(cols_matrix1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[7, 8], [9, 10], [11, 12]]

product_matrix = matrix_multiply(matrix1, matrix2)
print("Product of the matrices:")
for row in product_matrix:
    print(row)
