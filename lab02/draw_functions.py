import sys, pygame
from pygame import draw
import random
from random import random
import math

pygame.init()
size = WINDOW_WIDTH, WINDOW_HEIGHT = 640, 480
color = 0, 0, 0

screen = pygame.display.set_mode(size)
screen.fill(color)

WHITE = 255, 255, 255
GREY = 102, 102, 102
BLACK = 0, 0, 0
BROWN = 90, 40, 25
RED = 255, 0, 0
ORANGE = 255, 127, 0
YELLOW = 255, 255, 0
GREEN = 0, 255, 0
FOREST_GREEN = 0, 63, 0
CYAN = 0, 255, 255
BLUE = 0, 0, 255
MIDNIGHT_BLUE = 0, 0, 63
PURPLE = 127, 0, 200
MAGENTA = 255, 0, 255

def set_color(color_name):
    global color
    color = color_name

def set_color_rgb(red, green, blue):
    global color
    color = red, green, blue

def set_background_color(color_name):
    screen.fill(color_name)

def set_background_color_rgb(red, green, blue):
    screen.fill((red, green, blue))

def draw_line(x1, y1, x2, y2, thickness = 1):
    if y1 == y2:
        thickness = 2
    draw.line(screen, color, 
              (int(x1), int(WINDOW_HEIGHT-y1)), 
              (int(x2), int(WINDOW_HEIGHT-y2)), int(thickness))

def draw_rectangle(top_left_x, top_left_y, width, height, thickness = 1):
    draw.rect(screen, color, pygame.Rect(int(top_left_x), 
                                         int(WINDOW_HEIGHT-top_left_y), 
                                         int(width), int(height)), 
              int(thickness))

def draw_triangle(x1, y1, x2, y2, x3, y3, thickness = 1):
    draw.polygon(screen, color, [(int(x1), int(WINDOW_HEIGHT-y1)), 
                                 (int(x2), int(WINDOW_HEIGHT-y2)), 
                                 (int(x3), int(WINDOW_HEIGHT-y3))], 
                 int(thickness))

def draw_circle(x, y, radius, thickness = 1):
    draw.circle(screen, color, [int(x), int(WINDOW_HEIGHT-y)], 
                int(radius), int(thickness))

def draw_ellipse(top_left_x, top_left_y, width, height, thickness = 1):
    draw.ellipse(screen, color, pygame.Rect(int(top_left_x), 
                                            int(WINDOW_HEIGHT-top_left_y), 
                                            int(width), int(height)), thickness)

def draw_partial_ellipse(top_left_x, top_left_y, width, height, 
                         start_degrees, end_degrees, thickness = 1):
    if thickness == 0:
        thickness = 1
    draw.arc(screen, color, pygame.Rect(int(top_left_x), 
                                        int(WINDOW_HEIGHT-top_left_y), 
                                        int(width), int(height)),
             start_degrees * math.pi / 180, end_degrees * math.pi / 180,
             int(thickness))

def draw_filled_rectangle(top_left_x, top_left_y, width, height):
    draw_rectangle(top_left_x, top_left_y, width, height, 0)

def draw_filled_triangle(x1, y1, x2, y2, x3, y3):
    draw_triangle(x1, y1, x2, y2, x3, y3, 0)

def draw_filled_circle(x, y, radius):
    draw_circle(x, y, radius, 0)

def draw_filled_ellipse(top_left_x, top_left_y, width, height):
    draw_ellipse(top_left_x, top_left_y, width, height, 0)
