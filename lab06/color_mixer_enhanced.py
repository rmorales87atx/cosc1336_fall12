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


# is_valid_primary
#   input: color (string)
#   output: Boolean value indicating if `color` is a primary color.
def is_valid_primary(color):
    return color.lower() in ("red", "blue", "yellow")

# get_primary_color
#   input: N/A
#   output: String value containing the user's input,
#           which is guaranteed to be a valid primary color.
def get_primary_color():
    for result in iter(lambda: input("Enter a primary color: "), ''):
        if is_valid_primary(result):
            return result
        else:
            print("Invalid entry. Recognized colors: red, blue, yellow")

# mix_colors
#   inputs: two primary colors
#   output: String value containing the result of two primary colors
#           being combined.
def mix_colors(first, second):
    first = first.lower()
    second = second.lower()

    if first > second:
        first,second = second,first

    if "red" == first and "blue" == first, second:
        return "purple"
    elif "red" in (first, second) and "yellow" in (first, second):
        return "orange"
    elif "blue" in (first, second) and "yellow" in (first, second):
        return "green"
    else:
        return None

def maim():
    print("This program examines two primary colors and determines what")
    print("color they create when combined.")
    print()

    try:
        first = get_primary_color()
        second = get_primary_color()
        result = mix_colors(first, second)

        if result is None: # this should NOT happen
            print("Bork bork bork!!!")
        else:
            print("Mixing", first, "&", second, "makes", result)
    except KeyboardInterrupt:
        pass

maim()
