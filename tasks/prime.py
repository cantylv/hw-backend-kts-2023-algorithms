__all__ = (
    'is_prime',
)

"""
    Функция должна вернуть True если число является простым, иначе - False
"""
def is_prime(number: int) -> bool:
    # Тест на простоту по Миллеру-Рабину
    if number <= 1:
        return False
    if number <= 3:
        return True

    if number % 2 == 0 or number % 3 == 0:
        return False

    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6

    return True
