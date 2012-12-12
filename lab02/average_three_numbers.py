########################################################################
# COSC 1336 Lab 2 Problem 2
# Robert Morales
########################################################################

# PROGRAM DESCRIPTION:
#   This program reads in three numbers and displays their average. The
#   important thing is that it uses a function for calculating and 
#   displaying the average.
#
# TEST CASE:
#   First number = 10
#   Second number = 10
#   Third number = 10
#
#   The total of all three numbers is 30
#   The average is 10

# FUNCTION: display_average
# PURPOSE: Calculates the average of three numbers and displays the
#          result.
# INPUT:
#   1) first number
#   2) second number
#   3) third number
# OUTPUT:
#   1) Result of calculation
# PROCESS:
#   1) Calculate the result by adding first, second, and third,
#      and dividing by three.
#   2) Display the result.
def display_average(first, second, third):
    result = (first + second + third) / 3
    print("The average is", result)

# FUNCTION: main
# PURPOSE: Main program execution. Gathers all required program input
#          and calls display_average to process the input.
def main():
    print("Enter three numbers:")
    first = float(input("First: "))
    second = float(input("Second: "))
    third = float(input("Third: "))
    display_average(first, second, third)

########################################################################

main()
