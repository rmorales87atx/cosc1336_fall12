#
# COSC 1336 Lab 3 Problem 1 (enhanced)
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

################################################################################
# Global constants
################################################################################

HOURS_PER_WEEK = 40
OVERTIME_RATE = 1.5
MAX_HOURS_IN_WEEK = 168
MINIMUM_WAGE = 7.25
MAXIMUM_WAGE = 100.00 # All programs should reasonably limit their input

################################################################################

#
# FUNCTION: format_money
# PURPOSE: Formats a given value as U.S. currency and returns the
#          formatted string.
#
def format_money(value):
    return "$" + format(value, ",.2f")

#
# FUNCTION: get_hours_worked
# PURPOSE: Collects input from the user. Rejects input that is outside the
#          range [1, HOURS_PER_WEEK].
#
def get_hours_worked():
    result = -1

    while (result < 0.0) or (result > MAX_HOURS_IN_WEEK):
        try:
            result = float(input("Enter the hours worked last week: "))

            if result < 0:
                print("Hours worked must be greater than zero.")
            elif result > MAX_HOURS_IN_WEEK:
                print("Hours worked cannot exceed:", MAX_HOURS_IN_WEEK)
            
        except ValueError:
            result = -1

    return result

#
# FUNCTION: get_hourly_rate
# PURPOSE: Collects input from the user. Rejects input that is outside the
#          range [MINIMUM_WAGE, MAXIMUM_WAGE].
#
def get_hourly_rate():
    result = 0

    while (result < MINIMUM_WAGE) or (result > MAXIMUM_WAGE):
        try:
            result = float(input("Enter the employee's hourly rate: $"))

            if result < MINIMUM_WAGE:
                print("Hourly rate cannot be less than the current legal minimum wage:", format_money(MINIMUM_WAGE))
            elif result > MAXIMUM_WAGE:
                print("Company policy #123.45 limits hourly wages to:", format_money(MAXIMUM_WAGE))
        except ValueError:
            result = 0

    return result

#
# FUNCTION: get_overtime_pay
# PURPOSE: Given the hours worked, determines if any overtime pay is to be
#          calculated.
# INPUT:
#   1) hours_worked: The amount of hours worked in the week.
#   2) pay_rate: The hourly pay rate.
# OUTPUT:
#   1) Zero if there is no overtime (hours_worked <= HOURS_PER_WEEK)
#   -- OR --
#   2) The overtime wages for the overtime hours.
#
def get_overtime_pay(hours_worked, pay_rate):
    if hours_worked > HOURS_PER_WEEK:
        return (pay_rate * 1.5) * (hours_worked - HOURS_PER_WEEK)
    else:
        return 0

#
# FUNCTION: main
# PURPOSE: Program entry point.
#
def main():
    hours_worked = get_hours_worked()
    pay_rate = get_hourly_rate()
    wages = min(hours_worked, HOURS_PER_WEEK) * pay_rate
    wages += get_overtime_pay(hours_worked, pay_rate)

    print("Employee's wages:", format_money(wages))

################################################################################

main()
