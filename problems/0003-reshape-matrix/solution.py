import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	a_rows = len(a) # Number of rows
	a_columns = len(a[0]) # Number of columns 
    m,n = new_shape[0],new_shape[1] # Rows and Columns for the reshaped reshape_matrix
	if a_rows *a_columns != m*n :
		return []
	else : 
		arr = np.array(a)
		arr_reshaped = arr.reshape(m,n)
		reshaped_matrix = arr_reshaped.tolist()

		return reshaped_matrix