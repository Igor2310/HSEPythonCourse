# Task5: Палиндром
# На вход подается строка, выведите True если она является палиндромом и False иначе.


def task5(s: str) -> bool:
    length = len(s)
    s = s.lower()
    if length == 1:
        return True
    else:
        return s[:length // 2] == s[-(length // 2):][::-1]

# print(task5("acbca"))
# print(task5("ab"))