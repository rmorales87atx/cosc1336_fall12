# COSC 1336, Lab 8, Problem 1
# Robert Morales

def main():
    filename = input("Enter a filename. ")

    fp = open(filename, 'r')
    accum = 0
    count = 0

    line = fp.readline()

    while line != '':
        num = int(line)

        accum += num
        count += 1

        line = fp.readline()

    fp.close()

    print("Read {} numbers. Average {:.6f}.".format(count, accum / count))

main()
