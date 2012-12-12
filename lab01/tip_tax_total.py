# COSC 1336 Lab 1 Problem 1
# Robert Morales
#
# Test Case:
# The bill amount is $100.00. The tip is $15.00, tax is $7.00,
# total is $122.00.
#
# First probem is that input is not being correctly converted.
# Using 'float()' fixes this problem.
#
# Second problem is in the summation of the total; the bill
# total is bill + tip + tax. Changing the original "+ total"
# to "+ tax" fixes this.
#
# Third problem, in my opinion, is that the numbers are not properly
# formatted in the typical form that currency is written.
# Using "format()" fixes this. Adding sep='' to the print() calls also
# removes the extra space automatically placed after the currency symbol.

tip_percent = 0.15
tax_percent = 0.07
bill = float(input("Enter the bill amount: $"))
tip = bill * tip_percent
tax = bill * tax_percent
total = bill + tip + tax
print("Tip: $", format(tip, ",.2f"), sep='')
print("Tax: $", format(tax, ",.2f"), sep='')
print("Total: $", format(total, ",.2f"), sep='')
