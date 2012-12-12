# COSC 1336 Lab 5, Problem 1 (enhanced)
# Robert Morales (0849639)

from table_printer import print_table  # used to print a pretty table
from io_util import get_float          # used for input validation

# This program should read in the amount due for a meal (with tax), 
# and then use the provided function to display the total due with 
# a tip rate of 10%, 15%, 20% and 25%.  The tax rate should be the 
# same in each case (8.25%), so it should be stored in a constant 
# called TAX_RATE.

def get_total_due(bill_with_tax, tax_rate, tip_rate):
    bill_without_tax = bill_with_tax / (1 + tax_rate)
    tip = bill_without_tax * tip_rate
    total_due = bill_with_tax + tip
    return total_due

def main():
    TAX_RATE = 0.0825
    bill_with_tax = get_float("Enter the bill with tax: $", limit=(1, 9e9))

    data = [("Tip %", "Total Due")] # table header

    for tip_rate in [0.100, 0.125, 0.150, 0.175, 0.200, 0.225, 0.250]:
        total = get_total_due(bill_with_tax, TAX_RATE, tip_rate)
        data += [ ( format(tip_rate * 100, '.2f'), format(total, ',.2f') ) ]

    print_table(data, options={'col_align': {1: '^', 2: '>'}})

main()
