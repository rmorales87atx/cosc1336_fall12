# COSC 1336, Lab 7, Problem 3 (enhanced)
# Robert Morales

from random import randrange

def printf(spec, *args, end="\n"):
    """
    Formatted printing function. Calls the format method on the str object
    in `spec` with the given arguments.
    """
    print(spec.format(*args), end=end)

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
    return [ items[randrange(len(items))] for x in range(n) ]

def pull_lever(current_bet):
    sym1, sym2, sym3 = get_random_symbols(3)

    print(sym1, sym2, sym3)

    if sym1 == sym2 == sym3:
        return 20 * current_bet
    elif sym1 == sym2 or sym1 == sym3 or sym2 == sym3:
        return 2 * current_bet
    else:
        return 0

def print_stats(total_bet, total_won, num_plays):
    print()

    gross = total_won - total_bet

    if gross >= 0:
        printf("After {} play(s) you turned a profit of ${:,.2f}, betting ${:,.2f} and winning back ${:,.2f}.", \
            num_plays, gross, total_bet, total_won)
    else:
        printf("After {} play(s) you lost ${:,.2f}, betting ${:,.2f} and winning back ${:,.2f}.", \
            num_plays, -gross, total_bet, total_won)

    if total_bet > 0:
        printf("Payout %: {:.1f}", 100 * (total_won / total_bet))

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
            printf("Play #{}: ", count, end="")
            won = pull_lever(bet)

            printf("You won ${:,.2f}", won)

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
        total_won += pull_lever(bet)
        total_bet += bet

    print_stats(total_bet, total_won, count)

main()
