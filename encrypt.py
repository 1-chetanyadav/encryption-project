from typing import Dict
import random
# import main
seed=random.randrange(456,643)
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




def encrypt(text: str, char_map: Dict[str, str]) -> str:
    return ''.join(char_map.get(char, char) for char in text)


def mixer(mencrypt):
    char_map = create_char_map()
    
    # Example usage
    original_text = mencrypt
    encrypted_text = encrypt(original_text, char_map)
    
    return encrypted_text
# mixer(mencrypt)


