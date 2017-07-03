#Number of cars
cars = 100
#Amount of space in a car
space_in_a_car = 4.0
#Number of drivers
drivers = 30
#Number of passengers
passengers = 90
#Amount of cars not driven
cars_not_driven = cars - drivers
#Number of cars that are driven
cars_driven = drivers
#The amount of people who can be carpooled
carpool_capacity = cars_driven * space_in_a_car
#The average number of passengers per car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
