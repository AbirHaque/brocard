#
#	Copyright 2021 Abir Haque
#	Subject to MIT License in LICENSE file
#
#
#
#	Brocard's Problem:
#
#	Find integer pairs (n,m) that satisfy the following:
#
#		n! + 1 = m^2
#
#	Pairs (n, m) that exist are called Brown numbers [1].
#	As of 2020, only three known pairs have been found:
#
#		(4,5), (5,11), (7,71)
#
#	Below is a program I wrote after watching a Numberphile video that introduced this unsolved problem in mathematics [2]. 
#	The program only checks up to n = 100, as the time complexity of this program would make solving larger values a waste of time.
#	Check out the repository of the team that checked n values up to a quadrillion [3].
#
#	Links:
#	[1] https://en.wikipedia.org/wiki/Brocard%27s_problem
#	[2] https://www.youtube.com/watch?v=-Djj6pfR9KU
#	[3] https://github.com/jhg023/brocard

import math

#Below was an old factorial function that required recalculating previously calculated numbers
def factorialSlowVersion(n):
	result = 1
	for i in range(n):
		result = result*(i+1)
	print(result)

def factorial(n):
	factorialLog = open("factorialLog.txt","w+")
	result = 1
	for i in range(n):
		result = result*(i+1)
		factorialLog.write(str(result)+"\n")
		print("Calculating term " + str(i+1))
	return result

#Get last factorial calculated, then multiply it by n to get n!
def factorialCachedLastLine(n):
	factorialLog = open("factorialLog.txt","a+")
	currentFactorialsList = list(open("factorialLog.txt"))
	result = int(currentFactorialsList[len(currentFactorialsList)-1])
	result = result*n
	factorialLog.write(str(result)+"\n")
	return result

#Get last factorial calculated, then continue to multiply it until n! is reached
def factorialCachedAnyLine(n):
	factorialLog = open("factorialLog.txt","a+")
	currentFactorialsList = list(open("factorialLog.txt"))
	result = int(currentFactorialsList[len(currentFactorialsList)-1])
	for i in range(len(currentFactorialsList),n):
		result = result*(i+1)
		factorialLog.write(str(result)+"\n")
		print("Calculating term " + str(i+1))
	return result

brownLog = open("brownLog.txt","w+")
factorial(1)
maxNValue = 100
for n in range(maxNValue):
	mm = factorialCachedAnyLine(n+1)+1
	m = math.sqrt(mm)
	if int(m)**2 == mm:
		brownLog.write("("+str(n)+","+str(m)+")\n")
		print("("+str(n)+","+str(m)+")")
