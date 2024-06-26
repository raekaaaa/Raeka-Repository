def shift_letter(letter, shift):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if letter == " ":
        return ' '

    else:
        position = (alphabet.index(letter)+shift)%26
        new_letter = alphabet[position]
        return new_letter


def caesar_cipher(message,shift):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    for character in message:
        if character == " ":
            result += character 
        else:
            position = alphabet.index(character)
            new_position = (position+shift)%26
            result += alphabet[new_position]
    return result

    
def shift_by_letter(letter, letter_shift):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if letter == " ":
        return ' '

    else:
        position = (alphabet.index(letter)+alphabet.index(letter_shift))%26
        new_letter = alphabet[position]
        return new_letter


def vigenere_cipher(message,key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    key_length = len(key)
    key_index = 0
    
    for character in message:
        if character == " ":
            key_index += 1
            result += " " 
        else:
            key_position = alphabet.index(key[key_index % key_length])
            message_position = alphabet.index(character)
            new_position = (message_position + key_position)%26
            result += alphabet[new_position]
            key_index += 1
    return result



def scytale_cipher(message, shift):
    result = ""
    message_length = len(message)
    if message_length % shift != 0:
        message += (shift-(message_length%shift))* "_"
        
    for i in range(len(message)): 
        character_position = message[(i // shift) + (len(message) // shift) * (i % shift)]
        result += character_position
    return result


def scytale_decipher(message, shift):
    message_length = len(message)
    if shift == 0:
        return message
    result = ""

    for i in range (shift):
        for j in range(message_length//shift):
            result += message[i + (j*shift)]
    return result







