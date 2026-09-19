import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	a_rows = len(a) # Number of rows
	a_columns = len(a[0]) # Number of columns 
    m,n = new_shape[0],new_shape[1] 
	a_flatten = [] 
	if (a_rows * a_columns) != (m*n) : return []
	for i in range(a_rows) : 
		for j in range(a_columns) : 
			a_flatten.append(a[i][j])

	


	return a_flatten