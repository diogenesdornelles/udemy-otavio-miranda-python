from dataclasses import dataclass, field
from typing import Any

# Singleton by __new__ dunder method: May cause error on new initialization.


@dataclass(unsafe_hash=True)
class AppSettings:

    __instance: Any = field(default=None, init=False)
    # problem with __init__, see bellow:
    tema: str = 'dark'
    size: str = '18px'

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance


if __name__ == '__main__':
    as1 = AppSettings()
    as1.tema = 'bright'  # Set as bright
    print(as1.tema)
    as2 = AppSettings()  # When initialized, set as default dark.
    print(as2.tema)

    # Obj are the same:
    print(id(as1))
    print(id(as2))
    print(as1 == as2)

    # All obj receives new attrs:
    as1.nome = 'Dio'
    print(as2.nome)
