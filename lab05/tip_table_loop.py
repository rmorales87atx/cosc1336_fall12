# COSC 1336 Lab 5, Problem 1
# Robert Morales (0849639)
#
# This program should read in the amount due for a meal (with tax), 
# and then use the provided function to display the total due with 
# a tip rate of 10%, 15%, 20% and 25%.  The tax rate should be the 
# same in each case (8.25%), so it should be stored in a constant 
# called TAX_RATE.

# display_total_due function
#   inputs: the original bill (with tax), the tip rate, and the tax rate
#   output: displays the total due, with tip and tax
#   processing: calculates the total due by computing the tip
#               based on the pre-tax amount and then adding both
#               the tip and the tax to the original bill
def display_total_due(bill_with_tax, tax_rate, tip_rate):
    bill_without_tax = bill_with_tax / (1 + tax_rate)
    tip = bill_without_tax * tip_rate
    total_due = bill_with_tax + tip
    print("Total due with", format(tip_rate, ".0%"), end="")
    print(" tip: $", format(total_due, ".2f"), sep="")

def main():
    TAX_RATE = 0.0825
    bill_with_tax = float(input("Enter the bill with tax: $"))

    if bill_with_tax <= 0:
        print("Check your typing and try again.")
    else:
        # so there's two different ways to do this...
        # the values can be hard-coded:

        for tip_rate in [0.100, 0.125, 0.150, 0.175, 0.200, 0.225, 0.250]:
            display_total_due(bill_with_tax, TAX_RATE, tip_rate)

        print("------------------------------------------------------")

        # or we can use range -- although range() does not directly
        # support floats, so we need to convert the values...

##        for x in range(100, 251, 25):
##            display_total_due(bill_with_tax, TAX_RATE, x / 1000)

main()
