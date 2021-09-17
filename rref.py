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
			if pivot > A.n-1 or pivot > A.m-1:
				break

			row, col = self.__findNonZero(A, pivot)
			if (row, col) == (-1, -1):
				break

			print("row, col ", (row, col))

			if (pivot, pivot) != (row, col):
				print("not in the", pivot, "th position", row, col)
				if row == A.m-1:
					print("got here")
					for j in range(A.m-1, 0, -1):
						print("j is ", j)
						if A.matrix[j][pivot] == 0:
							print(A.matrix[j][pivot])
							A = self.__interchange(A, row, j)
							#A.matrix[j], A.matrix[row] = self.__interchange(A, row, j)
							'''
							temp = A.matrix[j].copy()
							temp2 = A.matrix[row].copy()

							for k in range(A.n):
								A.matrix[j][k] = temp2[k]
								A.matrix[row][k] = temp[k]
							'''
							print("After the interchange")
							A.printMatrix()
							row = j
							break
				
				else:
					for j in range(row+1, A.m):
						if A.matrix[j][pivot] != 0:
							A = self.__interchange(A, row, j)
							#A.matrix[j], A.matrix[row] = self.__interchange(A, row, j)
							'''
							temp = A.matrix[j].copy()
							temp2 = A.matrix[row].copy()

							for k in range(A.n):
								A.matrix[j][k] = temp2[k]
								A.matrix[row][k] = temp[k]
							'''
							print("After the interchange")
							A.printMatrix()
							row = j
							break
			#else:
				#print("it was in the right pivot position")

			for j in range(A.m):
				#print("j: ", A.matrix[j])
			#	print("pivot: ", pivot)
			#	print("j: ", j)
				if j != pivot and A.matrix[j][pivot] != 0 and A.matrix[pivot][pivot] != 0: 
					A.matrix[j] = self.__rowSum(A, j, row, -1*A.matrix[j][pivot]/A.matrix[pivot][pivot]) 
			#print("After row suming")
			#A.printMatrix()
			
			if A.matrix[pivot][pivot] != 0:
				val = 1/A.matrix[pivot][pivot]
			#	print("the scaling factor ", val)
				A.matrix[pivot] = self.__scale(A, pivot, val)
			#	print("New matrix after scaling is: ")
				#A.printMatrix()

			# get ready for the next pass
			pivot = pivot + 1
		#	print("pivot ", (pivot,pivot))

		
		# final check
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
		
		temp = A.matrix[row1].copy()
		for i in range(A.m-1):
			#print("Before: ", A.matrix[row1][i])
			A.matrix[row1][i] = A.matrix[row2][i]
			A.matrix[row2][i] = temp[i]
			#print("After: ", A.matrix[row1][i])
			#print("temp[i]: ", temp[i])
		return A
		'''
		print(A.matrix[row1], A.matrix[row2], sep="\n")
		return A.matrix[row1], A.matrix[row2]
		'''

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
	#A = Matrix([[0, 1, 0, 3], [1, 0, 0, 2], [0, 0, 1, 4]], 3, 4)
	#B = Matrix([[2.0, 8.0, 4.0, 2.0], [2.0, 5.0, 1.0, 5.0], [4.0, 10.0, -1.0, 1.0]], 3, 4)
	C = Matrix([[1],[9]], 2, 1)
	#C.printMatrix()
	#D = Matrix([[0,1], [0,0], [5,9]], 3, 2)

	#x = RREF(A)
	#y  = RREF(B)
	z = RREF(C)
	#r = RREF(D)

