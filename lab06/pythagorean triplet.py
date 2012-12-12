# COSC 1336, Lab 6, Problem 4
# Robert Morales

from math import sqrt

def main():
    a,b,c = find_triplet(1000) # returning multiple values is in the book
                               # (p. 224-225)

    if a != 0 and b != 0 and c != 0:
        print(a, "+", b, "+", c, "=", a+b+c)
    else:
        print("Bork bork bork!!")

def find_triplet(search):
    # given that a < b < c:
    # a can never be >= search//3
    # b can never be >= search//2

    for a in range(1, (search//3)+1):
        for b in range(a+1, (search//2)+1):
            c = search - a - b
            if (a**2 + b**2) == c**2 and (c > 0):
                return a, b, c

    return 0, 0, 0

main()
