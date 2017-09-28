#!/usr/bin/python3
num = int(input("enter the number:  "))
#we need to import a number 
for i in range(1,4):
	# i is range from 1 to 4
	for j in range(1,11): 
		#this is the range from 1 to 11
		print(i,"x",j,"=",i*j)
		#the result is seen after running the program
