# COSC 1336 Lab 1 Problem 4
# Robert Morales
#
# Input:
#   1) First odometer reading
#   2) Last odometer reading
#   3) Gallons consumed
# Process: Calculate miles per gallon
# Output: Miles per gallon
#
# Test Case:
# The initial odometer reading is 0. The last odemeter reading is 100.
# If we consume 50 gallons traveling 100 miles, the program should
# output an MPG of 100/50=2.
#
# Known Bugs:
# 1) This program will not handle the last odometer reading
#    being less than the initial odemeter reading.
# 2) This program will not handle negative numbers.
# 3) This program cannot handle obviously outrageous input, such as
#    having traveled 5,000 miles and only consuming 1 gallon of gas.
# 4) It is possible to make this program divide by 0. Don't blame me when
#    demons fly out of your nose.

odometer_start = float(input("Enter the odometer reading for the start of your trip: "))
odometer_stop = float(input("Enter the odometer reading for the end of your trip: "))
gallons_used = float(input("Enter the amount in gallons of gas used for the trip: "))

miles_traveled = odometer_stop - odometer_start
miles_per_gallon = miles_traveled / gallons_used

print("Your MPG (miles-per-gallon) for this trip is", format(miles_per_gallon, ",.4f"))
