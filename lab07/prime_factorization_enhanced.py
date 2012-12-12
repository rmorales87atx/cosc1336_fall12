# COSC 1336, Lab 7, Problem 2 (enhanced)
# Robert Morales

from math import sqrt
from sys import stderr

def is_prime(num):
    factors = [x for x in range(2, int(sqrt(num)+1)) if num % x == 0]
    return len(factors) == 0

def prime_factor_power(num, p):
    if p == 0:
        return 0

    x = num
    count = 0

    while x % p == 0:
        count += 1
        x = x // p

    return count

def display_factorization(num):
    try:
        pairs = [ (x, e) for x in range(2, num) if is_prime(x) \
                  for e in [prime_factor_power(num, x)] if e > 0 ]
        sep = ' * '
        print(sep.join(['{:,}**{}'.format(num, exp) for num, exp in pairs]))
    except KeyboardInterrupt:
        print("Factorization cancelled!", file=stderr)
        return

def main():
    num = int(input("Enter a number (0 to quit): "))

    while num > 0:
        if is_prime(num):
            print("{:,} is prime".format(num))
        else:
            print("Prime factorization of {:,} is:".format(num))
            display_factorization(num)

        print()
        num = int(input("Enter another number (or 0 to quit): "))

main()
