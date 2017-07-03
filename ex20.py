#imports the argument variable
from sys import argv
#states what the argv is going to be
script, input_file = argv

#creating a function to print all within f
def print_all(f):
  print f.read()

#seek starts reading the file at a specific point
#seek(0) will start at the beginning of the file
def rewind(f):
  f.seek(0)

#creating a function to print a line which takes two arguments
def print_a_line(line_count, f):
  print line_count, f.readline()

#creating a variable current_file that opens the input_file given to the script
current_file = open(input_file)

print "First let's print the whole file:\n"

#printing the contents of the current_file
print_all(current_file)

print "Now let's rewind, kind of like a tape."

#taking the current_file back to the start using seek(0)
rewind(current_file)

print "Let's print three lines:"

#adding 1 to the current_line twice and then printing the current line of the file
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
