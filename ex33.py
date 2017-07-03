def for_loop(loop_variable, increment):
    i = 0
    numbers = range(0, loop_variable)

    for number in numbers:
        if number <= loop_variable:
            print "At the top i is %d" % i
            numbers.append(i)

            i = i + increment
            print "Numbers now: ", numbers
            print "At the bottom i is %d" % i

            print "The numbers: "

            for num in numbers:
                print num

for_loop(30, 10)
