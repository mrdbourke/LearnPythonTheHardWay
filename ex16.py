from sys import argv

#the filename is the argument variable
#enter into terminal, python script filename
script, filename = argv

#Asking the user whether or not they want to erase the file
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

#Asking for input from the user, any input will do, we are just after the return key
raw_input("?")

#opens the specified file given to argv
print "Opening the file..."
#"w" mode creates the file if it does not exist and empties it if it does
target = open(filename, 'w')

#deleting the contents of the file, because of the w, this step isn't 100% needed
print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

#gathering input from the user
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

#writing the input from the user to the specified file
target.write("%s\n%s\n%s\n" % (line1, line2, line3))
'''
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
'''
#closing the file and telling the user about it
print "And finally, we close it."
target.close()
