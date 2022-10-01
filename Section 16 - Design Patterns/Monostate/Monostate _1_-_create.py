'''Monostate (ou Borg) -

É uma variação do Singleton proposto por Alex Martelli que tem a intenção de garantir que o
estado do objeto seja igual para todas as instâncias.

No sigleton, pretende-se que todas as instâncias da mesma classe sejam iguais. No monostate, as instãncias são
diferentes, mas os estados são os mesmos.

'''


class StringReprMixin:
    def __str__(self):
        params = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__}({params})'

    def __repr__(self):
        return self.__str__()


class A(StringReprMixin):
    def __init__(self):
        self.x = 10
        self.y = 20


class MonoStateSimple(StringReprMixin):
    _state: dict = {
        'x': 10,
        'y': 20
    }

    def __init__(self, number_1=None, number_2=None):

        self.__dict__ = self._state

        if number_1 is not None:
            self.z = number_1
        if number_2 is not None:
            self.w = number_2


if __name__ == '__main__':
    m1 = MonoStateSimple(100, 50)
    m2 = MonoStateSimple(60)
    m1.x = 40  # Changes for all instances. Shared states.
    print(m1)
    print(m2)
