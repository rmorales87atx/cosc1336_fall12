# COSC 1336, Lab 4 Problem 2(a)
# Robert Morales

# Test cases:
# +----------+----------+--------+
# | primary1 | primary2 | result |
# +----------+----------+--------+
# | red      | blue     | purple |
# | red      | yellow   | orange |
# | blue     | yellow   | green  |
# +----------+----------+--------+

# Known Bugs/Limitations:
#   1) primary1 will only be recognized with values "red" and "blue".
#   2) primary2 will only be recognized with values "blue" and "yellow".
#   3) Input is not recognized if it is not all lower case.
#
#   *  Fixing the above bugs requires machinery not yet presented in class;
#   *  see "color_mixer_enhanced.py"

def maim():
    primary1 = input("Enter a primary color: ")
    primary2 = input("Enter another primary color: ")
    result = "??"

    if (primary1 == "red" or primary1 == "blue" or primary1 == "yellow") \
       and (primary2 == "red" or primary2 == "blue" or primary2 == "yellow"):
        if primary1 == "red" and primary2 == "blue":
            result = "Purple"
        else:
            if primary1 == "red" and primary2 == "yellow":
                result = "Orange"
            else:
                if primary1 == "blue" and primary2 == "yellow":
                    result = "Green"

        if result == "??":
            print()
            print("Sorry, I didn't recognize your input.")
            print("Due to code limitations, the first color can only be " \
                  "'red' or 'blue'. The second color can only be " \
                  "'blue' and 'yellow'. All lower-case.")
        else:
            print("You get:", result)
    else:
        print("Check your typing and try again.")

maim()
