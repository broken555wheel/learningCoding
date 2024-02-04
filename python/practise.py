def gauss_jordan_elimination(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    for i in range(rows):
        for j in range(i, rows):
            if matrix[j][i] != 0:
                matrix[i] = matrix[j]
                matrix[j] = matrix[i]
                break
        pivot = matrix[i][j]
        if pivot != 0:
            matrix[i] = [element / pivot for element in matrix[i]]

        for k in range(rows):
            if k != i:
                factor = matrix[k][i]
                matrix[k] = [element_k - factor * element_i for element_i, element_k in zip(matrix[i], matrix[k])]
    return matrix

example = [
    [1, 2, -1, -2],
    [2, 7, -8, -16],
    [0, -2, 2, 2]
]
solution_matrix = gauss_jordan_elimination(example)
solution = [[row[-1]] for row in solution_matrix]
for x in solution:
    var = solution.index(x)+1
    print(f'x{var} = {x}')