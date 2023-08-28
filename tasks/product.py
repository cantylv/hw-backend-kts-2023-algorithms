from typing import Any

__all__ = (
    'cartesian_product',
)
"""
    Должна возвращать все пары элементы двух массивов:
    cartesian_product([1, 2], [3, 4]) == [(1, 3), (1, 4), (2, 3), (2, 4)]
    """


def cartesian_product(arr1: list[Any], arr2: list[Any]) -> list:
    result = []
    for item1 in arr1:
        for item2 in arr2:
            result.append((item1, item2))
    return result

