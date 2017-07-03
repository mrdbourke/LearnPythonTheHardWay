print "You enter a dark room with two doors. Do you go through door #1, #2 or #3?"

door = raw_input("> ")

if door == "1":
  print "There's a giant bear here eat a cheese cake. What do you do?"
  print "1. Take the cake."
  print "2. Scream at the bear."

  bear = raw_input("> ")

  if bear == "1":
    print "The bear eats your face off. Good job!"
  elif bear == "2":
    print "The bear eats your legs off. Good job!"
  else:
    print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
  print "You stare into the endless abyss at Cthulhu's retina."
  print "1. Blueberries."
  print "2. Yellow jacket clothespins."
  print "3. Understanding revolvers yelling melodies."

  insanity = raw_input("> ")

  if insanity == "1" or insanity == "2":
    print "Your body survives powered by a mind of Jello. Good job!"
  else:
    print "The insanity rots your eyes into a pool of muck. Good job!"

elif door == "3":
    print "You found a treasure chest! It's full of over $5 billion!"
    print "1. Take the gold for yourself."
    print "2. Share the wealth with others and only keep 10%."

    gold = raw_input("> ")

    if gold == "1":
        print "Your greed summons the keepers of the gold, the gold vanishe in"
        print "front of your eyes before burning them, sending you blind."

    elif gold == "2":
        print "Your generosity summons the keepers of the gold, they give you"
        print "an extra $1 billion to keep for yourself."

    else:
        print "So you're just going to leave the chest alone??"
else:
  print "You stumble around and fall on a knife and die. Good job!"
