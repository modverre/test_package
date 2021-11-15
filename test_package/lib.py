def try_me(i):
    #returns string of lower case letters up to the  ith position in the alphabet
    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    if i <= len(ascii_lowercase):
        return ascii_lowercase[:i]
    return "Argument must be number between 1 and 26"
