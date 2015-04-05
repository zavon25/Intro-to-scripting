#!/usr/bin/env python
"""
ITS 3210 Introduction to Scripting Languages
Governor's State University
Adam Balauskas

Assignment 2

This program should receive input from the user from both the command line arguments
used when launching the script and by use of prompts while the script is running. The
comments in this assignment give further guidance on what specific input is expected
and how it is to be handled.

Feel free to be creative and go beyond the minimum requirements. The primary learning
objective of this assignment is receiving user input, both from command line arguments
and within the program's execution. Can you incorporate any previously learned knowledge
about Python into this exercise?
"""

from sys import argv 
import os

script_name, user_name, age = argv

#print user_name, age  # display this in a friendlier way, e.g. "Hello {user_name}, you
# are at the very YOUNG age of {age} years old!"

os.system('cls') #information to clear the screen retrieved from http://stackoverflow.com/questions/1432480/any-way-to-clear-pythons-idle-window

#The following line outputs the arguments of user_name and age into a string welcoming the user and repeating their age.
print "Welcome %s to the python assignment bot,  I see you are currently %s years old" %(user_name,age)

print """The next two questions ask your height in feet and inches. If you are 5'11",
answer 5 to the first question and 11 to the second."""
#The following code is a bit of idiot proofing that will not let the user continue if 
#a non integer is entered for the following questions
#For example if a "d" is entered, it will warn the user that an incorrect entry has been used and 
#will re prompt the user to try again.
#This function was found http://stackoverflow.com/questions/19984168/python-checking-whether-or-not-a-variable-is-a-int-using-while-loop?lq=1
while True:
	try:	
		height_feet = int(raw_input("How many feet tall are you (excluding inches)? "))
		break
	except ValueError:
		print "Please make sure you are entering a number!"
while True:
	try:	
		height_inches = raw_input("How many inches tall are you (excluding feet)? ")
		if int(height_inches) >= 12:#this will correct your hight if an inches value of more than 12 is entered.
			height_inches = int(height_inches) - 12
			height_feet = int(height_feet) + 1	
		break
	except ValueError:
		print "Please make sure you are entering a number!"
 

# calculate how many inches tall the user is based on their input
# for instance, if they enter 5 and 10, they are 70 inches tall
inches = 0
inches = int(height_feet) * 12 + int(height_inches) #calculates your correct height in inches.
# displays this in the format 5'10 for values 5 and 10, and also shows what that equals to  in inches.
print """According to this data, you are currently %s'%s", or %d inches tall""" % (height_feet,height_inches,inches) 
print "Thank you for running Python Assignment Bot"