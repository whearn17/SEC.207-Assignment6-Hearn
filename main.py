# William Hearn
# Python Programming


def pig_latin(text):
    text = text.split()
    pig = ""
    end = False
    tmp = ""
    for word in text:
        tmp = ""
        if word[0] in "aeiouyAEIOUY":
            pig += word + "yay "
        elif word[0] not in "aeiouyAEIOUY":
            for character in word:
                if character in "aeiouyAEIOUY" and not end:
                    end = True
                elif character not in "aeiouyAEIOUY" and not end:
                    tmp += character
            end = False
            pig += word[len(tmp):] + word[0:len(tmp)] + "ay "
    return pig


if __name__ == '__main__':
    print(pig_latin(input("Enter a message")))

