########################################################################
# COSC 1336 Lab 2 Problem 1
# Robert Morales
########################################################################
# PROGRAM DESCRIPTION:
#   This program should read in the amount due for a meal (with tax), 
#   and then use the provided function to display the total due with 
#   a tip rate of 10%, 15%, 20% and 25%.  The tax rate should be the 
#   same in each case (8.25%), so it should be stored in a constant 
#   called TAX_RATE.
#
# TEST CASE:
#   Entering <16.24> should result in the following outputs:
#   $17.74, $18.49, $19.24, $19.99
#   (Taken from the output in the lab instructions)
########################################################################

# FUNCTION: display_total_due
# PURPOSE: Calculates tip and tax given the rates for each and prints
#          the total due with these calculations added.
# INPUT:
#     1) the original bill (with tax)
#     2) the tip rate
#     3) the tax rate
# OUTPUT:
#     1) Displays the total due, with tip and tax
# PROCESS:
#     1) Calculate the pre-tax subtotal by dividing bill_with_tax
#        by the tax rate plus 1.
#     2) Calculate the tip by multiplying the pre-tax subtotal
#        by the tip rate.
#     3) Calculate the total due by adding bill_with_tax and the tip.
#     4) Print the tip rate as a percentage.
#     5) Print the total due.
def display_total_due(bill_with_tax, tip_rate, tax_rate):
    pretax_subtotal = bill_with_tax / (1 + tax_rate)
    tip = pretax_subtotal * tip_rate
    total_due = bill_with_tax + tip
    print("Total due with", format(tip_rate, '.0%'), end="")
    print(" tip: $", format(total_due, ".2f"), sep='')

# FUNCTION: main
# PURPOSE: The main point of execution for this program.
# PROCESS:
#   1) Read input for the meal total (including tax).
#   2) Calculate the total due with the tip rates
#      10%, 15%, 20%, 25%
def main():
    TAX_RATE = 0.0825
    meal_total = float(input("Enter the bill with tax: "))

    for tip_rate in [0.10, 0.15, 0.20, 0.25]:
        display_total_due(meal_total, tip_rate, TAX_RATE)

########################################################################

main()
