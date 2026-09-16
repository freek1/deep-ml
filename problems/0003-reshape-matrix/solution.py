import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	import numpy as np

	a = np.array(a)
	ns = np.array(new_shape)
	
	if a.size != np.prod(ns):
		return []
	
	rm = a.reshape(new_shape)

	return rm.tolist()