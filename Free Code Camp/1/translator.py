
def translate(phrase):
    
    translation = ""
    for letter in phrase:
        ascii_value = ord(letter) + 1
        translation = translation + chr(ascii_value)
    return translation    

print(translate(input('Type a message: ')))

def decode(phrase):
    
    translation = ""
    for letter in phrase:
        ascii_value = ord(letter) - 1
        translation = translation + chr(ascii_value)
    return translation


    