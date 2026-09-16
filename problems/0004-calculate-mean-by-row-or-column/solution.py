def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	import numpy as np

	matrix = np.array(matrix)

	if mode == 'row':
		means = np.mean(matrix, 1)
	if mode == 'column':
		means = np.mean(matrix, 0)

	return means