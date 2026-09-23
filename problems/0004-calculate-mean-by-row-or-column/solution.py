def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	rows = len(matrix)
	columns = len(matrix[0])
	result = []
	if mode == 'column' : 
		for j in range(columns) :
			sum = 0 
			for i in range(rows) : 
				sum = sum + matrix[i][j] 
			mean = sum / rows
			result.append(mean)
	if mode == 'row' : 
		for i in range(rows) :
			sum = 0
			for j in range(columns) : 
				sum = sum + matrix[i][j]
			mean = sum / columns
			result.append(mean)


	return result