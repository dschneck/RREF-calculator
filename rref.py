#!/usr/bin/env python3

'''
	I'm using the algorithm from here: 
	https://www.math.purdue.edu/~shao92/documents/Algorithm%20REF.pdf


'''
import sys

class Matrix:
	def  __init__(self, matrix: [[int]], m: int, n: int):
		self.matrix = matrix
		self.m = m
		self.n = n

	def printMatrix(self):
		for i in range(self.m):
			for j in range(self.n):
				print(self.matrix[i][j], end=" ")
			print("\n")

class RREF:
	def __init__(self, A: Matrix):
		# Step 1
		print("Finding the RREF for the following matrix\n")
		A.printMatrix()

		# Step 2
		self.__findNonZero(A)

		
		# final check
		self.__validate(A)

	@staticmethod
	def __validate(A: Matrix):
		flag = 0 # changes if an error is detected

		for i in range(A.m):
			if A.matrix[i][i] != 1:
				flag = 1
				break

		if flag == 0:
			print("This is a valid RREF")
		else:
			print("This is NOT a valid RREF")


	@staticmethod
	def __findNonZero(A: Matrix):
		for i in range(A.m):
			for j in range(A.n):
				if A.matrix[i][j] != 0:
					return i, j

	# ELEMENTARY ROW OPERATIONS #
	@staticmethod
	def __interchange(A: Matrix, row1: int, row2: int):
		return A.matrix[row1], A.matrix[row2]

	@staticmethod
	def __scale(A: Matrix, row: int, scalar: int):
		tempRow = A.matrix[row]

		for i in range(A.n):
			tempRow[i] = tempRow[i] * scalar
		return tempRow
		
	@staticmethod
	def __rowSum(A: Matrix, row1: int, row2: int, scalar: int):
		tempRow = A.matrix[row1]
		tempRow2 = A.matrix[row2]

		for i in range(A.n):
			tempRow[i] = tempRow[i] + scalar * tempRow2[i]

		return tempRow



if __name__ == "__main__":
	#print(sys.argv[1])
	A = Matrix([[1, 0, 0, 2], [0, 1, 0, 3], [0, 0, 1, 4]], 3, 4)
	B = Matrix([[2, 0, 1], [0, 1, 2]], 2, 3)

	x = RREF(A)
	y  = RREF(B)

