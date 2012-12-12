# COSC 1336, Lab 4 Problem 2(b) Enhanced
# Robert Morales

# Test cases:
# +----------+----------+--------+
# | primary1 | primary2 | result |
# +----------+----------+--------+
# | red      | blue     | purple |
# | red      | yellow   | orange |
# | blue     | yellow   | green  |
# +----------+----------+--------+
# | red      | red      | red    |
# | blue     | blue     | blue   |
# | yellow   | yellow   | yellow |
# +----------+----------+--------+

def maim():
    PRIMARY_COLORS = ("red", "blue", "yellow")

    primary1 = input("Enter a primary color: ").lower()
    if primary1 not in PRIMARY_COLORS:
        print(repr(primary1), "is not a primary color.")
        return

    primary2 = input("Enter another primary color: ").lower()
    if primary2 not in PRIMARY_COLORS:
        print(repr(primary2), "is not a primary color.")
        return

    if primary1 == primary2:
        print("The colors are the same!")
        return

    result = None

    if "red" in (primary1, primary2) and "blue" in (primary1, primary2):
        result = "purple"
    elif "red" in (primary1, primary2) and "yellow" in (primary1, primary2):
        result = "orange"
    elif "blue" in (primary1, primary2) and "yellow" in (primary1, primary2):
        result = "green"

    if result is None: # this should be impossible
        print("o_O what did you do to my program?")
        return

    print("Mixing", primary1, "&", primary2, "gives you:", result)

##    if (primary1 == "red" or primary1 == "blue" or primary1 == "yellow") \
##       and (primary2 == "red" or primary2 == "blue" or primary2 == "yellow"):
##        if primary1 == "red" and primary2 == "blue":
##            result = "Purple"
##        elif primary1 == "red" and primary2 == "yellow":
##            result = "Orange"
##        elif primary1 == "blue" and primary2 == "yellow":
##            result = "Green"
##
##        if result == "??":
##            print()
##            print("Sorry, I didn't recognize your input.")
##            print("Due to code limitations, the first color can only be " \
##                  "'red' or 'blue'. The second color can only be " \
##                  "'blue' and 'yellow'. All lower-case.")
##        else:
##            print("You get:", result)
##    else:
##        print("Check your typing and try again.")

maim()
