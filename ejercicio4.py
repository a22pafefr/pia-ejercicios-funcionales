"""Programa para sistema Morse"""

def morse(numero):
    """Convierte un número al sistema Morse"""
    morse_string = ""
    for i in str(numero):
        match i:
            case "0":
                morse_string += "----- "
            case "1":
                morse_string += "·---- "
            case "2":
                morse_string += "··--- "
            case "3":
                morse_string += "···-- "
            case "4":
                morse_string += "····- "
            case "5":
                morse_string += "····· "
            case "6":
                morse_string += "-···· "
            case "7":
                morse_string += "--··· "
            case "8":
                morse_string += "---·· "
            case "9":
                morse_string += "----· "
            case _:
                morse_string += " "
    return morse_string[:-1] # Hacemos esto para quitar el último espacio

print(morse(213))
