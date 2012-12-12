# COSC 1336, Lab 6 Problem 1
# Robert Morales

# Test cases:
# +----------+----------+--------+
# | first    | second   | result |
# +----------+----------+--------+
# | red      | blue     | purple |
# | red      | yellow   | orange |
# | blue     | yellow   | green  |
# +----------+----------+--------+

# Known Bugs/Limitations:
#   1) Input is case-sensitive.

UNKNOWN = "??"

# is_valid_primary
#   input: color (string)
#   output: Boolean value indicating if `color` is a primary color.
def is_valid_primary(color):
    return color == "red" or color == "blue" or color == "yellow"

# get_primary_color
#   input: N/A
#   output: String value containing the user's input,
#           which is guaranteed to be a valid primary color.
def get_primary_color():
    result = UNKNOWN

    while result == UNKNOWN:
        result = input("Enter a primary color: ")

        if is_valid_primary(result):
            break
        else:
            result = UNKNOWN
            print("Invalid entry. Recognized colors (case sensitive): "
                  "red, blue, yellow")
            print()

    return result

# is_one_red
#   inputs: two string values, `a` and `b`
#   output: Boolean value which determines if either string is the
#           primary color 'red'.
def is_one_red(a,b):
    if is_valid_primary(a) and is_valid_primary(b):
        return a == "red" or b == "red"
    else:
        return UNKNOWN

# is_one_red
#   inputs: two string values, `a` and `b`
#   output: Boolean value which determines if either string is the
#           primary color 'blue'.
def is_one_blue(a,b):
    if is_valid_primary(a) and is_valid_primary(b):
        return a == "blue" or b == "blue"
    else:
        return UNKNOWN

# is_one_red
#   inputs: two string values, `a` and `b`
#   output: Boolean value which determines if either string is the
#           primary color 'yellow'.
def is_one_yellow(a,b):
    if is_valid_primary(a) and is_valid_primary(b):
        return a == "yellow" or b == "yellow"
    else:
        return UNKNOWN

# mix_colors
#   inputs: two primary colors
#   output: String value containing the result of two primary colors
#           being combined.
def mix_colors(first, second):
    if is_one_red(first, second) and is_one_blue(first, second):
        return "purple"
    elif is_one_red(first, second) and is_one_yellow(first, second):
        return "orange"
    elif is_one_blue(first, second) and is_one_yellow(first, second):
        return "green"
    else:
        return UNKNOWN

def maim():
    print("This program examines two primary colors and determines what")
    print("color they create when combined.")
    print()

    first = get_primary_color()
    second = get_primary_color()
    result = mix_colors(first, second)

    if result == UNKNOWN: # this should NOT happen
        print("Bork bork bork!!!")
    else:
        print("Mixing", first, "&", second, "makes", result)

maim()
