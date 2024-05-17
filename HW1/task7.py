# Task7: Максимальный палиндром
# На вход подается строка, содержащая буквы алфавита в нижнем регистре.
# Найдите максимальный палиндром, который можно составить из этих букв и выведите его длину.
from collections import Counter


def task7(s: str) -> int:
    res = ''
    extra_letter = ''
    for i in Counter(s).items():
        number = i[1] // 2
        if number:
            res += number * i[0]
        if extra_letter or i[1] % 2 == 1:
            extra_letter = i[0]

    res = res + extra_letter + res[::-1]
    return len(res)

# print(task7('aab'))
# print(task7('abcdba'))
