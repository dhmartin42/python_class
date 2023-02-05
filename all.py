# all() returns true if all values are truthy, which means if they are non-rmpty or non-zero


def valid_rgb2(rgb): # using a list comprehension
    '''recieves (r,g,b) tuple, 
       checks if each rgb int is within (0,255)
       returns true or false '''
    valid = [
        0 <= val <= 255
        for val in rgb
    ]
    return all(valid)

def valid_rgb(rgb): #using a generator
    '''recieves (r,g,b) tuple, 
       checks if each rgb int is within (0,255)
       returns true or false '''
    return all(
        0 <= val <= 255
        for val in rgb
    )
    

def main():
    assert valid_rgb((25,5,225)) == True
    assert valid_rgb((255,255,255)) == True
    assert valid_rgb((290, 100,200)) == False
    assert valid_rgb((250,300,200)) == False
    assert valid_rgb((250,100,400)) == False
    print("All tests valid")

if __name__ == "__main__":
    main()
