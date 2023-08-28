from typing import Any

__all__ = (
    'corresponding_pairs',
)
"""
    Функция должна возвращать соответствующие элементы двух массивов:
    corresponding_pairs([1, 2], [3, 4]) == [(1, 3), (2, 4)]
"""

def corresponding_pairs(arr1: list[Any], arr2: list[Any]) -> list[tuple[Any, Any]]:
    min_length = min(len(arr1), len(arr2))
    result = []

    for i in range(min_length):
        result.append((arr1[i], arr2[i]))

    return result
