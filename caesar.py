from helpers import alphabet_position, rotate_character

def encrypt(text,rot):
    new_string = ''
    for char in text:
        if char == ' ':
            new_string = new_string + ' '
        else:
            new_string = new_string + rotate_character(char,rot)
    return new_string

def main():
    message = input('Type a message:')
    rotate = int(input('Rotate by:'))
    print(encrypt(message,rotate))

if __name__ == "__main__":
    main()