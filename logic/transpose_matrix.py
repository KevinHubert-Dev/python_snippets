def transpose_matrix_logic(m):
    a, b = len(m), len(m[0])
    t_mat = [[0] * a for _ in range(b)]
    
    for i in range(a):
        for j in range(b):
            t_mat[j][i] = m[i][j]
    
    return t_mat

# 1.) Let us refactor the code to use meaningful names
# 2.) This code needs documentation. Pydoc and inline