#
# COSC 1336 Problem 2
# Robert Morales
#

def main():
    first = input("Enter a name: ")
    second = input("Enter another name: ")

    if first > second:
        print(second, "comes before", first)
    else:
        print(second, "comes after", first)

main()
