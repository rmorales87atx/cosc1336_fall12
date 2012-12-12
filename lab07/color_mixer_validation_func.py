# COSC 1336, Lab 7, Problem 1
# Robert Morales

# color_mixer_validation_func.py
# input: two primary colors
# output: the color obtained by mixing the two primary colors
# As distributed, the program does no input validation.
# You should change it to use a function to do input validation,
# as described in the problem.

def is_blue(c):
    return c == "blue" or c == "Blue" or c == "BLUE"

def is_red(c):
    return c == "red" or c == "Red" or c == "RED"

def is_yellow(c):
    return c == "yellow" or c == "Yellow" or c == "YELLOW"

def is_primary_color(c):
    return is_blue(c) or is_red(c) or is_yellow(c)

def read_color(c):
    c = input("Enter a primary color: ")

    while not is_primary_color(c):
        print("Invalid input. Primary colors: red, blue, yellow.")
        c = input("Enter a primary color: ")

    return c

def main():
    c1 = read_color("Enter a primary color: ")
    c2 = read_color("Enter a primary color: ")
    # put them in alphabetical order to cut down on combinations
    if c1 > c2:
        c1, c2 = c2, c1
    # now consider all the combinations of valid colors
    if is_blue(c1) and is_red(c2):
        print("Mixing",c1,"and",c2,"results in purple.")
    elif is_blue(c1) and is_yellow(c2):
        print("Mixing",c1,"and",c2,"results in green.")
    elif is_red(c1) and is_yellow(c2):
        print("Mixing",c1,"and",c2,"results in orange.")
    else:
        print(c1,"and",c2,"are the same, so mixing them gives",c1+".")

main()
