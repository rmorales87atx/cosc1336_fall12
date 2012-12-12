# COSC 1336, Lab 4 Problem 2
# Robert Morales

def print_total_due_logical(weight):
#
# The original version of this code was buggy in the sense that it set
# the rate to "3.7" for every weight that was under 10.
#
# +----------+--------+---------+
# | weight   | rate   | total   |
# +----------+--------+---------+
# | 1.0      | 3.7    | 3.7     |
# +----------+--------+---------+
#
# The correct output should be:
#
# +----------+--------+---------+
# | weight   | rate   | total   |
# +----------+--------+---------+
# | 1.0      | 1.1    | 1.1     |
# +----------+--------+---------+
#
    if weight <= 2:
        rate = 1.1
    if 2 < weight <= 6:
        rate = 2.2
    if 6 < weight <= 10:
        rate = 3.7
    if weight > 10:
        rate = 3.8
    total = weight * rate
    print("Total due: $", format(total, ".2f"))

def print_total_due_elif(weight):
    if weight <= 2:
        rate = 1.1
    elif weight <= 6:
        rate = 2.2
    elif weight <= 10:
        rate = 3.7
    elif weight > 10:
        rate = 3.8
    total = weight * rate
    print("Total due: $", format(total, ".2f"))

def main():
    w = float(input("Enter the weight of the package: "))

    if w >= 0:
        print_total_due_elif(w)
    else:
        print("Check your typing and try again.")

main()
