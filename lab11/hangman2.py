# COSC 1336, Lab 11
# Robert Morales

from random import shuffle
from random import randrange

MAX_FAIL = 8
EasyMode = False

# draw_stick_figure
#    input: the number of failed guesses
#    output: no return value; draws stick figure according to the number of
#            failed guesses
def draw_stick_figure(num_fails):
    # this array specifies the characters in the drawing
    body = [[' ', '_', '_', '_', ' ', ' '],
            ['|', '/', ' ', ' ', '|', ' '],
            ['|', ' ', ' ', ' ', 'O', ' '],
            ['|', ' ', ' ', '/', '|', '\\'],
            ['|', ' ', ' ', ' ', '|', ' '],
            ['|', ' ', ' ', '/', ' ', '\\'],
            ['^', ' ', ' ', ' ', ' ', ' ']]

    # this parallel array specifies the number of failed guesses
    # that result in the character being drawn
    body_fails = [[0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1, 0],
                  [0, 0, 0, 0, 2, 0],
                  [0, 0, 0, 5, 3, 6],
                  [0, 0, 0, 0, 4, 0],
                  [0, 0, 0, 7, 0, 8],
                  [0, 0, 0, 0, 0, 0]]

    # for each character in the body, draw it if the number of
    # failed guesses is large enough
    for r in range(len(body)):
        for c in range(len(body[r])):
            if num_fails >= body_fails[r][c]:
                print(body[r][c],end="")
            else:
                print(" ",end="")
        print()

def replace_all(word, guess, letter):
    result = list(guess)
    for i in range(len(word)):
        if word[i] == letter:
            result[i] = letter
    return (letter in word, str.join('', result))

def get_letter(guessed):
    letter = input("Enter a letter: ").upper()

    while len(letter) > 1:
        print("Invalid input. Letters are one character.")
        letter = input("Enter a letter: ").upper()

    while letter in guessed:
        print("You've already guessed '{}'.".format(letter))
        letter = input("Enter a letter: ").upper()

    guessed.append(letter)
    return letter

def play(word):
    fail = 0
    guess = '-' * len(word)
    guessed = []

    if EasyMode:
        # give user one letter
        i = randrange(0, len(word)-1)
        letter = word[i]
        guessed.append(letter)
        _, guess = replace_all(word, guess, letter)

    while guess != word:
        print("Guess this word: ", guess, ' (', len(word), ')', sep="")

        letter = get_letter(guessed)
        found, guess = replace_all(word, guess, letter)

        if found:
            num = word.count(letter)
            if num == 1:
                print("Yes, there is one '{}'.".format(letter))
            else:
                print("Yes, there are {} '{}'s.".format(num, letter))
        else:
            print("Sorry, there is no '{}'.".format(letter))
            fail += 1
            draw_stick_figure(fail)

        if word == guess:
            print()
            print("Great job! You got it:", word)
        elif fail > MAX_FAIL:
            print()
            print("Sorry, you're out of guesses now.")
            print("The word is:", word)
            break

def ask_user(question):
    response = input(question + " ").lower()
    while response not in ('y', 'n', 'yes', 'no'):
        print("I'm sorry, I didn't quite understand that...")
        print()
        response = input(question + " ").lower()
    return response in ('y', 'yes')

def load_words():
    f = open("words.txt", 'r')
    result = [ln.rstrip('\n').upper() for ln in f.readlines()]
    f.close()
    shuffle(result)
    return result

def main():
    global EasyMode
    if ask_user("Would you like to play Hangman?"):
        EasyMode = ask_user("Would you like to play in Easy Mode?")
        words = load_words()
        i = iter(words)
        while True:
            play(next(i))
            if not ask_user("Would you like to play again?"):
                break

main()
