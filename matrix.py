class Matrix:
	def  __init__(self, matrix: [[float]], m: float, n: float):
		self.matrix = matrix
		self.m = m
		self.n = n

	def printMatrix(self):
		if self.m > 5 or self.n > 6:
			print("Too big to print")
			return

		line = "+++++++++"

		for i in range(self.n):
			line += "++++++++"

		print(line)

		for i in range(self.m):
			print("|\t ", end="")
			for j in range(self.n):
				print(self.matrix[i][j], end="\t")
			print("|")

		print(line, "\n")
