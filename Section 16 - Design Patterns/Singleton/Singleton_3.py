from dataclasses import dataclass


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if not cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


@dataclass
class AppSettings(metaclass=Singleton):
    tema: str = 'dark'
    size: str = '18px'


if __name__ == '__main__':
    as1 = AppSettings()
    as1.tema = 'bright'  # Set as bright.

    print(as1.tema)
    as2 = AppSettings()  # When initialized, NOT set as default dark. Keeps bright.
    print(as2.tema)

    # Obj are the same:
    print(id(as1))
    print(id(as2))
    print(as1 == as2)

    # All obj receives new attrs:
    as1.nome = 'Dio'
    print(as2.nome)

