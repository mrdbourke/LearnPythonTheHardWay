#defining the x variable
x = "There are %d types of people." % 10
#defining the binary variable
binary = "binary"
#defining the do_not variable
do_not = "don't"
#defining the y variable using a combination of the binary and do_not variables
y = "Those who know %s and those who %s." % (binary, do_not)
#displaying the previously defined x variable
print x
#displaying the previously defined y variable
print y

# %r prints all the details within a string, it displays raw data
# %r is best for debugging
print "I said: %r." % x
#printing the y string
print "I also said: '%s'." % y

#defining hilarious as a False variable
hilarious = False
#Defining a joke evaluation statement
joke_evaluation = "Isn't that joke so funny?! %r"

#printing the joke evaluation string and result
print joke_evaluation % hilarious

#defining w as the left side of a string
w = "This is the left side of..."
#defining e as the right side of a string
e = "a string with a right side."

#printing a cominbation of w and e string variables
print w + e
