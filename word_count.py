#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser( description="" )

parser.add_argument(
	"data_file",
	help="path to file we want to read",
)
#boilerplate code to set file path
args = parser.parse_args( )
	#args will associate data_file and the data file we input
print("args=", args)
print("args.data_file =", args.data_file)
#these are ways to check that we have properly passed the file to our program
fh = open(args.data_file) #don't forget to assign the open file to a variable

lines = 0
words = 0
chars = 0

for line in fh:
	lines += 1

	str = ""
	str = line.split(" ")
	words += len(str)

	x = len(line)
	chars += x

print("Lines =", lines)
print("Words =", words)
print("Chars =", chars)

#-------------------------------------------------------------------------------
# our code for analyzing the data
#-------------------------------------------------------------------------------
