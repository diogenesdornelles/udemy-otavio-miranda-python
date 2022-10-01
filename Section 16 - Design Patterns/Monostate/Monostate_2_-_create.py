class StringReprMixin:
    def __str__(self):
        params = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__}({params})'

    def __repr__(self):
        return self.__str__()


class MonoStateComplex(StringReprMixin):

    _state: dict = {
        'x': 10,
        'y': 20
    }

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        obj.__dict__ = cls._state
        return obj

    def __init__(self, number_1=None, number_2=None):

        if number_1 is not None:
            self.z = number_1
        if number_2 is not None:
            self.w = number_2


class A(MonoStateComplex):
    pass


if __name__ == '__main__':
    m1 = MonoStateComplex(100, 50)
    m2 = A(60)
    m1.x = 40  # Changes for all instances. Shared states.
    print(m1)
    print(m2)
