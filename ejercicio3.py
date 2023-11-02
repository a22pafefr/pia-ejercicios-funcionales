"""Programa para sistema de palotes"""

def palotes(numero):
    """Convierte un número al sistema de palotes"""
    palotes_string = ""
    for i in str(numero):
        palotes_string += int(i) * "|"
        palotes_string += "-"
    return palotes_string[:-1] # Hacemos esto para quitar el último guión

print(palotes(84901))
