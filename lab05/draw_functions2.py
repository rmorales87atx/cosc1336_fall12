import time, os, sys

try:
    import tkinter as tk
except:
    import Tkinter as tk

##########################################################################
# Module Exceptions

class GraphicsError(Exception):
    """Generic error class for graphics module exceptions."""
    pass

OBJ_ALREADY_DRAWN = "Object currently drawn"
UNSUPPORTED_METHOD = "Object doesn't support operation"
BAD_OPTION = "Illegal option value"
DEAD_THREAD = "Graphics thread quit unexpectedly"

_root = tk.Tk()
_root.withdraw()

class GraphWin(tk.Canvas):

    """A GraphWin is a toplevel window for displaying graphics."""

    def __init__(self, title="Graphics Window",
                 width=200, height=200, autoflush=True):
        master = tk.Toplevel(_root)
        master.protocol("WM_DELETE_WINDOW", self.close)
        tk.Canvas.__init__(self, master, width=width, height=height)
        self.master.title(title)
        self.pack()
        master.resizable(0,0)
        self.foreground = "black"
        self.items = []
        self.mouseX = None
        self.mouseY = None
        self.bind("<Button-1>", self._onClick)
        self.height = height
        self.width = width
        self.autoflush = autoflush
        self._mouseCallback = None
        self.trans = None
        self.closed = False
        master.lift()
        if autoflush: _root.update()
     
    def __checkOpen(self):
        if self.closed:
            raise GraphicsError("window is closed")

    def setBackground(self, color):
        """Set background color of the window"""
        self.__checkOpen()
        self.config(bg=color)
        self.__autoflush()
        
    def setCoords(self, x1, y1, x2, y2):
        """Set coordinates of window to run from (x1,y1) in the
        lower-left corner to (x2,y2) in the upper-right corner."""
        self.trans = Transform(self.width, self.height, x1, y1, x2, y2)

    def close(self):
        """Close the window"""

        if self.closed: return
        self.closed = True
        self.master.destroy()
        self.__autoflush()


    def isClosed(self):
        return self.closed


    def isOpen(self):
        return not self.closed


    def __autoflush(self):
        if self.autoflush:
            _root.update()

    
    def plot(self, x, y, color="black"):
        """Set pixel (x,y) to the given color"""
        self.__checkOpen()
        xs,ys = self.toScreen(x,y)
        self.create_line(xs,ys,xs+1,ys, fill=color)
        self.__autoflush()
        
    def plotPixel(self, x, y, color="black"):
        """Set pixel raw (independent of window coordinates) pixel
        (x,y) to color"""
        self.__checkOpen()
        self.create_line(x,y,x+1,y, fill=color)
        self.__autoflush()
      
    def flush(self):
        """Update drawing to the window"""
        self.__checkOpen()
        self.update_idletasks()
        
    def getMouse(self):
        """Wait for mouse click and return Point object representing
        the click"""
        self.update()      # flush any prior clicks
        self.mouseX = None
        self.mouseY = None
        while self.mouseX == None or self.mouseY == None:
            self.update()
            if self.isClosed(): raise GraphicsError("getMouse in closed window")
            time.sleep(.1) # give up thread
        x,y = self.toWorld(self.mouseX, self.mouseY)
        self.mouseX = None
        self.mouseY = None
        return x,y

    def checkMouse(self):
        """Return last mouse click or None if mouse has
        not been clicked since last call"""
        if self.isClosed():
            raise GraphicsError("checkMouse in closed window")
        self.update()
        if self.mouseX != None and self.mouseY != None:
            x,y = self.toWorld(self.mouseX, self.mouseY)
            self.mouseX = None
            self.mouseY = None
            return x,y
        else:
            return None
            
    def getHeight(self):
        """Return the height of the window"""
        return self.height
        
    def getWidth(self):
        """Return the width of the window"""
        return self.width
    
    def toScreen(self, x, y):
        trans = self.trans
        if trans:
            return self.trans.screen(x,y)
        else:
            return x,y
                      
    def toWorld(self, x, y):
        trans = self.trans
        if trans:
            return self.trans.world(x,y)
        else:
            return x,y
        
    def setMouseHandler(self, func):
        self._mouseCallback = func
        
    def _onClick(self, e):
        self.mouseX = e.x
        self.mouseY = e.y
        if self._mouseCallback:
            self._mouseCallback((e.x, e.y)) 


class Transform:

    """Internal class for 2-D coordinate transformations"""
    
    def __init__(self, w, h, xlow, ylow, xhigh, yhigh):
        # w, h are width and height of window
        # (xlow,ylow) coordinates of lower-left [raw (0,h-1)]
        # (xhigh,yhigh) coordinates of upper-right [raw (w-1,0)]
        xspan = (xhigh-xlow)
        yspan = (yhigh-ylow)
        self.xbase = xlow
        self.ybase = yhigh
        self.xscale = xspan/float(w-1)
        self.yscale = yspan/float(h-1)
        
    def screen(self,x,y):
        # Returns x,y in screen (actually window) coordinates
        xs = (x-self.xbase) / self.xscale
        ys = (self.ybase-y) / self.yscale
        return int(xs+0.5),int(ys+0.5)
        
    def world(self,xs,ys):
        # Returns xs,ys in world coordinates
        x = xs*self.xscale + self.xbase
        y = self.ybase - ys*self.yscale
        return x,y


