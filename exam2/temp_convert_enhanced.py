# temp_convert_enhanced.py
# Converts temperatures from one set of units to another.
# Converts between Celsius, Fahrenheit, and Kelvin
#
# Written by Robert Morales, 7-NOV-2012

from io_util import get_float, get_str, printf
import functools

@functools.total_ordering
class Temperature:
    def __init__(self, value, unit):
        if unit not in 'CcFfKk':
            raise ValueError('invalid unit')

        self.__value = value
        self.__unit = str(unit).upper()

    def __repr__(self):
        return 'Temperature({!r}, {!r})'.format(self.__value, self.__unit)

    def str(self, num_digits = 2):
        return '{:.{digits}f}{}'.format(self.value(), self.__unit, \
                                        digits=num_digits)

    def __str__(self):
        return self.str()

    def value(self):
        return float(self.__value)

    def unit(self):
        return str(self.__unit)

    def is_celsius(self):
        return self.unit() == 'C'

    def is_fahrenheit(self):
        return self.unit() == 'F'

    def is_kelvin(self):
        return self.unit() == 'K'

    def set_celsius(self, value):
        self.__value = value
        self.__unit = 'C'

    def set_kelvin(self, value):
        self.__value = value
        self.__unit = 'K'

    def set_fahrenheit(self, value):
        self.__value = value
        self.__unit = 'F'

    def to_celsius(self):
        if self.is_celsius():
            return self
        elif self.is_kelvin():
            return Temperature(self.value() - 273.15, 'C')
        elif self.is_fahrenheit():
            return Temperature((self.value() - 32) * (5/9), 'C')

    def to_kelvin(self):
        temp = self.to_celsius()
        return Temperature(temp.value() + 273.15, 'K')

    def to_fahrenheit(self):
        temp = self.to_celsius()
        return Temperature((temp.value() * (9/5)) + 32, 'F')

    def convert(self, desired_unit):
        if desired_unit == 'C':
            return self.to_celsius()
        elif desired_unit == 'F':
            return self.to_fahrenheit()
        elif desired_unit == 'K':
            return self.to_kelvin()
        else:
            raise ValueError('invalid unit')

    #### relational operator implementations ####

    def __eq__(self, other):
        comp = other.convert(self.unit())
        return self.value() == comp.value() and self.unit() == comp.unit()

    def __lt__(self, other):
        comp = other.convert(self.unit())
        return self.value() < comp.value() and self.unit() == comp.unit()

    # @functools.total_ordering automatically generates
    # the other relational operator methods

# FUNCTION: get_temperature_unit
# PURPOSE: Queries the user for a temperature unit. The input is validated
#          and will return either 'C', 'F', or 'K'; None is returned if the
#          user cancels input by pressing Ctrl+C.
def get_temperature_unit(prompt):
    try:
        unit = input(prompt + " (C/F/K): ")

        while unit not in 'CcFfKk':
            print("Invalid unit; must be one of: C, F, K.")
            unit = input(prompt + " (C/F/K): ")

        return unit
    except KeyboardInterrupt:
        return None

# FUNCTION: main
# PURPSOE: Program entry point.
def main():
    try:
        prompt = "Enter temperature (without unit), or Ctrl+C to quit: "

        for value in iter(lambda: float(input(prompt)), None):
            unit = get_temperature_unit("Enter current temperature unit")

            if unit is None:
                break

            temp = Temperature(value, unit)

            new_unit = get_temperature_unit("Enter desired temperature unit")

            if new_unit is not None:
                printf('{} = {}', temp, temp.convert(new_unit))
    except ValueError:
        print("Invalid input. Try again.")
        print()
    except KeyboardInterrupt:
        pass

# END OF PROGRAM
main()

##for v in [100, 0, 37, 21.11]:
##    t = Temperature(v, 'C')
##    f = t.to_fahrenheit()
##    k = t.to_kelvin()
##    printf("{:>8} {:>8} {:>8}", t, f, k)
