# COSC 1336, Lab 12, Problem 2
# Robert Morales

# KNOWN BUGS:
# - Any punctuation near words counts the word as incorrectly spelled, such as
#   the sentence: "The cat meowed." ("meowed." is "incorrectly spelled")

class SpellChecker:
    def __init__(self, filename):
        infile = open(filename)
        self.__words = [ln.rstrip('\n').lower() for ln in infile.readlines()]
        infile.close()

    def spellcheck_word(self, word):
        return word.lower() in self.__words

    def spellcheck_sentence(self, text):
        okay = True
        for part in text.split():
            if not self.spellcheck_word(part):
                okay = False
                print("The word '{}' does not appear to be spelled correctly.".format(part))

        if okay:
            print("All words appear to be spelled correctly.")

def main():
    check = SpellChecker("dictionary.txt")
    text = input("Enter a sentence (or blank to quit): ")
    while text != "":
        check.spellcheck_sentence(text)
        print()
        text = input("Enter a sentence (or blank to quit): ")

main()