# Default values for various item configuration options. Only a subset of
#   keys may be present in the configuration dictionary for a given item
DEFAULT_CONFIG = {"fill":"",
      "outline":"black",
      "width":"1",
      "arrow":"none",
      "text":"",
      "justify":"center",
                  "font": ("helvetica", 12, "normal")}

size = WINDOW_WIDTH, WINDOW_HEIGHT = 640, 480


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

pen_color = "#%02x%02x%02x" % BLACK

def set_color(color_name):
    global pen_color
    pen_color = "#%02x%02x%02x" % color_name

def set_color_rgb(red, green, blue):
    global pen_color
    pen_color = "#%02x%02x%02x" % (red, green, blue)

def set_background_color(color_name):
    tk_color = "#%02x%02x%02x" % color_name
    win.setBackground(tk_color)

def set_background_color_rgb(red, green, blue):
    tk_color = "#%02x%02x%02x" % (red, green, blue)
    win.setBackground(tk_color)
    
def draw_line(x1, y1, x2, y2, thickness = 1):
    win.create_line(x1, WINDOW_HEIGHT - y1, 
                    x2, WINDOW_HEIGHT - y2, 
                    fill=pen_color, width = thickness)

def draw_rectangle(top_left_x, top_left_y, width, height, thickness = 1):
    win.create_rectangle(top_left_x, WINDOW_HEIGHT - top_left_y, 
                         top_left_x + width, 
                         WINDOW_HEIGHT - (top_left_y - height),
                         outline = pen_color,
                         width = thickness)

def draw_triangle(x1, y1, x2, y2, x3, y3, thickness = 1):
    win.create_polygon(x1, WINDOW_HEIGHT - y1, 
                       x2, WINDOW_HEIGHT - y2, 
                       x3, WINDOW_HEIGHT - y3, 
                       outline = pen_color,
                       width = thickness)

def draw_circle(x, y, radius, thickness = 1):
    top_left = x - radius, WINDOW_HEIGHT - (y + radius)
    bottom_right = x + radius, WINDOW_HEIGHT - (y - radius)
    win.create_oval(top_left, bottom_right, 
                    outline = pen_color,
                    width = thickness)

def draw_ellipse(top_left_x, top_left_y, width, height, thickness = 1):
    top_left = top_left_x, WINDOW_HEIGHT - top_left_y
    bottom_right = top_left_x + width, WINDOW_HEIGHT - (top_left_y-height)
    win.create_oval(top_left, bottom_right, 
                    outline = pen_color, 
                    width = thickness)

def draw_partial_ellipse(top_left_x, top_left_y, width, height,
                         start_degrees, end_degrees, 
                         thickness = 1, style = "arc"):
    win.create_arc(top_left_x, WINDOW_HEIGHT - top_left_y, 
                   top_left_x + width, WINDOW_HEIGHT - (top_left_y - height),
                   style = style, start = start_degrees, 
                   extent = (end_degrees - start_degrees) % 360, 
                   outline = pen_color, width = thickness)

def draw_filled_rectangle(top_left_x, top_left_y, width, height):
    win.create_rectangle(top_left_x, WINDOW_HEIGHT - top_left_y, 
                         top_left_x + width, 
                         WINDOW_HEIGHT - (top_left_y - height),
                         outline = pen_color, fill = pen_color)

def draw_filled_triangle(x1, y1, x2, y2, x3, y3):
    win.create_polygon(x1, WINDOW_HEIGHT - y1, 
                       x2, WINDOW_HEIGHT - y2, 
                       x3, WINDOW_HEIGHT - y3, 
                       outline = pen_color, fill = pen_color)

def draw_filled_circle(x, y, radius):
    top_left = x - radius, WINDOW_HEIGHT - (y + radius)
    bottom_right = x + radius, WINDOW_HEIGHT - (y - radius)
    win.create_oval(top_left, bottom_right, 
                    outline = pen_color, fill = pen_color)

def draw_filled_ellipse(top_left_x, top_left_y, width, height):
    top_left = top_left_x, WINDOW_HEIGHT - top_left_y
    bottom_right = top_left_x + width, WINDOW_HEIGHT - (top_left_y-height)
    win.create_oval(top_left, bottom_right, 
                    outline = pen_color, fill = pen_color)

def draw_filled_partial_ellipse(top_left_x, top_left_y, width, height,
                                start_degrees, end_degrees, style = "pieslice"):
    win.create_arc(top_left_x, WINDOW_HEIGHT - top_left_y, 
                   top_left_x + width, WINDOW_HEIGHT - (top_left_y - height),
                   style = style, start = start_degrees, 
                   extent = (end_degrees - start_degrees) % 360, 
                   outline = pen_color, fill = pen_color)


def draw_text(left_x, left_y, text, anchor = "w"):
    win.create_text(left_x, WINDOW_HEIGHT - left_y, fill = pen_color, 
                    anchor = "w", text = text)

def init_graphics(name = "Drawing"):
    global win
    win = GraphWin(name, WINDOW_WIDTH, WINDOW_HEIGHT)

def main_loop():
    try:
        win.getMouse()
    except:
        pass
    win.close()
