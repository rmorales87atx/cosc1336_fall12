# COSC 1336 Lab 1 Problem 3
# Robert Morales
#
# Input: Total square feet
# Process: Calculate number of acres
# Output: Number of acres
#
# Test Case:
# Verified in Google's calculator we know that
# 50,000 square feet equals 1.14784 acres.

ONE_ACRE = 43560

square_feet = float(input("Enter the number of square feet: "))

total = square_feet / ONE_ACRE

print("The number of acres in your tract is", format(total, ",.4f"))
