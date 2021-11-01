# William Hearn
# Python Programming


def split(text):
    text = text.split()
    for word in text:
        print(word)


def split2(text):
    print(text.replace(" ", "\n"))


if __name__ == '__main__':
    sentence = input("Enter a sentence: ")
    if "\'" not in sentence:
        print("Must have an apostraphe is sentence.")
        exit(0)
    else:
        split(sentence)
        split2(sentence)


