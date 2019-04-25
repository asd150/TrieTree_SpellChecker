import numpy as np


def diff(a, b):
	if a == b:
		return 0
	else:
		return 1


def edit_distance(x, y):
	m = len(x)
	n = len(y)
	E = np.zeros((m+1, n+1))
	for i in range(m+1):
		E[i][0] = i
	for j in range(n+1):
		E[0][j] = j
	for i in range(1, m+1):
		for j in range(1, n+1):
			E[i][j] = min(1+E[i-1][j], 1+E[i][j-1], diff(x[i-1], y[j-1])+E[i-1][j-1])
	print(E)
	return E[m][n]


if __name__ == '__main__':
	x = 'exponential'
	y = 'polynomial'
	print(int(edit_distance(x,y)))