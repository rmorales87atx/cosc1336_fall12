# shipping_charges_buggy.py
# A buggy implementation of Programming Exercise #9 in the textbook.
# For the lab, you will fix it in two different ways

def print_total_due(weight):
    if weight <= 2:
        rate = 1.1
    if weight <= 6:
        rate = 2.2
    if weight <= 10:
        rate = 3.7
    if weight > 10:
        rate = 3.8
    total = weight * rate
    print("Total due: $", format(total, ".2f"))

def main():
    w = float(input("Enter the weight of the package: "))
    print_total_due(w)

main()
