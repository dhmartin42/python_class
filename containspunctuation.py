import string

def contains_punctuation(input_str):
    '''returns true if string contains punctuation, false otherwise'''
    return any(
        char in string.punctuation #needed to have char in added to work
        for char in input_str
    )
    # remember to check if the character is actually in the string.punctuation
    # rather than just saying hey string.punctuation! 

def main():
    
    assert contains_punctuation('this does not contain punctuation') == False
    assert contains_punctuation('This, however, does.') == True
    print('all tests passed')

if __name__ == "__main__":
    main()
