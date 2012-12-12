# COSC 1336 (15850), Fall 2012
# Lab 9, Problem 2 (enhanced)
# Written by Robert Morales

def copy_unique(data):
    used = set()
    return [ v for v in data \
             if v not in used and not used.add(v) ]

class Application:
    def __init__(self):
        self.start = 1903
        self.data = []
        self.teams = []

    def read_file(self):
        with open('WorldSeriesWinners.txt', 'r') as file:
            self.data = [ln.rstrip('\n') for ln in file]

        if len(self.data) == 0:
            raise Exception("No data in WorldSeriesWinners.txt!")

        self.teams = sorted(copy_unique(self.data))

    def get_wins(self, team):
        return [self.start+i for i in range(len(self.data)) \
                if self.data[i] == team]

    def print_menu(self):
        print("Choose a team by specifying its choice number.")
        n = 0
        for entry in self.teams:
            print("{}. {}".format(n, entry))
            n += 1
        print("-1 to Quit")

    def get_user_choice(self):
        self.print_menu()

        try:
            try:
                index = int(input("Your choice? "))
            except ValueError:
                index = None

            while index not in range(-1, len(self.teams)):
                print("Invalid choice. Please try again.")
                index = int(input("Your choice? "))

            return index
        except KeyboardInterrupt:
            return -1

    def run(self):
        self.read_file()

        for index in iter(self.get_user_choice, -1):
            name = self.teams[index]
            years = self.get_wins(name)
            print("The", name, "won in the following years:", years)
            print()
            input("Press <ENTER> to continue.")

app = Application()
app.run()
