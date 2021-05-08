# pizza_slices.py
# Calculates the maximum number of pizza slices to divide a pizza into,
# so that the minimum area per slice is maintained.

# Robert Morales (0849639)
# Fall 2012
# Oct 2, 2012

from math import pi

MIN_SLICE_AREA = 56

def main():
    radius = float(input("Enter the radius of the pizza: "))
    area = pi * radius**2
    max_slices = int(area / MIN_SLICE_AREA)

    print("Maximum number of slices:", max_slices)

main()
