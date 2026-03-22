def validate_numbers(a, b):
    """Функция для проверки типов"""

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Аргументы должны быть числами (int или float)")

def add(a, b):
    """Функция сложения"""
    validate_numbers(a, b)

    return a + b

def subtract(a, b):
    """Функция вычитания"""

    validate_numbers(a, b)

    return a - b

def multiply(a, b):
    """Функция умножения"""

    validate_numbers(a, b)

    return a * b

def divide(a, b):
    """Функция деления"""

    validate_numbers(a, b)

    if b == 0:
        raise ZeroDivisionError("Деление на ноль невозможно")

    return a / b
