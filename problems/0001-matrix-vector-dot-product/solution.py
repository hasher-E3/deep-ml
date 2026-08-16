def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	if (len(a[0]) != len(b)) or len(a) == 0 or len(b)==0:
		return -1
	out= []
	for i in range(len(a)):
		s = 0
		for j in range(len(b)):
			 s += a[i][j] * b[j]
		out.append(s)
	return out
