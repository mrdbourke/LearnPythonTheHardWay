from sys import exit

choice = 0

#broken
def choice_zero():
    choice = 0
    choice = raw_input("> ")

def gold_room():
  print "This room is full of gold. How much do you take?"

  how_much = int(raw_input("> "))
  if how_much < 50:
    print "Nice, you're not greedy, you win!"
    exit(0)
  else:
    dead("You greedy bastard!")

#broken (because of choice())
def bear_room():
  print "There is a bear here."
  print "The bear has a bunch of honey."
  print "The fat bear is in front of another door."
  print "How are you going to move the bear?"
  bear_moved = False

  while True:
    choice_zero()
    if choice == "honey" or choice == "honey pot":
      dead("The bear looks at you then slaps your face off.")
    elif "taunt" or "taunt bear" in choice and not bear_moved:
      print "The bear has moved from the door. You can go through it."
      bear_moved = True
      choice_zero()
    elif choice == "taunt bear" and bear_moved:
      dead("The bear gets pissed off and chews your leg off.")
    elif "open" or "open door" or "go" or "go through door" and bear_moved:
      gold_room()
    else:
      print "I got no idea what that means."

def cthulhu_room():
  print "Here you see the great evil Cthulhu."
  print "He, it, whatever stares at you and you go insane."
  print "Do you flee for your life or eat your head?"

  choice = raw_input("> ")

  if "flee" in choice:
    start()
  elif "head" in choice:
    dead("Well that was tasty!")
  else:
    cthulhu_room()


def dead(why):
  print why, "Good job!"
  exit(0)

def start():
  print "You are in a dark room."
  print "There is a door to your right and left."
  print "Which one do you take?"

  choice = raw_input("> ")

  if choice == "left":
    bear_room()
  elif choice == "right":
    cthulhu_room()
  else:
    dead("You stumble around the room until you starve.")

def end_game():
    leave = raw_input('> ')

    if leave or exit or finish or end in leave:
        exit(0)
    else:
        gold_room()

start()
