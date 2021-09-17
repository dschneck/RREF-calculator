#!/usr/bin/env python3

'''
	I'm using the algorithm from here: 
	https://www.math.purdue.edu/~shao92/documents/Algorithm%20REF.pdf

'''

import sys
from matrix import Matrix
from getInput import Input

class RREF:
	def __init__(self, A: Matrix):
		A.printMatrix()
		pivot = 0

		for i in range(A.m):
			if pivot > A.n-1 or pivot > A.m-1:
				break

			row, col = self.__findNonZero(A, pivot)
			if (row, col) == (-1, -1):
				break

			if (pivot, pivot) != (row, col):
				if row == A.m-1:
					for j in range(A.m-1, 0, -1):
						if A.matrix[j][pivot] == 0:
							A.matrix[j], A.matrix[row] = self.__interchange(A, row, j)
							row = j
							break
				
				else:
					for j in range(row+1, A.m):
						if A.matrix[j][pivot] != 0:
							A.matrix[j], A.matrix[row] = self.__interchange(A, row, j)
							row = j
							break

			for j in range(A.m):
				if j != pivot and A.matrix[j][pivot] != 0 and A.matrix[pivot][pivot] != 0: 
					A.matrix[j] = self.__rowSum(A, j, row, -1*A.matrix[j][pivot]/A.matrix[pivot][pivot]) 
			if A.matrix[pivot][pivot] != 0:
				val = 1/A.matrix[pivot][pivot]
				A.matrix[pivot] = self.__scale(A, pivot, val)

			pivot = pivot + 1

		A.printMatrix()
		self.__validate(A)

	@staticmethod
	def __validate(A: Matrix):
		flag = 0 # changes if an error is detected

		for i in range(A.m-1):
			if A.matrix[i][i] != 1:
				flag = 1
				break

		if flag == 0:
			print("This is a valid RREF")
		else:
			print("This is NOT a valid RREF")


	@staticmethod
	def __findNonZero(A: Matrix, offset: int):
		for i in range(offset, A.m):
			for j in range(A.n):
				if A.matrix[i][j] != 0:
					return i, j
		return -1, -1

	#----ELEMENTARY ROW OPERATIONS----#
	@staticmethod
	def __interchange(A: Matrix, row1: int, row2: int):
		print(A.matrix[row1], A.matrix[row2], sep="\n")
		return A.matrix[row1], A.matrix[row2]

	@staticmethod
	def __scale(A: Matrix, row: int, scalar: float):
		tempRow = A.matrix[row]

		for i in range(A.n):
			tempRow[i] = tempRow[i] * scalar
		return tempRow
		
	@staticmethod
	def __rowSum(A: Matrix, row1: int, row2: int, scalar: float):
		tempRow = A.matrix[row1]
		tempRow2 = A.matrix[row2]

		for i in range(A.n):
			tempRow[i] = tempRow[i] + scalar * tempRow2[i]

		return tempRow



if __name__ == "__main__":
	if len(sys.argv) == 1:
		x = Input.getInput()
		y = Matrix(x[0], x[1], x[2])
		z = RREF(y)
	else:
		x = Input.getInput(sys.argv[1])
		y = Matrix(x[0], x[1], x[2])
		z = RREF(y)
	#A = Matrix([[0, 1, 0, 3], [1, 0, 0, 2], [0, 0, 1, 4]], 3, 4)
	#B = Matrix([[2.0, 8.0, 4.0, 2.0], [2.0, 5.0, 1.0, 5.0], [4.0, 10.0, -1.0, 1.0]], 3, 4)
	#C = Matrix([[1],[9]], 2, 1)
	#C.printMatrix()
	#D = Matrix([[0,1], [0,0], [5,9]], 3, 2)

	#x = RREF(A)
	#y  = RREF(B)
	#z = RREF(C)
	#r = RREF(D)
