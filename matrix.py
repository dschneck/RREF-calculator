class Matrix:
	def  __init__(self, matrix: [[int]], m: int, n: int):
		self.matrix = matrix
		self.m = m
		self.n = n

	def printMatrix(self):
		line = "+++"

		for i in range(self.n):
			line += "++"

		print(line)

		for i in range(self.m):
			print("| ", end="")
			for j in range(self.n):
				print(self.matrix[i][j], end=" ")
			print("|")

		print(line, "\n")
