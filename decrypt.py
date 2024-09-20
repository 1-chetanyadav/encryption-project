from typing import Dict
# import main

def create_char_map() -> Dict[str, str]:
    # Define a bijective character-to-character mapping
    return {
        'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5',
        'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0',
        'k': '!', 'l': '@', 'm': '#', 'n': '$', 'o': '%',
        'p': '^', 'q': '&', 'r': '*', 's': '_', 't': ')',
        'u': '-', 'v': '(', 'w': '=', 'x': '+', 'y': '[',
        'z': ']', ' ': ' '  # Including space for completeness
    }



def invert_char_map(char_map: Dict[str, str]) -> Dict[str, str]:
    # Create the inverse of the character map for decryption
    return {v: k for k, v in char_map.items()}


def decrypt(encrypted_text: str, inverse_char_map: Dict[str, str]) -> str:
    return ''.join(inverse_char_map.get(char, char) for char in encrypted_text)



def dixer(unmessage):
    encoded_text = unmessage
    char_map = create_char_map()
    inverse_char_map = invert_char_map(char_map)
    decrypted_text = decrypt(encoded_text, inverse_char_map)
    print(f"Decrypted Text: {decrypted_text}")


