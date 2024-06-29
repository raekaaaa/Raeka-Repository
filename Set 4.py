#!/usr/bin/env python
# coding: utf-8

# In[63]:


def bin_to_dec(binary_string):
    reversed_string = binary_string[::-1]
    normal_number = 0
    
    for i in range(len(binary_string)):
        bit_number = int(reversed_string[i])
        normal_number += bit_number*2**i
    return normal_number
        

bin_to_dec ("10000000001")


# In[3]:


def dec_to_bin(number):
    if number == 0:
        return "0"
    binary_number = ""
    while number > 0:
        binary_number = str(number % 2) + binary_number
        number = number // 2
    return binary_number

dec_to_bin(1025)


# In[119]:


encoder_dict = {
        " ":"0",
        "A":"2",
        "B":"22",
        "C":"222",
        "D":"3",
        "E":"33",
        "F":"333",
        "G":"4",
        "H":"44",
        "I":"444",
        "J":"5",
        "K":"55",
        "L":"555",
        "M":"6",
        "N":"66",
        "O":"666",
        "P":"7",
        "Q":"77",
        "R":"777",
        "S":"7777",
        "T":"8",
        "U":"88",
        "V":"888",
        "W":"9",
        "X":"99",
        "Y":"999",
        "Z":"9999"
    }
   
def telephone_cipher(message):
    result = ""
    before_number = ""
    for letter in message:
        character_number = str(encoder_dict[letter])
    
        if result and character_number[0] == before_number:
            result += "_" + character_number
           
        else:
            result += character_number
         
        before_number = character_number[0] 
          
    return result

telephone_cipher("I LOVE YOU BABY")


# In[116]:


decipher_dict = {
        "0":" ",
        '2': 'A',
        '22': 'B',
        '222': 'C',
        '3': 'D',
        '33': 'E',
        '333': 'F',
        '4': 'G',
        '44': 'H',
        '444': 'I',
        '5': 'J',
        '55': 'K',
        '555': 'L',
        '6': 'M',
        '66': 'N',
        '666': 'O',
        '7': 'P',
        '77': 'Q',
        '777': 'R',
        '7777': 'S',
        '8': 'T',
        '88': 'U',
        '888': 'V',
        '9': 'W',
        '99': 'X',
        '999': 'Y',
        '9999': 'Z'
    }
def telephone_decipher(telephone_string):
    result = ""
    parts = telephone_string.split("_")
    for part in parts:
        i = 0
        while i < len(part):
            for length in range(4, 0, -1):  # Check from longest to shortest
                if part[i:i+length] in decoder_dict:
                    result += decoder_dict[part[i:i+length]]
                    i += length
                    break
    return result 


telephone_decipher("2_22_222")


# In[120]:


def telephone_decipher(telephone_string):
    decoder_dict = {
        "0":" ",
        '2': 'A',
        '22': 'B',
        '222': 'C',
        '3': 'D',
        '33': 'E',
        '333': 'F',
        '4': 'G',
        '44': 'H',
        '444': 'I',
        '5': 'J',
        '55': 'K',
        '555': 'L',
        '6': 'M',
        '66': 'N',
        '666': 'O',
        '7': 'P',
        '77': 'Q',
        '777': 'R',
        '7777': 'S',
        '8': 'T',
        '88': 'U',
        '888': 'V',
        '9': 'W',
        '99': 'X',
        '999': 'Y',
        '9999': 'Z'
    }
    
    result = ""
    sections = telephone_string.split("_")
    for part in sections:
        i = 0
        while i < len(part):
            for length in range(4, 0, -1):  # Check from longest to shortest
                if part[i:i+length] in decoder_dict:
                    result += decoder_dict[part[i:i+length]]
                    i += length
                    break
    return result

telephone_decipher("444055566688833099966688022_2_22999")

