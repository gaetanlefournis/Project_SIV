def sudoku(mat):
    size = len(mat)
    for i in range(size):
        for j in range(size):
            if mat[i][j] != 0:
                if mat[i].count(mat[i][j]) > 1 or [mat[x][j] for x in range(size)].count(mat[i][j]) > 1:
                    return False
                if size == 4:
                    start_row, start_col = 2 * (i // 2), 2 * (j % 2)
                    square = [mat[start_row + l][start_col + m] for l in range(2) for m in range(2)]
                    return (len(set(square)) == len(mat))
        if size == 9:
            valeurs = [0] * 10
            start_row = (i // 3) * 3
            start_col = (i % 3) * 3
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if mat[i][j] != 0:
                        if valeurs[mat[i][j]] == 1:
                            return False
                        valeurs[mat[i][j]] = 1
    return True

# Exemple de grille 4x4
grid_4x4 = [
    [1, 2, 3, 4],
    [3, 4, 2, 1],
    [2, 1, 4, 3],
    [4, 3, 1, 2]
]

grid_9x9 = [
    [8,1,3,9,2,5,7,4,6],
    [9,5,6,8,4,7,3,1,2],
    [4,7,2,3,6,1,8,9,5],
    [6,2,4,7,1,9,5,3,8],
    [7,9,5,6,3,8,4,2,1],
    [3,8,1,4,5,2,9,6,7],
    [2,3,8,1,7,4,6,5,9],
    [5,4,9,2,8,6,1,7,3],
    [1,6,7,5,9,3,2,8,4]
]

result_4x4 = sudoku(grid_4x4)
result_9x9 = sudoku(grid_9x9)
print("La grille 9x9 est valide :", result_9x9)
