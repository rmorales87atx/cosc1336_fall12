# COSC 1336, Lab 10, Problem 2
# Robert Morales
# 20-NOV-2012

NUM_COLS = 5
NUM_ROWS = 10

def read_data():
    file = open('data.txt', 'r')
    data = [ [ float(file.readline()) for y in range(NUM_COLS) ] \
             for x in range(NUM_ROWS) ]
    file.close()
    return data

def get_user_values():
    begin = int(input("Enter minimum: "))
    end = int(input("Enter maximum: "))
    return begin, end

def read_column(index, data):
    return [row[index] for row in data]

def main():
    data = read_data()
    begin, end = get_user_values()
    column_ranges = [ len([v for v in read_column(i, data) if begin <= v <= end]) \
                      for i in range(NUM_COLS) ]

    print("Data in range for each column: ", end="")
    for value in column_ranges:
        print(value, end=" ")
    print()

main()
