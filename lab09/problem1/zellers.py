# zellers.py
# Reads in dates from the user and converts the date to the 
# corresponding day of the week.

# main: reads in dates from the user, converts them to the corresponding
#       day of the week, and displays the result.
def main():
    days_of_week = ('Satur', 'Sun', 'Mon', 'Tues', 'Wednes', 'Thurs', 'Fri')
    month, day, year = read_date()
    while month != 0:
        i = calc_day_index(month, day, year)
        week_day = days_of_week[i] + 'day'
        date_str = date_to_str(month, day, year)
        print(date_str, "is/was a", week_day)
        month, day, year = read_date()

# read_date: reads in the three numbers specifying a date from the user
#    input parameters: none
#    inputs from user: number for month, day, and year of a date
#    return values: validated month, day, and year numbers
def read_date():
    day_num, year_num = 0, 0
    month_num = validate_integer(
        "\nEnter the number of the month (zero to quit): ", 0, 12)
    if month_num != 0:
        max_day = get_num_days(month_num)
        day_num = validate_integer("Enter the day: ", 1, max_day)        
        year_num = int(input("Enter the year: "))
    while month_num != 0 and not valid_date(month_num, day_num, year_num):
        print("That date is not valid.")
        month_num = validate_integer(
            "Enter the number of the month (zero to quit): ", 0, 12)
        if month_num != 0:
            day_num = validate_integer("Enter the day: ", 1, 31)
            year_num = int(input("Enter the year: "))
    return month_num, day_num, year_num

# calc_day_index: converts a date to an index indicating the day of the week
#    input parameters: month, day, and year numbers indicating a date
#    return value: an index indicating the day of the week of the given date
#        0 means Saturday, 1 means, Sunday, etc.
def calc_day_index(month_num, day_num, year_num):
    m, y = month_num, year_num
    if m < 3:
        m += 12
        y -= 1
    j = y // 100
    k = y % 100
    return (day_num + ((m+1)*26)//10 + k + k//4 + j//4 - 2*j) % 7

# date_to_str: converts the numbers of a date into a string, for easy printing
#    input parameters: numbers for the month, day, and year
#    return value: a string in the MM/DD/YYYY format
def date_to_str(month, day, year):
    return format(month,"02d")+"/"+format(day,"02d")+"/"+format(year,"04d")

#### The rest of the functions are used by the provided functions, and 
#### don't need to be modified or called by your code

# validate_integer: reads in an integer from the user and validates it
#    input parameters: the prompt to display to the user, and the minimum
#        an maximum allowable values
#    return values: the valid inputs given by the user
def validate_integer(prompt, minimum, maximum):
    num = int(input(prompt))
    if num < minimum or num > maximum:
        num = int(input("Input must be between "+str(minimum)+" and "+
                        str(maximum)+".  Try again: "))
    return num

# get_num_days: returns the number of days in a particular month, allowing
#        for leap years.
#    input parameters: the numbers of a month and a year
#    return values: the number of days in the given month
def get_num_days(month_num, year_num = None):
    if month_num == 2:
        days = 28
        # if no year provided, allow it to go up to 29
        # not a leap year if it's a century unless it's divisible by 400
        if (year_num is None or 
            (year_num % 4 == 0 and 
             (year_num % 100 != 0 or year_num % 400 == 0))):
            days += 1
    elif month_num == 4 or month_num == 6 or month_num == 9 or month_num == 11:
        days = 30
    else:
        days = 31
    return days

# valid_date: determines whether a given date is valid
#     input parameters: month, day, and year numbers for a date
#     return value: a Boolean that is true if and only if the date
#         is valid.
def valid_date(month_num, day_num, year_num):
    max_days = get_num_days(month_num, year_num)
    return day_num <= max_days

main()
