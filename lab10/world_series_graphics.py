import draw_functions2
from draw_functions2 import *
import math
import random

init_graphics("World series bar graph")

### Don't need to change the draw_bar_graph function; just call it
# draw_bar_graph: creates a bar graph for received data
#    input parameter: a list of tuples where each tuple has the form
#                     (category, value)
#    return values: none
#    output: displays a bar graph corresponding to the data in a window
def draw_bar_graph(data, sort = 'alpha'):
    ## SOME CONSTANTS
    NUM_WIDTH = 20
    TEAM_NAME_WIDTH = 150
    minx, miny = TEAM_NAME_WIDTH, 10
    canvas_x, canvas_y = WINDOW_WIDTH - minx - NUM_WIDTH, WINDOW_HEIGHT - miny

    ## SORT THE DATA
    if sort == 'alpha':
        # sort the data according to team name
        data.sort(key = lambda p: p[0], reverse = True)
    elif sort == 'wins':
        # to sort according to number of wins, do this instead:
        data.sort(key = lambda p: p[1])
    
    ## GET MAX FOR SCALING
    # calculates the max by looking only at the second element in each tuple
    max_data = max(data, key = lambda x : x[1])[1]
    len_per_data = canvas_x / max_data
    # calculate bar width
    space_between_bars = 5
    bar_width = canvas_y // len(data) - space_between_bars

    ## DRAW DATA
    y = miny
    for point in data:
        set_color(BLACK)
        draw_text(10, y + bar_width / 2, point[0].rstrip("\n"))
        set_color(BLUE)
        draw_text(minx + point[1]*len_per_data + 5, 
                  y + bar_width / 2, str(point[1]))
        set_color(RED)
        draw_filled_rectangle(minx, y + bar_width, 
                              point[1]*len_per_data, bar_width)
        y += bar_width + space_between_bars


#############################################################################

DATA_FILE = 'WorldSeriesWinners.txt'
START_YEAR = 1903

def copy_unique(data):
    used = set()
    return sorted([v for v in data if v not in used and not used.add(v)])

def read_winning_teams():
    file = open(DATA_FILE, 'r')
    result = [ln.rstrip('\n') for ln in file.readlines()]
    file.close()
    return result

def get_wins(data, team):
    return [START_YEAR+i for i in range(len(data)) if data[i] == team]

def get_data(data, teams):
    return [ (team, len(get_wins(data, team))) for team in teams ]

team_wins = read_winning_teams()
team_list = copy_unique(team_wins)
draw_bar_graph(get_data(team_wins, team_list), sort='wins')

#############################################################################
# Don't modify below this line
main_loop()
