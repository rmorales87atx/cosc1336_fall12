################################################################################
# COSC 1336, Lab 4 Problem 1(a)
# Robert Morales (0849639)
################################################################################
# Test cases:
#
# +--------------+----------+---------------+--------+
# | num_packages | discount | discount_rate | price  |
# +--------------+----------+---------------+--------+
# | 0            | 0.0      | 0.0           | 0.0    |
# | 1            | 0.0      | 0.0           | 99.0   |
# | 9            | 0.0      | 0.0           | 891.0  |
# | 10           | 198.0    | 0.2           | 792.0  |
# | 19           | 376.2    | 0.2           | 1504.8 |
# | 20           | 594.0    | 0.3           | 1386.0 |
# | 49           | 1455.3   | 0.3           | 3395.7 |
# | 50           | 1980.0   | 0.4           | 2970.0 |
# | 99           | 3920.4   | 0.4           | 5880.6 |
# | 101          | 4999.5   | 0.5           | 4999.5 |
# +--------------+----------+---------------+--------+
#
# Known bugs:
#   1) Accepts negative values for input.
################################################################################

def main():
    PRICE_PER_PACKAGE = 99.0
    num_packages = int(input("Enter the number of packages purchased: "))
    price = PRICE_PER_PACKAGE * num_packages
    discount_rate = 0.0

    if num_packages >= 100:
        discount_rate = 0.5
    else:
        if num_packages >= 50:
            discount_rate = 0.4
        else:
            if num_packages >= 20:
                discount_rate = 0.3
            else:
                if num_packages >= 10:
                    discount_rate = 0.2
                    # whew

    if discount_rate > 0:
        discount = price * discount_rate
        price -= discount

        # I chose to write both the discount amount with the percentage rate.
        # Customers like dollars n 'cents.
        print("You saved: $", format(discount, ",.2f"),
              '(', format(discount_rate, '.0%'), ')')

    print("Price: $", format(price, ",.2f"))

main()
