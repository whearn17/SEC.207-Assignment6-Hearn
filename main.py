# William Hearn
# Python Programming


def split(text):
    text = text.split()
    for word in text:
        print(word)


def split2(text):
    print(text.replace(" ", "\n"))


if __name__ == '__main__':
    split(input("Enter a word "))
    split2(input("Enter a word "))


