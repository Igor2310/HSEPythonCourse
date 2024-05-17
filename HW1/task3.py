# Task3: Возрастает ли список?
# Дан список. Определите, является ли он монотонно возрастающим
# (то есть верно ли, что каждый элемент этого списка больше предыдущего).

from typing import List


def task3(l: List[int]) -> bool:
    # Loop to check if array is increasing
    for i in range(0, len(l) - 1):
        # To check if array is not increasing
        if l[i] >= l[i + 1]:
            return False
    return True


# print(task3([1, 2, 3, 4]))
# print(task3([-1, -2, 4, -3, 4]))
# print(task3([2, 2, 2]))
