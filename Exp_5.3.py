# 5.3 Matrix Operations (list of lists)


def read_matrix(filename):
    matrix = []
    with open(filename, "r") as f:
        for line in f:
            
            row = [int(x) for x in line.split()]
            matrix.append(row)
    return matrix



matrix_a = read_matrix("matrix1.txt")
matrix_b = read_matrix("matrix2.txt")


print("Matrix A = ")
for row in matrix_a:
    print(row)

print("\nMatrix B = ")
for row in matrix_b:
    print(row)



rows = len(matrix_a)
cols = len(matrix_a[0])

result_add = []

for i in range(rows):
    new_row = []
    for j in range(cols):
        sum_val = matrix_a[i][j] + matrix_b[i][j]
        new_row.append(sum_val)
    result_add.append(new_row)

result_sub = []

for i in range(rows):
    new_row = []
    for j in range(cols):
        sub_val = matrix_a[i][j] - matrix_b[i][j]
        new_row.append(sub_val)
    result_sub.append(new_row)

transpose = []

for j in range(cols):
    new_row = []
    for i in range(rows):
        new_row.append(matrix_a[i][j])
    transpose.append(new_row)


print("\n--- Matrix Addition ---")
for row in result_add:
    print(row)


print("\n--- Matrix Substraction ---")
for row in result_sub :
    print(row)
    
print("\n--- Transpose of Matrix A ---")
for row in transpose:
    print(row)