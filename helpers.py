import string
def alphabet_position(letter):
    if letter in string.ascii_lowercase:
        pos_num = string.ascii_lowercase.find(letter)
    else:
        pos_num = string.ascii_uppercase.find(letter)
    return pos_num

def rotate_character(char,rot):
    x = alphabet_position(char) + rot
    new_value = ''
    if char in string.ascii_lowercase:
        if x <= 25:
            new_value = string.ascii_lowercase[x]
        else:
            x = x - 26
            new_value = string.ascii_lowercase[x]
    elif char in string.ascii_uppercase:
        if x <= 25:
            new_value = string.ascii_uppercase[x]
        else:
            x = x - 26
            new_value = string.ascii_uppercase[x]
    else:
        new_value = char
    return(new_value)
    