# temp_convert.py
# Converts temperatures from one set of units to another.
# Converts between Celsius, Fahrenheit, and Kelvin
#
# Written by Robert Morales, 6-NOV-2012

# FUNCTION: get_temperature_unit
# PURPOSE: Queries the user for a temperature unit. The input is validated
#          and will return either 'c', 'f', or 'k'.
def get_temperature_unit(prompt):
    unit = input(prompt + " (c/f/k): ")

    while not (unit == 'c' or unit == 'f' or unit == 'k'):
        print("Invalid unit; must be one of: c, f, k.")
        unit = input(prompt + " (c/f/k): ")

    return unit

# FUNCTION: read_temperature_info
# PURPOSE: Gathers user input, validates, and returns 3 values.
# INPUT:
#   From the user:
#     1. Temperature value to be converted;
#     2. Current unit of the temperature just entered;
#     3. Desired unit that the temperature should be converted to.
#   Parameters:
#     sentinel: If non-zero, the function will return without further
#               prompting the user for input if the temperatured entered
#               matches this value.
#     temperature_prompt:
#               String specifying the prompt to be used when querying the
#               user for a temperature value.
# OUTPUT:
#   1. User's input for temp. value (not validated)
#   2. Temperature's current unit
#   3. Temperature's desired unit
def read_temperature_info(sentinel = 0, \
                          temperature_prompt = "Enter temperature (without unit): "):
    value = float(input(temperature_prompt))

    if sentinel != 0 and value == sentinel:
        return value, '', ''

    current = get_temperature_unit("Enter current temperature unit")
    desired = get_temperature_unit("Enter desired temperature unit")
    return value, current, desired

# FUNCTION: convert_to_celsius
# PURPOSE: Converts a given temperature to Celsius.
# INPUT:
#   1. Current temperature value
#   2. Current temperature unit
# OUTPUT:
#   1. Temperature converted to Celsius
def convert_to_celsius(temperature, current_unit):
    if current_unit == 'c':
        return temperature # already in Celsius
    elif current_unit == 'k':
        return temperature - 273.15
    elif current_unit == 'f':
        return (temperature - 32) * (5/9)
    else:
        return "bork"

# FUNCTION: convert_from_celsius
# PURPOSE: Converts a given temperature from Celsius.
# INPUT:
#   1. Current temperature value
#   2. Desired temperature unit
# OUTPUT:
#   1. Temperature converted to specified unit
def convert_from_celsius(temperature, desired_unit):
    if desired_unit == 'c':
        return temperature
    elif desired_unit == 'k':
        return temperature + 273.15
    elif desired_unit == 'f':
        return (temperature * (9/5)) + 32
    else:
        return "bork"

# FUNCTION: convert_temperature
# PURPOSE: Converts the specified temperature to the desired units.
# INPUT:
#   1. Current temperature value
#   2. Current temperature unit
#   3. Desired temperature unit
# OUTPUT:
#   1. Temperature converted to specified unit
def convert_temperature(temperature, current_unit, desired_unit):
    temp = convert_to_celsius(temperature, current_unit)
    return convert_from_celsius(temp, desired_unit)

# FUNCTION: main
# PURPSOE: Program entry point.
def main():
    sentinel = -999
    prompt = "Enter temperature (without unit), or -999 to quit: "

    temperature, current_unit, desired_unit = \
                 read_temperature_info(sentinel, prompt)

    while temperature != sentinel:
        result = convert_temperature(temperature, current_unit, desired_unit)
        print(temperature, current_unit, " == ", result, desired_unit, sep="")

        temperature, current_unit, desired_unit = \
                     read_temperature_info(sentinel, prompt)

# END OF PROGRAM
main()

##for x in [100, 0, 37, 21.11]:
##    print("{:>6}".format(x), end=": ")
##    for y in ['f', 'k']:
##            z = convert_from_celsius(x, y)
##            print("{:>6.2f}".format(z), end=" ")
##    print()
