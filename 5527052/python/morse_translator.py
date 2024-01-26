def morse_translator(text):
    morse_code_dict = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
    }
    
    text = text.upper()

    morse_code = []
    for char in text:
        if char.isalpha():
            morse_code.append(morse_code_dict[char])
        elif char == " ":
            morse_code.append("/")
    
    return " " .join(morse_code)

print(morse_translator("HELLO WORLD"))  
print(morse_translator("Python"))      
print(morse_translator("Morse Code"))   
