# COSC 1336, Lab 6, Problem 2
# Robert Morales

################################################################################
# holy massive code block, batman!
##def main():
##    month = int(input("Enter the month number (1-12): "))
##    while month < 1 or month > 12:
##        print(month, "is not between 1 and 12.")
##        month = int(input("Enter the month number (1-12): "))
##    day = int(input("Enter the day of the month: "))
##    year = int(input("Enter the year: "))
##    if month == 1 or month == 3 or month == 5 or month == 7 or \
##       month == 8 or month == 10 or month == 12:
##        max_day = 31
##    elif month == 4 or month == 6 or month == 9 or month == 11:
##        max_day == 30
##    elif year % 4 == 0:
##        max_day = 29
##    else:
##        max_day = 28
##    while day < 1 or day >= max_day:
##        print("The day should between 1 and", max_day)
##        day = int(input("Enter the day of the month: "))
##
##    if month * day == year % 100:
##        print(month,"/",day,"/",year," is magic!",sep="")
##    else:
##        print(month,"/",day,"/",year," is not magic.",sep="")
################################################################################

# get_month
#   output: Integer value containing the user's input,
#           guaranteed to be a valid month (1-12).
def get_month():
    prompt = "Enter the month (1-12), or 0 to cancel: "
    result = int(input(prompt))

    while not (0 <= result <= 12):
        print("Invalid entry.")
        print()
        result = int(input(prompt))

    return result

# get_day
#   output: Integer value containing the user's input.
def get_day():
    prompt = "Enter the day of the month: "
    result = int(input(prompt))

    while not (1 <= result <= 31):
        print("Invalid entry.")
        print()
        result = int(input(prompt))

    return result

# get_year
#   output: Integer value containing the user's input.
def get_year():
    return int(input("Enter the year: "))

# is_leap_year
#   input: An integer specifying a 4-digit year
#   output: Boolean value determining if the year is a leap year.
def is_leap_year(value):
    # Using the Gregorian calendar as the standard:
    # Leap years are divisible by 4, EXCEPT for any leap year
    # that is a multiple of 100 (unless it is also a multiple of 400).

    if value % 400 == 0:
        return True
    elif value % 100 == 0:
        return False
    else:
        return value % 4 == 0

# days_in_month
#   input: Current month and year
#   output: Integer value containing the maximum number of days
#           for the specified month (and year).
def days_in_month(month, year):
    if month == 1 or month == 3 or month == 5 or month == 7 or \
       month == 8 or month == 10 or month == 12:
        return 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif is_leap_year(year):
        return 29
    else:
        return 28

# is_valid_date
#   input: Month, day, and year (int values)
#   output: Boolean value determining if the values all conform to
#           a valid date.
def is_valid_date(month, day, year):
    max_days = days_in_month(month, year)
    return (1 <= month <= 12) and (1 <= day <= max_days) and \
           (0 <= year <= 9999)

# is_date_magic
#   input: Month, day, and year to be checked. These values are assumed
#          to be properly formed.
#   output: Boolean value which determines if month*day equals the year.
def is_date_magic(month, day, year):
    return month * day == year

######################################################################

def main():
    month = get_month()

    while month != 0:
        day = get_day()
        year = get_year()

        if not is_valid_date(month, day, year):
            print("Invalid data.")
        elif is_date_magic(month, day, year%100):
            print(month, "/", day, "/", year, " is magic!", sep="")
        else:
            print(month, "/", day, "/", year, " is not magic.", sep="")

        print()
        month = get_month()

main()
