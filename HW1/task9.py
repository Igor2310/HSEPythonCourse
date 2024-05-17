# Task 9: Спираль
# Выведите таблицу (print) размером nxn, заполненную числами от 1 до $n^2$ по спирали,
# выходящей из левого верхнего угла и закрученной по часовой стрелке.

def task9(n: int) -> None:
    if type(n) is not int: return []
    i, j, dir, result = 0, 0, 0, [[0] * n for _ in range(n)]
    for x in range(1, n * n + 1):
        result[i][j] = x
        if dir == 0:
            if j == n - 1 or result[i][j + 1]:
                i, j, dir = i + 1, j, 1
            else:
                j += 1
        elif dir == 1:
            if i == n - 1 or result[i + 1][j]:
                i, j, dir = i, j - 1, 2
            else:
                i += 1
        elif dir == 2:
            if j == 0 or result[i][j - 1]:
                i, j, dir = i - 1, j, 3
            else:
                j -= 1
        else:
            if i == 0 or result[i - 1][j]:
                i, j, dir = i, j + 1, 0
            else:
                i -= 1
    for row in result:
        print(*row)

# task9(5)