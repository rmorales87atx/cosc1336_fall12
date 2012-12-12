#
# COSC 1336 Problem 3
# Robert Morales
#
# ┌────────────────┬────────────────────────────────────────────────┬──────────┐
# │ INPUT          │ PROCESS                                        │ OUTPUT   │
# ├────────────────┼────────────────────────────────────────────────┼──────────┤
# │ month          │ 1) Gather all input                            │ message  │
# │ day            │ 2) Calculate the 'magic' value by multiplying  │          │
# │ year (2─digit) │    month by day.                               │          │
# │                │ 3) Determine if the magic value is equal to    │          │
# │                │    the year.                                   │          │
# │                │    a. If the magic value is equal to the year  │          │
# │                │       set the message to "This date is magic!" │          │
# │                │    b. Otherwise set the message to             │          │
# │                │       "This date is not magic."                │          │
# │                │ 4) Print the message.                          │          │
# └────────────────┴────────────────────────────────────────────────┴──────────┘
#
# KNOWN BUGS:
#   1) Accepts negative inputs.
#   2) Does not validate that year is, in fact, a two-digit year.

def main():
    month = int(input("Enter the month: "))
    day = int(input("Enter the day: "))
    year = int(input("Enter the two-digit year: "))

    message = ""
    magic_value = month * day

    if magic_value == year:
        message = "This date is magic!"
    else:
        message = "This date is not magic."

    print()
    print(message)

main()
