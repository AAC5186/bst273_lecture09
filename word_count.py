#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser( description="" )

parser.add_argument(
	"data_file",
	help="path to file we want to read",
)

#-------------------------------------------------------------------------------
# Are there other arguments we need?
#-------------------------------------------------------------------------------

args = parser.parse_args( )
	#args will associate data_file and the data file we input
print(args)
print(args.data_file)
#these are ways to check that we have properly passed the file to our program
#-------------------------------------------------------------------------------
# our code for analyzing the data
#-------------------------------------------------------------------------------
