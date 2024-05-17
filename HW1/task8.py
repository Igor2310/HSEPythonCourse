from typing import Union, List, Tuple
import numpy as np


# заменил int|float на "int|float" для своей версии python
class Statistics:
    def __init__(self, data: Union[List["int|float"], Tuple["int|float"], np.ndarray["int|float"]]):
        """
        Пара моментов:
            1. массив всегда 1D, т.е. просто вектор
            2. степенями свободы можете принебречь
        """
        self.data = np.array(data)

    def calculate_mean(self) -> "float | int":
        # считаем среднюю от self.data
        return self.data.mean()

    def calculate_median(self) -> "float | int":
        # считаем медиану от self.data
        return np.median(self.data)

    def calculate_mode(self) -> "float | int":
        # считаем моду от self.data
        """
        в случае если два и более объекта встречаются одинаковое количество раз
        модой будет наибольший из них
        
        Пример1:
        data = [1,2,2,3]
        out: 2
        
        Пример2:
        data = [1,2,3]
        out: 3
        """
        # find unique values in array along with their counts
        vals, counts = np.unique(self.data, return_counts=True)

        # find mode
        mode_value = np.argwhere(counts == np.max(counts))
        # search for the greatest mode
        return max(vals[mode_value].flatten().tolist())

    def std(self) -> "float | int":
        # считаем стандартное отклонение (не дисперсию)
        return np.std(self.data)

    def iqr(self) -> "float | int":
        # считаем интерквартильный размах: https://shorturl.at/rsuBK
        return np.quantile(self.data, 0.75) - np.quantile(self.data, 0.25)

#a=Statistics([1,2,3,3,4,5,6,7,7,8,9,10])
