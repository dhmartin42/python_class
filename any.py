# any() returns true if any of the items are true or truthy
# any('asdf', '')) == True
# any((0,'')) == False

def conatains_digit3(input_str):
    for char in input_str:
        if char.isdigit():
            return True
    return False

def conatains_digit2(input_str):
    valid = [
        char.isdigit()
        for char in input_str
    ]
    return any(valid)

def conatains_digit(input_str):
    return any(
        char.isdigit()
        for char in input_str
    )
    
def main():
    assert conatains_digit('This sentence does not contain any digits') == False
    assert conatains_digit('But th15 0ne d0e5') == True
    assert conatains_digit('123-456-7890') == True
    print('Passed all tests')

if __name__ == "__main__":
    main()