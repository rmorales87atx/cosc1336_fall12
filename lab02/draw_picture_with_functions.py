########################################################################
# COSC 1336 Lab 2 Problem 4
# Robert Morales
#
# KNOWN BUGS:
#   1) Due to the use of random.randint(), it is possible for this
#      to occasionally draw pictures off-screen.
########################################################################

# NEED TO KEEP THIS IMPORT STATEMENT
import draw_functions
from draw_functions import *

############################################################################
# Draw an iPhone! (And hope Apple doesn't sue me)
# Now with Functions™

import random

# Initialize globals ("quasi-constants")

phone_width = 0
phone_height = 0
phone_color = BLACK

# FUNCTION: phone_init
# PURPOSE: Initializes variables for a drawing operation.
#          This function should not be used directly; see 'phone_draw'.
def phone_init(width, color):
    global phone_width, phone_height, phone_color
    phone_width = width
    phone_height = int(width * 1.5)
    phone_color = color

# FUNCTION: phone_draw_case
# PURPOSE: Draws a rectangle resembling the outer case of the phone.
#          This function should not be used directly; see 'phone_draw'.
def phone_draw_case(base_x, base_y):
    set_color(phone_color)
    draw_rectangle(base_x, base_y, phone_width, phone_height, 2)

# FUNCTION: phone_draw_screen
# PURPOSE: Draws a filled rectangle resembling the phone's screen in a
#          blank state.
#          This function should not be used directly; see 'phone_draw'.
def phone_draw_screen(base_x, base_y):
    screen_x = base_x + 5
    screen_y = base_y - 30
    screen_width = phone_width - 10
    screen_height = phone_height - 70
    set_color(phone_color)
    draw_filled_rectangle(screen_x, screen_y, screen_width, screen_height)

# FUNCTION: phone_draw_speaker
# PURPOSE: Draws a filled ellipse resembling the phone's speaker.
#          This function should not be used directly; see 'phone_draw'.
def phone_draw_speaker(base_x, base_y):
    speaker_width = phone_width // 2
    speaker_height = 10
    speaker_x = (base_x + (phone_width // 2)) - (speaker_width // 2) # this is why I don't do graphics programming...
    speaker_y = base_y - 15
    set_color(phone_color)
    draw_filled_ellipse(speaker_x, speaker_y, speaker_width, speaker_height)

# FUNCTION: phone_draw_button
# PURPOSE: Draws a filled circle resembling the phone's "Home" button.
#          This function should not be used directly; see 'phone_draw'.
def phone_draw_button(base_x, base_y):
    button_radius = 12
    button_x = base_x + (phone_width // 2)
    button_y = (base_y - 30) - (phone_height - 70) - int(button_radius * 1.5)
    set_color(phone_color)
    draw_filled_circle(button_x, button_y, button_radius)

# FUNCTION: phone_draw
# PURPOSE: Uses the previously defined phone_draw_* functions to draw
#          a phone with the specified attributes.
def phone_draw(color, width, x, y):
    phone_init(width, color)
    phone_draw_case(x, y)
    phone_draw_screen(x, y)
    phone_draw_speaker(x, y)
    phone_draw_button(x, y)

# FUNCTION: draw_phone_random
# PURPOSE: Uses the previously defined phone_draw_* functions to draw
#          a phone with the specified color attribute, but uses an RNG
#          to randomly determine where the phone is to be drawn (X,Y).
def phone_draw_random(color):
    random_width = random.randint(80, 200)
    random_x = random.randint(phone_width, WINDOW_WIDTH)
    random_y = random.randint(phone_height, WINDOW_HEIGHT)
##    print("width", random_width, "x", random_x, "y", random_y)
    phone_draw(color, random_width, random_x, random_y)

# FUNCTION: main
# PURPOSE: Program entry point. Initializes the background color and draws
#          three random phones in three different colors.
def main():
    set_background_color(WHITE)
    phone_draw_random(BLACK)
    phone_draw_random(RED)
    phone_draw_random(GREEN)

############################################################################
main()
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.display.quit()
