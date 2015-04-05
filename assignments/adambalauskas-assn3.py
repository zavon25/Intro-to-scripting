#!/usr/bin/env python
"""
ITS 3210 Introduction to Scripting Languages
Governor's State University
Adam Balauskas

Assignment 3

This program should receive two filenames from the user from the command line arguments
used when launching the script, and copy the first file into the second. Use the file
provided (infile.txt) as the input_file.
"""

from sys import argv
from os.path import exists 
import os

# we don't use the script variable, so there is no need to assign it a value:
# use the indexing operator / slice techniques learned for strings and apply them to the
# argv attribute to ONLY extract the filenames (as discussed in last week's discussion 
# board).
script, input_file, output_file = argv
#extracts and sets the file names from the commandline

input_file = argv[1]
output_file = argv[2]
os.system('cls')#clear the screen for easy reading

# print the absolute path of each file using the relevant function from the os.path module
print "Path of the input file is: %s" % os.path.abspath(input_file)
print "Path of the output file is: %s" % os.path.abspath(output_file)

# combine the next two lines into one
#in_file = open(input_file).read()
#indata = in_file.read()
indata = open(input_file).read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(output_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input('>')

out_file = open(output_file, 'w')
out_file.write(indata)

# before closing the files, read the first 13 characters from the first file and print
# them to the console
print open(input_file).read(13)
# why are the next two lines important?  
# These lines are important because you need to close the file 
out_file.close()
#in_file.close()

# append the footer string to the output_file (do not overwrite any existing text)
footer = 'The End'
output = open(output_file, 'a')
output.write("\n")
output.write(footer)
output.close()