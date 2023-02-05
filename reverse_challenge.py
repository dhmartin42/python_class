import re

def remove_punctuation(words):
    return re.sub('\W+', '', words)

def is_palindrome(words):
    return  remove_punctuation(words.lower()) == ''.join(reversed(remove_punctuation(words.lower())))

def main():
    print(is_palindrome('sagas'))
    print(is_palindrome('This should not work'))
    print(is_palindrome("Madam I'm Adam!"))

if __name__ == "__main__":
    main()
