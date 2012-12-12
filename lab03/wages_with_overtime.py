#
# COSC 1336 Lab 3 Problem 1
# Robert Morales
#
# PROGRAM DESCRIPTION:
#   Calculates an employee's pay, including overtime compensated at 1.5 times
#   the employee's wage.
#
# INPUT:
#   1) Employee's hourly pay rate
#   2) Number of hours worked last week
#
# OUTPUT:
#   1) Employee's total wages
#
# PROCESS:
#   1) Input hours worked.
#   2) Input hourly pay rate.
#   3) If hours worked is greater than 40, calculate overtime pay by
#      multiplying the employee's hourly rate by 1.5 by the number of hours
#      over 40. Then add this overtime pay to the current wages.
#   4) If hours worked is less than or equal to 40, calculate wages by
#      multiplying hours worked by hourly pay rate.
#   5) Display the calculated wages.
#
# KNOWN BUGS:
#   1) Accepts negative inputs.
#   2) Accepts zero as input for the hourly rate.
#   3) Accepts input greater than 168 for hours worked.
#   4) Accepts input less than the legal minimum wage for the hourly rate.

HOURS_PER_WEEK = 40
OVERTIME_RATE = 1.5

def print_money(value):
    print("$", format(value, ",.2f"), sep="", end="")

def main():
    hours_worked = float(input("Enter the hours worked last week: "))
    pay_rate = float(input("Enter the employee's hourly rate: $"))
    wages = 0.0

    if hours_worked > HOURS_PER_WEEK:
        overtime_hours = hours_worked - HOURS_PER_WEEK
        overtime_pay = pay_rate * 1.5 * overtime_hours
        wages = HOURS_PER_WEEK * pay_rate + overtime_pay
    else:
        wages = hours_worked * pay_rate

    print("Employee's wages: ", end="")
    print_money(wages)
    print()

main()
