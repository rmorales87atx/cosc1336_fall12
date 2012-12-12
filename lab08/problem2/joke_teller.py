# COSC 1336, Lab 8, Problem 2
# Robert Morales

def tell_joke(file):
    text = file.readline()

    if text == '':
        return False

    num_lines = int(text)
    question = file.readline()
    question = question.rstrip()
    print("Q:", question)

    for x in range(num_lines-1):
        input()
        answer = file.readline()
        print("A:", answer)

    input()
    return True

def main():
    print()
    print("Welcome to the COSC 1336 Joke Teller!")
    print("Press <ENTER> after each line to continue.")
    print()

    file = open("jokes.txt")

    while tell_joke(file):
        pass

    file.close()

main()
