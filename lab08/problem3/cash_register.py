# COSC 1336, Lab 8, Problem 2
# Robert Morales

# KNOWN BUGS:
# 1. If an item name is greater than the constant WIDTH, it screws up
#    the receipt.
# 2. Numbers no longer line up if a price is greater than 99.
# 3. Negative inputs are accepted for prices.

# global "constants"
WIDTH = 30
TAX_RATE = 0.0825

# prints a line of n symbols
def print_line(file, symbol = '', n = 0):
    print(symbol*n, file=file)

# prints the message, centered, with one symbol before and after
def print_boxed_text(file, symbol, text, n):
    print("{0}{1:{fill}^{width}}{0}".format(symbol, text, fill=' ', width=n-2),\
          file=file)

# prints a message in a box as the top of the receipt
def print_receipt_preamble(file):
    ch = "*"
    print_line(file, ch, WIDTH)
    print_boxed_text(file, ch, "Welcome to", WIDTH)
    print_boxed_text(file, ch, "Cafe Python!", WIDTH)
    print_line(file, ch, WIDTH)
    print_line(file)

# prints a single item and price
def print_item_line(file, item, price):
    print("{0:.<{width}}${1:5.2f}".format(item, price, width=WIDTH-6), \
          file=file)

# prints the subtotal, tax, and total due
def print_totals(file, total):
    print_line(file)
    print_item_line(file, "Subtotal", total)
    tax = total * TAX_RATE
    print_item_line(file, "Tax", tax)
    print_line(file, "-", WIDTH)
    total_with_tax = total + tax
    print_item_line(file, "Total", total_with_tax)

    return total_with_tax

# prints the amount paid and the change due
def print_change(file, due, paid):
    print_line(file)
    print_item_line(file, "Amount paid", paid)
    print_item_line(file, "Change due", paid-due)

def main():
    file = open('receipt.txt', 'w')

    print_receipt_preamble(file)
    total = 0
    item = input("Enter the item name (blank to quit): ")

    while item != "":
        price = float(input("Enter the price for {}: $".format(item)))
        total += price
        print_item_line(file, item, price)
        item = input("Enter the next item name (blank to quit): ")

    total_with_tax = print_totals(file, total)
    print("\nTotal due: ${:5.2f}".format(total_with_tax))
    paid = float(input("Enter the total paid by customer: $"))

    while paid < total_with_tax:
        paid = float(input("I'm sorry, that's not enough.  Try again: $"))

    print("Change due: ${:5.2f}".format(paid-total_with_tax))
    print_change(file, total_with_tax, paid)

    file.close()

main()
