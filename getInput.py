#!/usr/bin/env python3
import sys

class Input:
	def getInput(filename=None):
		A =[[]]
		r = None
		c = None

		if filename == None:
			print("How many rows?")
			r = int(input())

			print("How many rows?")
			c = int(input())

			for i in range(r):
				for j in range(c):
					A[i].append(float(input(f'Entry {i},{j}: ')))
				if i != r-1:
					A.append([])
			return (A, r, c)
		else:
			print("Getting input from:", filename, sep=" ")
			#try:
				#with open(filename, "r") as matrix:
