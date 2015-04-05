#!/usr/bin/env python
"""
ITS 3210 Introduction to Scripting Languages
Governor's State University
adam balauskas

Assignment 4

You've just learned functions and a little bit about importing modules and debugging code!
That's a lot! This will be slightly complicated since it will involve a couple tasks:

1. You will need this file (assn4.py) and the other attached file in the same folder for
   this to work (valentine.py). Do not worry about understanding the code in the valentine
   module. The point is THIS file (assn4.py), not comprehending the imported module. For
   now treat it like a 'black box'.
2. Fix the code that is currently in this file. I recommend doing this before anything
   else! The valentine.py file does not contain any errors. All of the errors are in this
   file.
3. Once you have fixed the errors in this file, follow the additional instructions in the
   comments below.
4. HINT: Look at what code has already run before you receive an error message. No need
   to try fixing something that isn't broken!
"""

import valentine

# CREATE FUNCTION BEGINNING HERE (remove this comment when done)
# create a function using the code below
def Val_Date():
	print "Valentine's Day is %s" % valentine.how_many_days_away()
	print "I can't believe Valentine's Day falls on a %s this year! There won't be \
	an open table at a restaurant until midnight!" % valentine.which_weekday()


print "Wait! I can't remember how many days away it is till Valentine's Day.\n"
print "How many days away is Valentine's Day?"

# call your function that you created above
Val_Date()
# there are no errors above this comment unless you created them (but plenty below it!)

def favorite_candy(candy_name):
    print "Go ahead and buy %s for yourself, you deserve it!" % candy_name

def more_cowbell():
    print "I've got a fever, and the only prescription is more cowbell!"
    print "Or Valentine's Day candy!"
    candy = raw_input("What is your favorite candy? ")
    favorite_candy(candy)
    
# call the more_cowbell function
more_cowbell()