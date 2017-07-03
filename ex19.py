#defining the function cheese_and_crackers, with the arguments
#cheese_count and cheese_and_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
  print "You have %d cheeses!" % cheese_count
  print "You have %d boxes of crackers!" % boxes_of_crackers
  print "Man that's enough for a party!"
  print "Get a blanket.\n"

#feeding cheese_and_crackers two values as arguments
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

#creating variables for amount_of_cheese and amount_of_crackers
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

#feeding the cheese_and_crackers function the previously created variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#feeding the cheese_and_crackers function math as the arguments
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

#combining the variables with math as arguments
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def weightlifting(sets, reps):
    print "You have to do %d sets and %d reps of squats!" % (sets, reps)
    print "Don't do anything less than %d reps!" % reps
    print "Man you're going to make some gains!"
    print "Keep on lifting!\n"

weightlifting(5, 10)
weightlifting(5*2, 1*8)
weightlifting(16/4, 10/5)
amount_of_sets = 10
amount_of_reps = 10
weightlifting(amount_of_sets, amount_of_reps)
weightlifting(amount_of_sets - 7, amount_of_reps)
weightlifting(amount_of_sets - 6, amount_of_reps + 2)
