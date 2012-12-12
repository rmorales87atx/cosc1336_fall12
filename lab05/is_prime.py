# COSC 1336, Lab 5, Problem 2
# Robert Morales (0849639)

def display_is_prime(num):
    is_prime = True

    for x in range(2, num):
        if (num % x == 0):
            is_prime = False
            break

    if is_prime:
        print(num, "is prime")
    else:
        print(num, "is not prime (composite)")

def main():
    run = True
    while run:
        number = int(input("Enter a number: "))
        display_is_prime(number)

        print()
        response = input("Test another number? ")

        if response not in ['Y', 'y', 'yes']:
            run = False

main()
