def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	import numpy as np
	m = np.array(matrix)
	e = np.linalg.eigvals(m)
	return e