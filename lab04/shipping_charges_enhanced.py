# COSC 1336, Lab 4 Problem 2 (enhanced)
# Robert Morales

from bisect import bisect

def get_shipping_rate(weight):
    rates = (1.1, 2.2, 3.7, 3.8)
    breakpoints = (0, 2, 6, 10)
    ins = bisect(breakpoints, weight)

    if ins == 0:
        return None
    else:
        return rates[ins-1]

def print_total_due(weight):
    rate = get_shipping_rate(weight)
    total = weight * rate
    print("Total due: $", format(total, ",.2f"), sep="")

def main():
    w = float(input("Enter the weight of the package: "))

    if w >= 0:
        print_total_due(w)
    else:
        print("Check your typing and try again.")

main()
