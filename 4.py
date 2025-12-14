# Задача 1: Замыкание, возвращающее только уникальные значения из переданных

def unique_values_closure():
    """
    Замыкание, которое сохраняет и возвращает только уникальные значения
    """
    seen_values = set()
    
    def inner(*args):
        new_values = [x for x in args if x not in seen_values]
        seen_values.update(new_values)
        return new_values
    
    return inner

# Задача 2: Декоратор, ограничивающий количество вызовов функций

def call_limiter(max_calls):
    """
    Декоратор, который ограничивает количество вызовов функции
    """
    def decorator(func):
        call_count = 0
        
        def wrapper(*args, **kwargs):
            nonlocal call_count
            if call_count >= max_calls:
                raise RuntimeError(f"Функция {func.__name__} была вызвана более {max_calls} раз")
            call_count += 1
            print(f"Вызов {call_count}/{max_calls} функции {func.__name__}")
            return func(*args, **kwargs)
        
        return wrapper
    return decorator

# Применение декоратора к замыканию

@call_limiter(3)
def get_unique_values(*args):
    """
    Функция с декоратором, которая использует замыкание для возврата уникальных значений
    """
    unique_func = unique_values_closure()
    return unique_func(*args)

# Дополнительные примеры использования

# Пример с декоратором на обычной функции
@call_limiter(2)
def multiply(a, b):
    """Простая функция умножения с ограничением вызовов"""
    return a * b

@call_limiter(5)
def factorial(n):
    """Рекурсивное вычисление факториала с ограничением вызовов"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Тестирование
if __name__ == "__main__":
    print("=== Тестирование замыкания уникальных значений ===")
    
    unique_func = unique_values_closure()
    
    print("Первые значения [1, 2, 3]:", unique_func(1, 2, 3))
    print("Повторные значения [1, 2, 4]:", unique_func(1, 2, 4))
    print("Новые значения [5, 6]:", unique_func(5, 6))
    print("Все повторные [1, 2, 3, 4, 5, 6]:", unique_func(1, 2, 3, 4, 5, 6))
    
    print("\n=== Тестирование декоратора ограничения вызовов ===")
    
    # Тестирование функции с декоратором
    try:
        print("Уникальные значения с ограничением вызовов:")
        print("Вызов 1:", get_unique_values(1, 2, 3))
        print("Вызов 2:", get_unique_values(2, 3, 4))
        print("Вызов 3:", get_unique_values(5, 6))
        print("Вызов 4 (должен вызвать ошибку):", get_unique_values(7, 8))
    except RuntimeError as e:
        print(f"Ошибка: {e}")
    
    print("\n=== Тестирование декоратора на других функциях ===")
    
    # Тестирование функции multiply
    try:
        print("Умножение:")
        print("2 * 3 =", multiply(2, 3))
        print("4 * 5 =", multiply(4, 5))
        print("6 * 7 =", multiply(6, 7))  # Должен вызвать ошибку
    except RuntimeError as e:
        print(f"Ошибка: {e}")
    
    # Тестирование функции factorial
    try:
        print("\nФакториал:")
        print("factorial(3) =", factorial(3))
        print("factorial(4) =", factorial(4))
    except RuntimeError as e:
        print(f"Ошибка: {e}")
    
    print("\n=== Демонстрация состояния замыкания ===")
    
    # Создаем новое замыкание для демонстрации независимости состояния
    another_unique = unique_values_closure()
    print("Новое замыкание [1, 2]:", another_unique(1, 2))
    print("Старое замыкание [1, 2]:", unique_func(1, 2))