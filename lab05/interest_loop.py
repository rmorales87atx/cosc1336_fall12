# COSC 1336, Lab 5, Problem 3
# Robert Morales (0849639)

def balance_display_loop(start_balance, interest_rate, num_months):
    balance = start_balance
    for n in range(1, num_months+1):
        balance *= (1 + interest_rate)

        if n == 1:
            print("Balance after 1 month: $", format(balance, ".2f"), sep="")
        else:
            print("Balance after ", n, " months: $", format(balance, ".2f"), sep="")

def main():
    start = float(input("Enter the starting account balance: $"))
    int_rate = float(input("Enter the interest rate (from 1-100): "))
    months = int(input("Enter the number of months: "))

    int_rate /= 100
    balance_display_loop(start, int_rate, months)

main()
