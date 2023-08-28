from typing import Optional
import re

__all__ = (
    'find_shortest_longest_word',
)

"""
    В переданном тексте вернуть слово имеющее наименьшую и наибольшую длину.
    Если такого слова нет - вернуть None
    """

def find_shortest_longest_word(text: str) -> tuple[Optional[str], Optional[str]]:
    # Извлечение всех слов из текста
    words = re.findall(r'\b\w+\b', text)
    if not words:
        return (None, None)

    min_word = min(words, key=len)
    max_word = max(words, key=len)

    return (min_word, max_word)
