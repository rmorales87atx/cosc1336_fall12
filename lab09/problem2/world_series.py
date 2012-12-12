# COSC 1336 (15850), Fall 2012
# Lab 9, Problem 2
# Written by Robert Morales

DATA_FILE = 'WorldSeriesWinners.txt'
START_YEAR = 1903

def read_winning_teams():
    file = open(DATA_FILE, 'r')
    result = [ln.rstrip('\n') for ln in file.readlines()]
    file.close()
    return result

def get_wins(data, team):
    return [START_YEAR+i for i in range(len(data)) if data[i] == team]

def copy_no_duplicates(data):
    result = []
    for entry in data:
        if entry not in result:
            result.append(entry)
    result.sort()
    return result

def print_menu(teams):
    print("Choose a team by specifying its choice number.")
    n = 0
    for entry in teams:
        print(n, '. ', entry, sep="")
        n += 1
    print("-1 to Quit")

def get_user_choice(teams):
    print_menu(teams)
    index = int(input("Your choice? "))
    while index not in range(-1, len(teams)):
        print("Invalid choice. Please try again.")
        index = int(input("Your choice? "))
    return index

def main():
    data = read_winning_teams()

    if len(data) == 0:
        print("Bork bork bork!!!")
        return

    teams = copy_no_duplicates(data)

    index = get_user_choice(teams)

    while index != -1:
        name = teams[index]
        years = get_wins(data, name)

        print("The", name, "won in the following years:", years)

        input("\nPress <ENTER> to continue.")
        index = get_user_choice(teams)

main()
