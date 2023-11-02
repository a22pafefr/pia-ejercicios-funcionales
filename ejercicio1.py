"""Programa que permite realizar operaciones matemáticas básicas"""

# pylint: disable=C0103
n1 = 0
n2 = 0
are_numbers_input = False

def menu(menu_options):
    """Menu de opciones"""
    while True:
        print("------------------------------------------------------------")
        for menu_number, menu_item in menu_options.items():
            if "conditional" in menu_item and are_numbers_input is False:
                continue
            print(menu_number, menu_item["text"])
        print("------------------------------------------------------------")
        option = int(input("Selecciona una opción: "))
        if option in menu_options:
            menu_options[option]["function"]()
        else:
            print("Opción no válida")

def input_numbers():
    """Input de dos números"""
    global n1
    global n2
    n1 = int(input("Ingrese el primer número:"))
    n2 = int(input("Ingrese el segundo número:"))
    global are_numbers_input
    are_numbers_input = True

def sums():
    """Suma de dos números"""
    print(f"El resultado de {n1} + {n2} es: {n1 + n2}")

def substract():
    """Resta de dos números"""
    print(f"El resultado de {n1} - {n2} es: {n1 - n2}")

def multiply():
    """Multiplicación de dos números"""
    print(f"El resultado de {n1} * {n2} es: {n1 * n2}")

def divide():
    """División de dos números"""
    print(f"El resultado de {n1} / {n2} es: {n1 / n2}")

options = {
    0: {
        "text": "Ingresar números",
        "function": input_numbers
    },
    1: {
        "text": "Sumar",
        "function": sums,
        "conditional": True
    },
    2: {
        "text": "Restar",
        "function": substract,
        "conditional": True
    },
    3: {
        "text": "Multiplicar",
        "function": multiply,
        "conditional": True
    },
    4: {
        "text": "Dividir",
        "function": divide,
        "conditional": True
    },
    5: {
        "text": "Salir",
        "function": exit
    }
}

menu(options)
