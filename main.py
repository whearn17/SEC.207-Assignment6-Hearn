# William Hearn
# Python Programming


def secret(text):
    coded_text = ""
    for character in text:
        coded_text += chr(ord(character) + 5)
    return coded_text


def multiply(text):
    return text * 5


if __name__ == '__main__':
    print(secret(input("Enter a message")))
    print(multiply(input("Enter a message")))


