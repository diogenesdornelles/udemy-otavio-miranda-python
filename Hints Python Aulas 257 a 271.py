from typing import Callable



# CALLABLE
DataFunc = Callable[[int, int], int]


def _exec(func: DataFunc, a: int, b: int) -> int:
    c = func(a, b)
    return c


def sum_n(a, b):
    c = a + b
    return c


a = _exec(sum_n, 2, 3)
print(a)
