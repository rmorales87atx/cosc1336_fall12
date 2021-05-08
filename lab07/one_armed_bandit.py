# COSC 1336, Lab 7, Problem 3
# Robert Morales

from random import randrange

# FUNCTION: get_bet
# PURPOSE: Asks for, and returns, the amount of the user's bet.
# INPUT: amount of bet to place
# OUTPUT: float number which is always > 0
# KNOWN BUGS: doesn't handle conversion error (ValueError) or the
#             'interrupt key' (KeyboardInterrupt)
def get_bet():
    result = float(input("How much do you want to bet? "))

    while result <= 0:
        print("Enter a non-zero positive number.")
        result = float(input("How much do you want to bet? "))

    return result

# FUNCTION: get_random_symbol
# PURPOSE: Selects a symbol using the random number generator.
# INPUT: none
# OUTPUT: A string containing the randomly selected symbol.
def get_random_symbol():
    selector = randrange(6)

    if selector == 0:
        return "Cherries"
    elif selector == 1:
        return "Oranges"
    elif selector == 2:
        return "Plums"
    elif selector == 3:
        return "Bells"
    elif selector == 4:
        return "Melons"
    elif selector == 5:
        return "Bars"

# FUNCTION: pull_lever
# PURPOSE: Selects three random symbols and returns the amount won.
# INPUT: the user's current bet.
# OUTPUT: one of three possibilities:
#           1) all three symbols match: 20 times the current bet
#           2) only two symbols: twice the current bet
#           3) no symbols match: zero
def pull_lever(current_bet):
    sym1 = get_random_symbol()
    sym2 = get_random_symbol()
    sym3 = get_random_symbol()

    print(sym1, sym2, sym3)

    if sym1 == sym2 == sym3:         # curiously this does work
        return 20 * current_bet
    elif sym1 == sym2 or sym1 == sym3 or sym2 == sym3:
        return 2 * current_bet
    else:
        return 0

# FUNCTION: print_stats
# PURPOSE: Prints game statistics.
# INPUT: The user's total bets, total winnings, and the number of plays.
# OUTPUT: Inputs formatted and written to console, including a calculated
#         gross profit and percentage payout.
def print_stats(total_bet, total_won, num_plays):
    print()
    print("==== END OF GAME STATISTICS ====")
    print("Number of plays: {:,}".format(num_plays))
    print("Total bet: ${:,.2f}".format(total_bet))
    print("Total won: ${:,.2f}".format(total_won))
    print("Gross profit: ${:,.2f}".format(total_won - total_bet))

    if total_bet > 0:
        print("Payout %: {:.1f}".format(100 * (total_won / total_bet)))

# FUNCTION: get_yes_or_no
# PURPOSE: Queries the user for a 'yes' or 'no' answer, given a prompt.
# INPUT: Prompt to the user, which is automatically appended with " (y/n) ".
# OUTPUT: Returns True if the user enters 'y', False otherwise.
# KNOWN BUGS: only accepts lowercase input;
#             doesn't handle 'interrupt key' (KeyboardInterrupt)
def get_yes_or_no(prompt):
    response = input(prompt + " (y/n) ")

    while response != 'y' and response != 'n':
        response = input(prompt + " (y/n)")

    return response == 'y'

# FUNCTION: main
# PURPOSE: Program entry point.
def main():
    total_won = 0
    total_bet = 0
    keep_going = True
    num_plays = 0

    while keep_going:
        print()
        bet = get_bet()
        num_plays += 1
        print("Play #{}: ".format(num_plays), end="")
        won = pull_lever(bet)

        total_won += won
        total_bet += bet

        print("You won ${:,.2f}; Balance: ${:,.2f}".format(won, total_won - total_bet))

        keep_going = get_yes_or_no("Again?")

    print_stats(total_bet, total_won, num_plays)

main()
