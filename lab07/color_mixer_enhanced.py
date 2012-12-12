# COSC 1336, Lab 7, Problem 1 (enhanced)
# Robert Morales

from itertools import combinations

def main():
    colors = ('blue', 'red', 'yellow')
    mixes = {
        ('blue', 'red'): 'purple',
        ('blue', 'yellow'): 'green',
        ('red', 'yellow'): 'orange',
    }

    for comb in combinations(colors, 2):
        c1,c2 = comb
        print("Mixing {} and {} results in {}.".format(c1, c2, mixes[comb]))

main()
