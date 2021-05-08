########################################################################
# COSC 1336, Exam 3 Lab
# 13-DEC-2012
# Robert Morales
########################################################################

########################################################################
# FUNCTION: read_data
# PURPOSE: Reads song data from a text file.
# INPUT: filename (str) - Name of file to be read.
# OUTPUT: list - List of tuples containing song information.
########################################################################
def read_data(filename):
    file = open(filename, 'r')
    lines = [ln.rstrip('\n') for ln in file.readlines()]
    file.close()

##    data = []
##    for ix in range(0, len(lines), 3)
##        title = lines[ix]
##        artist = lines[ix+1]
##        duration = int(lines[ix+2])
##        data += [(title, artist, duration)]

    return [(lines[ix], lines[ix+1], int(lines[ix+2])) \
             for ix in range(0, len(lines), 3)]

########################################################################
# FUNCTION: get_max_within_limit
# PURPOSE: Selects a song that best fits the given time limit.
# INPUTS: limit (int) - The time limit, in seconds.
#         data (list) - List of songs
# OUTPUT: The longest song that fits within the time limit, or the
#         tuple `("", "", 0)` if there is no suitable song.
########################################################################
def get_max_within_limit(limit, data):
    result = ("", "", 0)

    for datum in data:
        if datum[2] <= limit and datum[2] > result[2]:
            result = datum

    return result

########################################################################
# FUNCTION: main
# PURPOSE: Program entry point. Reads songs from "songs.txt", queries
#          the user for a time limit, and selects a song that fits
#          in that time limit.
# INPUT: data - Read in from text file
#        limit - Time limit read in from user
# OUTPUT: Best suggestion for a song, or an error indicating none is
#         available.
########################################################################
def main():
    data = read_data('songs.txt')
##    for title, artist, duration in data:
##        print("{:<22} {:<22} {:<22}".format(title, artist, duration))
    limit = int(input("Enter time limit in seconds (-1 to quit): "))
    while limit >= 0:
        title, artist, duration = get_max_within_limit(limit, data)

        if title == '' and artist == '' and duration == 0:
            print("There is no available song given the time limit.")
        else:
            print("Best suggestion: {} - {} ({})".format(title, artist, duration))

        print()
        limit = int(input("Enter another time limit in seconds (-1 to quit): "))

########################################################################

main()
