# COSC 1336, Lab 6, Problem 3
# Robert Morales

def print_triangle():
    height = 7

    print("#")
    print("##")

    for x in range(3, height):
        print('#', end="")
        for y in range(x-2):
                print(' ', end="", file=stderr)
        print('#')

    print('#'*(x+1))

def print_triangle_with_height(height):
    # Observation:
    # When running in IDLE, this can take a ridiculously long time
    # to print when a large height value is given...

    if 3 <= height <= 200:
        print("#")
        print("##")

        if height > 3:
            for x in range(3, height):
                print('#', end="")
                for y in range(x-2):
                        print(' ', end="")
                print('#')

            print('#'*(x+1))
        else:
            print('###')
