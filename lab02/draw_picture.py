########################################################################
# COSC 1336 Lab 2 Problem 3
# Robert Morales
########################################################################

# NEED TO KEEP THIS IMPORT STATEMENT
import draw_functions
from draw_functions import *

############################################################################
# Draw an iPhone! (And hope Apple doesn't sue me)

# Arbitrary stuff
PHONE_WIDTH = 160
PHONE_HEIGHT = PHONE_WIDTH * 1.5
set_background_color(WHITE)

# Draw the outside of the phone
PHONE_CASE_X = (WINDOW_WIDTH - PHONE_WIDTH) / 2
PHONE_CASE_Y = WINDOW_HEIGHT - PHONE_HEIGHT / 2
set_color(BLACK)
draw_rectangle(PHONE_CASE_X, PHONE_CASE_Y, PHONE_WIDTH, PHONE_HEIGHT, 2)

# Draw the phone's screen
PHONE_SCREEN_X = PHONE_CASE_X + 5
PHONE_SCREEN_Y = PHONE_CASE_Y - 30
PHONE_SCREEN_WIDTH = PHONE_WIDTH - 10
PHONE_SCREEN_HEIGHT = PHONE_HEIGHT - 70
set_color(BLACK)
draw_filled_rectangle(PHONE_SCREEN_X, PHONE_SCREEN_Y,
               PHONE_SCREEN_WIDTH, PHONE_SCREEN_HEIGHT)

# Draw the speaker above the screen
PHONE_SPEAKER_WIDTH = 80
PHONE_SPEAKER_HEIGHT = 10
PHONE_SPEAKER_X = (PHONE_CASE_X + (PHONE_WIDTH / 2)) - (PHONE_SPEAKER_WIDTH / 2) # this is why I don't do graphics programming...
PHONE_SPEAKER_Y = PHONE_CASE_Y - 15
set_color(BLACK)
draw_filled_ellipse(PHONE_SPEAKER_X, PHONE_SPEAKER_Y,
                    PHONE_SPEAKER_WIDTH, PHONE_SPEAKER_HEIGHT)

# Draw the "Home" button
PHONE_BUTTON_RADIUS = 12
PHONE_BUTTON_X = PHONE_CASE_X + (PHONE_WIDTH / 2)
PHONE_BUTTON_Y = PHONE_SCREEN_Y - PHONE_SCREEN_HEIGHT - (PHONE_BUTTON_RADIUS * 1.5)
set_color(BLACK)
draw_filled_circle(PHONE_BUTTON_X, PHONE_BUTTON_Y, PHONE_BUTTON_RADIUS)

############################################################################
# Don't change anything below this line!
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.display.quit()
