from sys import argv
#This tells that the first word of argv is the script (ex15.py)
#The second part of argv (argv[1]) is the filename
script, filename = argv

#This sets up the txt variable to open the previously entered filename
txt = open(filename)

#This prints the filename
print "Here's your file %r:" % filename
#Using the .read() function the file is read
print txt.read()

txt.close()


#The user is asked for the filename again (same name as before)
print "Type the filename again:"
file_again = raw_input("> ")

#This sets txt_again to the second filename that the user entered
txt_again = open(file_again)

#This reads the second entering of the filename and prints the contents
print txt_again.read()

txt_again.close()
