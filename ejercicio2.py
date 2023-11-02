"""Programa que contiene funciones para trabajar con números enteros."""

def is_palindromic(num):
    """
    Devuelve True si el número pasado como parámetro es palindrómico, False en caso contrario.
    """
    return num == turn(num)

def is_prime(num):
    """
    Devuelve True si el número pasado como parámetro es primo, False en caso contrario.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def next_prime(num):
    """
    Devuelve el menor número primo mayor que el número pasado como parámetro.
    """
    num += 1
    while not is_prime(num):
        num += 1
    return num

def digits(num):
    """
    Devuelve el número de dígitos de un número entero.
    """
    count = 0
    while num > 0:
        count += 1
        num //= 10
    return count

def turn(num):
    """
    Devuelve el número pasado como parámetro con sus dígitos invertidos.
    """
    reversed_num = 0
    while num > 0:
        reversed_num = reversed_num * 10 + num % 10
        num //= 10
    return reversed_num

def digit_n(num, n):
    """
    Devuelve el dígito en la posición n (contando desde 0 y de izquierda a derecha)
    de un número entero.
    """
    return (num // 10 ** (digits(num) - n - 1)) % 10

def digit_position(num, digit):
    """
    Devuelve la posición de la primera ocurrencia de un dígito dentro de un número entero.
    Si no se encuentra el dígito, devuelve -1.
    """
    position = 0
    while num > 0:
        if num % 10 == digit:
            return position
        num //= 10
        position += 1
    return -1

def remove_behind(num, n):
    """
    Devuelve el número pasado como parámetro con n dígitos eliminados por la derecha.
    """
    return num // 10 ** n

def remove_ahead(num, n):
    """
    Devuelve el número pasado como parámetro con n dígitos eliminados por la izquierda.
    """
    return num % 10 ** (digits(num) - n)

def paste_behind(num, digit):
    """
    Devuelve el número pasado como parámetro con un dígito añadido por la derecha.
    """
    return num * 10 + digit

def paste_ahead(num, digit):
    """
    Devuelve el número pasado como parámetro con un dígito añadido por la izquierda.
    """
    return digit * 10 ** digits(num) + num

def piece_of_number(num, start, end):
    """
    Devuelve el trozo del número pasado como parámetro que empieza en la posición start
    (contando desde 0 y de izquierda a derecha) y termina en la posición end (inclusive).
    """
    return (num // 10 ** (digits(num) - end - 1)) % 10 ** (end - start + 1)

def put_numbers_together(num1, num2):
    """
    Devuelve la concatenación de los dos números pasados como parámetros.
    """
    return num1 * 10 ** digits(num2) + num2

# is_palindromic
print(f"Prueba de is_palindromic: {is_palindromic(12321)}")

# is_prime
print(f"Prueba de is_prime: {is_prime(7)}")

# next_prime
print(f"Prueba de next_prime: {next_prime(7)}")

# digits
print(f"Prueba de digits: {digits(12345)}")

# turn
print(f"Prueba de turn: {turn(12345)}")

# digit_n
print(f"Prueba de digit_n: {digit_n(12345, 2)}")

# digit_position
print(f"Prueba de digit_position: {digit_position(12345, 2)}")

# remove_behind
print(f"Prueba de remove_behind: {remove_behind(12345, 2)}")

# remove_ahead
print(f"Prueba de remove_ahead: {remove_ahead(12345, 2)}")

# paste_behind
print(f"Prueba de paste_behind: {paste_behind(12345, 6)}")

# paste_ahead
print(f"Prueba de paste_ahead: {paste_ahead(12345, 6)}")

# piece_of_number
print(f"Prueba de piece_of_number: {piece_of_number(12345, 1, 3)}")

# put_numbers_together
print(f"Prueba de put_numbers_together: {put_numbers_together(123, 456)}")
