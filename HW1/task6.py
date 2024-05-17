# Task6: Наибольшая подстрока палиндром
# На вход подается строка, найдите максимальную по длине подстроку,
# которая является палиндромом и выведите ее длину.


def task6(s: str) -> int:
    res = 0

    def get_pal(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return len(s[left + 1:right])

    for i in range(len(s)):
        op1, op2 = get_pal(s, i, i), get_pal(s, i, i + 1)
        if op1 > res:
            res = op1
        if op2 > res:
            res = op2
    return res


# print(task6("cdaaabca"))
# print(task6("ab"))