import enum
from enum import Enum, auto, IntFlag

# Útil para criar enumerações de escolha, através de um tipo de dado, auxiliando no type hinting.

class Directions(Enum):
    right = auto()
    left = auto()
    up = auto()
    down = auto()


def move(direction: Directions):
    return f'Moving {direction.name}'


if __name__ == '__main__':
    print(move(Directions.right))
    print(move(Directions.down))
    print(move(Directions.up))
    print(move(Directions.left))
