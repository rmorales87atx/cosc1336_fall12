# COSC 1336, Lab 7, Problem 2
# Robert Morales

from math import sqrt

def is_prime(num):
    limit = int(sqrt(num)+1)
    for x in range(2, limit):
        if (num % x == 0):
            return False
    return num > 1

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
    product = 1
    for p in range(2, num):
        if is_prime(p):
            e = prime_factor_power(num, p)
            if e > 1:
                print("{:,}^{}".format(p, e), end=' ')
            elif e == 1:
                print("{:,}".format(p), end=' ')

            # some optimizations to end the search faster
            # for large numbers

            if p**e == num:
                break

            product *= (p**e)
            if product == num:
                break
    print()

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
