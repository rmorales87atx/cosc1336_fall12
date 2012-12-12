#
# COSC 1336 Problem 4
# Robert Morales
#
# PROGRAM DESCRIPTION:
#   Calculates the total due for a "Buy One, Get One 50% Off" sales program.
#
# INPUT:
#   1) Price of first item
#   2) Price of second item
#
# OUTPUT:
#   1) The total due, including discount on the second item.
#
# PROCESS:
#   1) Collect all input.
#   2) Determine the cheapest price of the two prices given.
#   3) Calculate the discount by multiplying the cheaper price by 50%.
#   4) Calculate the total due by adding both original prices and subtracting
#      the discount.
#   5) Print the total due.
#
# TEST CASE:
#   Given the following:
#     • Price of first item = 10.50
#     • Price of second item = 11.25
#   The first item is cheaper, so applying the discount to 10.50 gives us 5.25.
#   The program should therefore print a total due of 16.50 (5.25 + 11.25).
#
# KNOWN BUGS:
#   1) Accepts negative inputs for both prices.

DISCOUNT_RATE = 0.5

def main():
    first = float(input("Enter the price of the first item: $"))
    second = float(input("Enter the price of the second item: $"))
    cheapest = min(first, second)
    discount = cheapest * DISCOUNT_RATE
    total_due = (first + second) - discount

    print()
    print("Total due: $", format(total_due, ",.2f"), sep="")

main()
