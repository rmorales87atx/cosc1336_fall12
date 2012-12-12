# zellers_enhanced.py
# Reads in dates from the user and converts the date to the 
# corresponding day of the week.

import datetime

# Utility functions

def printf(spec, *args, end="\n"):
    """
    Formatted printing function. Calls the format method on the str object
    in `spec` with the given arguments.
    """
    print(spec.format(*args), end=end)

def try_cast(value, convert, default=None):
    """
    Attempts to convert a value given a type. If the conversion fails by way
    of a ValueError exception, the specified default value is returned.
    """
    try:
        return convert(value)
    except ValueError:
        return default

# Main program class

class Application:
    """
    Main class for the Lab09 Problem1 program.
    """
    def __init__(self):
        """
        Constructor initializing the Application instance.
        """
        self.__days_of_week = ('Saturday', 'Sunday', 'Monday',
                               'Tuesday', 'Wednesday', 'Thursday',
                               'Friday')

        self.__date_prompt = "Enter a date (format MM/DD/YYYY): "

    def parse_date(self):
        """
        Query the user to enter a date in MM/DD/YYYY format.
        The input is parsed and returned as a datetime.date object.

        None is returned if the user cancels input by pressing
        Ctrl+C.
        """
        while True:
            prompt = self.__date_prompt
            try:
                parts = input(prompt).split('/')
                if len(parts) != 3:
                    raise ValueError('unrecognizable data entry')

                i = iter(parts)
                month = try_cast(next(i), int)
                day = try_cast(next(i), int)
                year = try_cast(next(i), int)

                # all input validation is handled
                # by datetime.date(), which raises
                # TypeError or ValueError
                #
                # if the user enters a 2-digit year
                # instead of a 4-digit year, this is
                # actually accepted by datetime.date

                return datetime.date(year, month, day)
            except (ValueError, TypeError) as err:
                printf("Invalid input: {}.", err)
                print("Check your typing and try again.")
                print()
            except KeyboardInterrupt:
                return None

    def calc_day_index(self, date):
        """ Converts a date to an index indicating the day of the week. """
        m, y = date.month, date.year
        if m < 3:
            m += 12
            y -= 1
        j = y // 100
        k = y % 100
        return (date.day + ((m+1)*26)//10 + k + k//4 + j//4 - 2*j) % 7

    def day_of_week(self, date):
        """ Calculates day of the week given a particular date. """
        i = self.calc_day_index(date)
        return self.__days_of_week[i]

    def is_date_past(self, date):
        """ Determines if the given date is in the past. """
        today = datetime.date.today()
        return date < today

    def get_date_tense(self, date):
        """
        Returns an English word describing the date's past or future
        tense.
        """
        if self.is_date_past(date):
            return "was"
        else:
            return "is"

    def run(self):
        self.__date_prompt = "Enter a date (format MM/DD/YYYY), " \
                             "or Ctrl+C to quit: "

        for date in iter(self.parse_date, None):
            printf("{} {} a {}.", date, self.get_date_tense(date),
                   self.day_of_week(date))

app = Application()
app.run()
