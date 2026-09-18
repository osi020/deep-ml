def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here 
    matrix_rows = len(a) # number of matrix rows
    matrix_columns = len(a[0]) # number of columns rows  
    transpose_matrix_result = [] 
    for j in range (matrix_columns): # ALLONS DE 0 VERS 3
        temp_list = []
        for i in range (matrix_rows) : # allons de 0 vers 2 
            temp_list.append(a[i][j])
        transpose_matrix_result.append(temp_list)
    return  transpose_matrix_result

           


    