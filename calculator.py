def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Ошибка: деление на ноль"

def power(a, b):
    """Возводит число a в степень b."""
    return a ** b

if __name__ == "__main__":
    print("Сложение:", add(10, 5))
    print("Вычитание:", subtract(10, 5))
    print("Умножение:", multiply(10, 5))
    print("Деление:", divide(10, 5))
    print("Возведение в степень:", power(10, 2))
