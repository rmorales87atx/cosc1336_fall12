"""
COSC 1336, Lab 4 Problem 1(b)
Robert Morales (0849639)

Test cases:

+--------------+----------+---------------+--------+
| num_packages | discount | discount_rate | price  |
+--------------+----------+---------------+--------+
| 0            | 0.0      | 0.0           | 0.0    |
| 1            | 0.0      | 0.0           | 99.0   |
| 9            | 0.0      | 0.0           | 891.0  |
| 10           | 198.0    | 0.2           | 792.0  |
| 19           | 376.2    | 0.2           | 1504.8 |
| 20           | 594.0    | 0.3           | 1386.0 |
| 49           | 1455.3   | 0.3           | 3395.7 |
| 50           | 1980.0   | 0.4           | 2970.0 |
| 99           | 3920.4   | 0.4           | 5880.6 |
| 101          | 4999.5   | 0.5           | 4999.5 |
+--------------+----------+---------------+--------+

"""

from bisect import bisect
from random import randint

def money_str(n):
    """Formats a given value as U.S. currency."""
    return "$" + format(n, ",.2f")

def get_discount_rate(qty):
    RATES = (0.2, 0.3, 0.4, 0.5)
    BREAKPOINTS = (10, 20, 50, 100)

    ins = bisect(BREAKPOINTS, qty)

    if ins != 0:
        return RATES[ins-1]
    else:
        return 0.0

def print_total(qty):
    PRICE_PER_PACKAGE = 99.0
    price = PRICE_PER_PACKAGE * qty

    print()
    print("Quantity:", format(qty, ","))
    print("Subtotal:", money_str(price))

    discount_rate = get_discount_rate(qty)

    if discount_rate > 0:
        discount = price * discount_rate
        price -= discount

        # I chose to write both the discount amount with the percentage rate.
        # Customers like dollars n 'cents.
        print("You saved:", money_str(discount),
              '(' + format(discount_rate, '.0%') + ')')

    print("Price:", money_str(price))

def main():
    num_packages = int(input("Enter the number of packages purchased: "))

    if num_packages < 0:
        # run the test case values
        for x in (0, 1, 9, 10, 19, 20, 49, 50, 99, 101):
            print_total(x)
    else:
        print_total(num_packages)

main()
