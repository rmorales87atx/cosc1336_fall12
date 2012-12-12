# COSC 1336, Lab 5, Problem 3 (enhanced)
# Robert Morales (0849639)

from table_printer import print_table  # used to print a pretty table
from io_util import get_float, get_int # used for input validation

def balance_display_loop(start_balance, interest_rate, num_months):
    balance = start_balance
    data = [("Months", "Balance")] # table header

    for n in range(1, num_months+1):
        balance *= (1 + interest_rate)
        data += [(n, "$"+format(balance, ".2f"))]

    print_table(data, options={'col_align': {1: '^', 2: '>'}})

def main():
    start = get_float("Enter the starting account balance: $", limit=(1,9e9))
    int_rate = get_float("Enter the interest rate (from 1-100): ", limit=(1,101))
    months = get_int("Enter the number of months: ", limit=(1,121))

    int_rate /= 100
    balance_display_loop(start, int_rate, months)

main()
