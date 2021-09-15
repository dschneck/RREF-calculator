#!/usr/bin/env python3

'''
	I'm using the algorithm from here: 
	https://www.math.purdue.edu/~shao92/documents/Algorithm%20REF.pdf

'''

import sys
from matrix import Matrix

class RREF:
	def __init__(self, A: Matrix):
		# Step 1
		print("Finding the RREF for the following matrix\n")
		A.printMatrix()
		pivot = 0

		# Step 2 - 5
		for i in range(A.m):
			row, col = self.__findNonZero(A, pivot)
			print("row, col ", (row, col))

			if (pivot, pivot) != (row, col):
				print("not in the", pivot, "th position", row, col)
				for j in range(row+1, A.n-1):
					if A.matrix[j][col] != 0:
						A.matrix[j], A.matrix[row] = self.__interchange(A, row, j)
						A.printMatrix()
						row = j
						break
			else:
				print("it was in the right pivot position")


			
			for j in range(A.n-1):
				if j != pivot: 
					A.matrix[j] = self.__rowSum(A, j, row, -1*A.matrix[j][pivot]/A.matrix[row][pivot]) 
			print("After row suming")
			A.printMatrix()
			
			A.matrix[row] = self.__scale(A, pivot, 1/A.matrix[pivot][pivot])
			print("New matrix after scaling is: ")
			A.printMatrix()

			# get ready for the next pass
			pivot = pivot + 1
			print("pivot ", (pivot,pivot))

		
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
	def __findNonZero(A: Matrix, offset: int):
		for i in range(offset, A.m):
			for j in range(A.n):
				if A.matrix[i][j] != 0:
					return i, j

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
	#print(sys.argv[1])
	#A = Matrix([[1, 0, 0, 2], [0, 1, 0, 3], [0, 0, 1, 4]], 3, 4)
	B = Matrix([[2.0, 8.0, 4.0, 2.0], [2.0, 5.0, 1.0, 5.0], [4.0, 10.0, -1.0, 1.0]], 3, 4)
	#C = Matrix([[1],[9]], 2, 1)
	#C.printMatrix()

	#x = RREF(A)
	y  = RREF(B)
	#z = RREF(C)

