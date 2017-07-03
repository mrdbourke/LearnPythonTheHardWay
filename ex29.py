people = 20
cats = 30
dogs = 15

if people < cats:
  print "Too many cats! The world is doomed!"

if people > cats:
  print "Not many cats! The world is saved!"

if people < dogs:
  print "The world is drooled on!"

if people > dogs:
  print "The world is dry!"

dogs += 5

if people >= dogs:
  print "People are greater than or equal to dogs."

if people <= dogs:
  print "People are less than or equal to dogs."

if people == dogs:
  print "People are dogs."

if people == dogs and cats > people:
    print "People are dogs and cats rule over people."

if people is not None:
    print "I'm a dog person."
