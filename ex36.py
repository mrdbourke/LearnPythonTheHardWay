import random
from sys import exit

#defining the different outcomes of each of the functions
leg_day_squats = ["3 sets of 10 squats",
                   "3 sets of 10 lunges",
                   "3 sets of 10 stiff-legged deadlifts",
                   "3 sets of 10 box jumps"]

leg_day_not_squats = ["3 sets of 10 leg press",
                      "3 sets of 10 leg extension",
                      "3 sets of 10 hamstring curl",
                      "3 sets of 10 calf raises"]

rest_day_message = "You've managed to unlock a rest day! \nEnjoy the day off for recovery."

chest_day = ["3 sets of 10 bench press",
             "3 sets of 10 weighted dips",
             "3 sets of 10 chest pullovers",
             "3 sets of 10 tricep pressdowns"]

back_day = ["3 sets of 10 bent over rows",
            "3 sets of 10 deadlifts",
            "3 sets of 10 pullups",
            "3 sets of 10 bicep curls"]

#starting the workout bot functions here
def start():
    print "Hello world! I'm the workout bot!"
    print "It's time to make some gains!"
    print "Press 1 for leg day or 2 for an upper body workout."
    print "Or type in random for a random workout!"

    start_input = raw_input("> ")

    if start_input == "1":
        leg_day()
    elif start_input == "2":
        upper_body()
    elif start_input == "random":
        rand = random.randint(1,3)
        if rand == 1:
            leg_day()
        elif rand == 2:
            upper_body()
        elif rand == 3:
            rest_day()
        else:
            print "Something went wrong :("
    else:
        print "I don't understand that!"


def leg_day():
    #leg day function, offer choice for squats or no squats
    print "Let's grow some wheels!"
    print "Do you prefer squats? Enter 1"
    print "No squats? Enter 2"
    print "Want an upper body workout instead? Enter upper"

    leg_day_input = raw_input("> ")

    if leg_day_input == "1":
        for item in leg_day_squats:
            print item
    elif leg_day_input == "2":
        for item in leg_day_not_squats:
            print item
    elif leg_day_input == "upper":
        upper_body()
    else:
        print "I'm sorry, I don't understand that!"
    restart()


def upper_body():
    #upper body day function, offer choice for chest or back workout
    print "Let's pump up that upper body!"
    print "Want to train chest? Hit 1"
    print "Back day more your thing? Hit 2"
    print "Prefer a leg day? Type in legs"

    upper_body_input = raw_input("> ")

    if upper_body_input == "1":
        for item in chest_day:
            print item
    elif upper_body_input == "2":
        for item in back_day:
            print item
    elif upper_body_input == "legs":
        leg_day()
    else:
        print "I'm sorry, I don't understand that!"
    restart()


def rest_day():
    #rest day function, print rest day message
    print rest_day_message
    restart()


def restart():
    #restart entire program back to start
    #set inputs to 0
    print "\nAwesome work!"
    print "When you've finished your workout or rest day, enter 1 to go back to the start."
    print "Or type any key to exit the workout bot."
    #implement exit option
    reset = raw_input("> ")
    if reset == "1":
        start()
    else:
        exit(0)

start()
