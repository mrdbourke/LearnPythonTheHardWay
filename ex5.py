name = 'Zed Shaw'
age = 35 # not a lie
height = 74 # inches
height_in_cm = height * 2.54
weight = 180 # lbs
weight_in_kg = weight / 2.2
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "%d cm tall." % height_in_cm
print "He's %d kilograms heavy." % weight_in_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right

print "If I add %d, %d, and %d I get %d." % (
  age, height, weight, age + height + weight)
