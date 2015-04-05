#!/usr/bin/env python
"""
ITS 3210 Introduction to Scripting Languages
Governor's State University
Adam Balauskas

Assignment 6

Create a script that performs the following tasks:

1. Ask the user for a numeric score using raw_input()
2. Convert the user-supplied score into an integer
3. Return the letter grade for the score in a user-friendly sentence (use the grading
   scale in the syllabus)
4. Modify the code you wrote in steps 1-3 so that the script continues asking for a 
   score until the user types 'end' instead of a score
5. Every time the user enters a score, save the score in a list
6. Convert step 1 into its own function that it returns the user input
7. Convert step 3 into its own function so that it returns the letter grade
8. Modify the program so that the user can enter as many scores as they'd like (until
   they type 'end'), and instead of showing the letter grade immediately, wait until
   the user has typed all of the scores then return formatted output showing each score
   and its letter grade at the end. Sort the list from low to high scores before 
   displaying them. The final output should look similar to this (with the scores you
   enter). Be sure to test entering the minimum and maximum scores for different grades
   such as 90, 79, and 60:

Score  Grade
-----  -----
    0      F
   72      C
   84      B
   91      A
  100      A
  
9. Print the lowest score and corresponding letter grade in a user-friendly sentence.
10. Create a dictionary with student names and scores, similar to this (use any names
    and scores you want):
    
student_dictionary = {
    "John Doe": 65,
    "Jane Doe": 77,
    "Bob Smith": 100,
    "Amy Jones": 99
}

11. Using the function created in step 7, loop through the dictionary and print a 
    user-friendly sentence with each student's name, score, and corresponding letter grade
"""
import os
grade = 0
gradelist = []
lettergrade = 0
#define the student dictionary.
student_dict = {
	"Adam Balauskas": 100,
	"Ai Dogostino": 35,
	"Alvin Prude": 75,
	"Ja Romeo": 86,
	"Riven Smith": 67,
	"Garen Damacia": 92,
	"Draven Blood": 15}
#Accepts input from a user and verifies that it is a number or not. If it is not a number it then checks to 
#see if the string entered was "end". if it is, it returns end. other wise it asks for a number again.
#After a number is entered it, the number is added to the score list and then returned.
def entergrade():
	while True:
		try:
			grade = raw_input("Please enter the score you received:")
			if(grade == "end"):
				return grade
			grade = int(grade)
			gradelist.append(grade)
			# displays the letter grade received from the score.... [modified to hide till after the list is sorted]
			#print "Your grade of %i gives you a letter grade of %s" % (grade,checkgrade(grade))
			return grade
		except ValueError:
			print "Please enter a number"
	
#accepts an input and returns the corresponding Letter Grade.
def checkgrade(grade):
	if grade < 60:
		lettergrade = "F"
	elif grade >= 60 and grade <=69:
		lettergrade = "D"
	elif grade >= 70 and grade <=79:
		lettergrade = "C"
	elif grade >= 80 and grade <=89:
		lettergrade = "B"
	elif grade >= 90:
		lettergrade = "A"
	return lettergrade
os.system('cls')
""""
while grade != "end":
#	try:
	grade = raw_input("Please enter the score you received > ")
	grade = int(grade)
	gradelist.append(grade)
	checkgrade(grade)
	#break
	#except ValueError:
	#	print "Please make sure you are entering a number."
"""
while grade != "end":#Allows the user to continuously enter scores until they enter End.
	grade = entergrade()
#entergrade()
gradelist.sort()#sorts the grade list.
os.system('cls')#simply clears the screen for readability

#the following section of code will step through the list and print out the score and letter grade, then print out the lowest one in a sentence.
print "Score	Grade"
print "-----	-----"
for i in gradelist:
	print "%5i	%5s" % (i,checkgrade(i))
print "The lowest score and corresponding letter grade entered was a score of %i and a grade of %s" % (gradelist[0],checkgrade(gradelist[0]))
raw_input("Please press any key to clear the screen and continue:")
os.system('cls')#simply clears the screen for readability

#The following code will step through the student dictionary and print a line with the name,score, and letter grade by 
#retrieving the letter grade from calling the Checkgrade() fuction.
for key in student_dict:
	print "The Student %s received a score of %i which is a letter grade of %s." % (key,student_dict[key],checkgrade(student_dict[key]))