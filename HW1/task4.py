# На вход подается строка, выведите количество уникальных гласных в ней
# (гласные это [а,у,о,ы,э,я,ю,ё,и,е]).
def task4(s: str) -> int:
    s = s.lower()
    s = set([letter for letter in s])
    vowels = ['а', 'у', 'о', 'ы', 'э', 'я', 'ю', 'ё', 'и', 'е']
    return len(s.intersection(vowels))

# print(task4("ауеив"))
# print(task4("ааааа"))
