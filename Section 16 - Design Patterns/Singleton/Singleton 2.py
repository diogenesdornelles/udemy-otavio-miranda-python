from dataclasses import dataclass

# Singleton by function decorator: Without error on a new initialization.


def singleton(_class):
    instances = {}

    def get_class(*args, **kwargs):
        if _class not in instances:
            instances[_class] = _class(*args, **kwargs)
        return instances[_class]

    return get_class


@singleton
@dataclass
class AppSettings:
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

