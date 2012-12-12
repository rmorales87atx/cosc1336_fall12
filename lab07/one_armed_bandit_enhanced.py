# COSC 1336, Lab 7, Problem 3 (enhanced)
# Robert Morales

from random import randrange

def get_bet():
    try:
        try:
            result = float(input("How much do you want to bet? "))
        except ValueError:
            result = 0

        while result <= 0:
            print("Enter a non-zero positive number.")
            try:
                result = float(input("How much do you want to bet? "))
            except ValueError:
                result = 0

        return result
    except KeyboardInterrupt:
        return None

def get_random_symbols(n = 1):
    items = ("Cherry", "Orange", "Plum", "Bell", "Melon", "Bar")
    return [ items[randrange(len(items))] for x in range(num) ]

def pull_lever(current_bet, no_print=False):
    sym1, sym2, sym3 = get_random_symbols(3)

    if not no_print:
        print(sym1, sym2, sym3)

    if sym1 == sym2 == sym3:         # curiously this does work
        return 20 * current_bet
    elif sym1 == sym2 or sym1 == sym3 or sym2 == sym3:
        return 2 * current_bet
    else:
        return 0

def print_stats(total_bet, total_won, num_plays):
    print()
    print("==== END OF GAME STATISTICS ====")
    print("Number of plays: {:,}".format(num_plays))
    print("Total bet: ${:,.2f}".format(total_bet))
    print("Total won: ${:,.2f}".format(total_won))
    print("Gross profit: ${:,.2f}".format(total_won - total_bet))

    if total_bet > 0:
        print("Payout %: {:.1f}".format(100 * (total_won / total_bet)))

def get_yes_or_no(prompt):
    try:
        response = input(prompt + " (y/n) ")

        while response not in ('Y', 'y', 'N', 'n'):
            response = input(prompt + " (y/n)")

        return response in ('Y', 'y')
    except KeyboardInterrupt:
        return None

def main():
    total_won = 0
    total_bet = 0
    keep_going = True
    count = 0

    while keep_going:
        print()
        bet = get_bet()

        if bet is not None:
            count += 1
            print("Play #{}: ".format(count), end="")
            won = pull_lever(bet)

            print("You won ${:,.2f}".format(won))

            total_won += won
            total_bet += bet

            keep_going = get_yes_or_no("Again?")
        else:
            keep_going = False

    print_stats(total_bet, total_won, count)

def auto_simulate():
    total_won = 0
    total_bet = 0
    count = 0

    for x in range(randrange(2, 42)):
        bet = randrange(1, 10000) / 100.0
        count += 1
        total_won += pull_lever(bet, no_print=True)
        total_bet += bet

    print_stats(total_bet, total_won, count)

main()
