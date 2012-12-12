#
# COSC 1336 Problem 3 (enhanced)
# Robert Morales
#

import datetime
from datetime import date
import random

def parse_date(txt):
    try:
        return datetime.datetime.strptime(txt, "%m/%d/%y")
    except ValueError:
        return None

def get_all_magic_dates():
    result = []

    for year in range(100):
        is_leap = (year % 4) == 0 or (year % 400 == 0 and year % 100 == 0)
        for month in range(1, 13):
            for day in range(1, 32):
                try:
                    temp = date(1900+year, month, day)
                    if month * day == year:
                        result += [temp]
                except ValueError:
                    pass # ignore it

    return result

def main():
    data = None

    while data is None:
        data = parse_date(input("Enter a date in the format 'MM/DD/YY': "))

        if data is None:
            print("You entered an invalid date. Try again.")
            continue

        magic_value = 1900 + (data.month * data.day)

        if magic_value == data.year:
            print("This date is magic!")
        else:
            print("This date is not magic.")

        all_dates = get_all_magic_dates()

        print()
        print("Here are all", len(all_dates), "magic dates:")

        count = 1
        for date in all_dates:
            print(date.strftime("%m/%d/%y"), " ", end="")

            if (count % 6) == 0:
                print()

            count += 1

main()
