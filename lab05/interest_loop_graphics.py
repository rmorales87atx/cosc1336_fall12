import draw_functions2 
from draw_functions2 import * 
import math

init_graphics("Interest plot")
#############################################################################
# Edit code between here and similar line below

# TODO: Modify function to display plot instead of single data point
def balance_display_loop(start_balance, int_rate, num_months):
    balance = start_balance
    for n in range(1, num_months+1):
        balance *= (1 + int_rate)

    # draw a single red data point
    set_color(RED)
    draw_filled_circle(100, 100, 3)

# You can use whatever colors you want
set_background_color(BLACK)
balance_display_loop(100, 0.02, 10*12)

#############################################################################

# Don't remove this line
main_loop()
