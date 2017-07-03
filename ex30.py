people = 10
cars = 45
trucks = 97

if cars > people:
#prints if cars greater than people
  print "We should take the cars."
elif cars < people:
#prints if cars not greater than people
  print "We should not take the cars."
else:
  print "We can't decide."

if trucks > cars or trucks > people:
#prints if trucks greater than cars or trucks greater than people
  print "That's too many trucks."
elif trucks < cars:
#prints if cars greater than trucks
  print "Maybe we could take the trucks."
else:
  print "We still can't decide."

if people > trucks or cars < people:
#prints if people greater than trucks or cars less than people
  print "Alright, let's just take the trucks."
else:
  print "Fine, let's stay home then."
