# COSC 1336 Lab 1 Problem 2
# Robert Morales
#
# Using Google's handy built-in calculator, the test case is:
# 100 F = 37.7778 C
# As this program was originally written, the actual output was:
# "100 F = 83 C"
# (How dare this program say Google is wrong!)
#
# Changing the use of "//" to "/" brought us just a small step
# closer:
# "100 F = 82.22222222222223 C"
#
# Placing parentheses around both parts of the equation finally
# brings us to the correct result:
# "100 F = 37.77777777777778 C"
#
# A small use of format() thrown in to keep things sane.

fahrenheit = float(input("Enter a temperature in Fahreheit: "))
celsius = (fahrenheit - 32) * (5 / 9)
print("Temperature converted to Celsius:", format(celsius, ",.4f"), "degrees")
