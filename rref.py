#!/usr/bin/env python3

'''
	Inspiration for the solution came from the following link:
	https://www.math.purdue.edu/~shao92/documents/Algorithm%20REF.pdf

'''

import sys
from matrix import Matrix
from getInput import Input

class RREF:
	def __init__(self, A: Matrix):
		print("Original matrix:")
		A.printMatrix()
		pivot = 0

		for i in range(A.m):
			if pivot > A.n-1 or pivot > A.m-1:
				break

			row, col = self.__findNonZero(A, pivot)
			if (row, col) == (-1, -1): # case where there are no more nonzero values
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

		print("RREF matrix: ")
		A.printMatrix()
		self.__validate(A)

	@staticmethod
	def __validate(A: Matrix):
		flag = 0 # changes if an error is detected

		if A.n != 1:
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

	@staticmethod
	def __interchange(A: Matrix, row1: int, row2: int):
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
	if len(sys.argv) == 1: 				# input from command line
		x = Input.getInput()
		y = Matrix(x[0], x[1], x[2])
		z = RREF(y)
	else: 								# input from file
		x = Input.getInput(sys.argv[1])
		y = Matrix(x[0], x[1], x[2])
		z = RREF(y)
