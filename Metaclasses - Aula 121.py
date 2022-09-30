# Metaclasses são classes que criam classes. No exempplo. Forças a criação de
# Um método em classes filhas de A, que herdou diretamente.
# Meta pode determinar atributos, métodos e o comportamento de todas as classes filhas.

# name: nomes das classes instanciadas na metaclasse
# bases: (<class '__main__.A'>,)
# namespaces: atributos e métodos das classes instanciadas. In dict.
# mcs: <class '__main__.Meta'>; própria metaclass
from dataclasses import dataclass, field


class Meta(type):

    @staticmethod
    def __new__(mcs, name, bases, namespaces, **kwds):

        # Se for classe que herda diretamente, no caso A, mantém-se o comportamento.
        if name == 'A':
            return type.__new__(mcs, name, bases, namespaces, **kwds)

        elif name == 'B':

            # forças a implementação de 'b_fala' em B
            method_required = 'b_fala'
            if method_required not in namespaces:
                raise NotImplementedError(f'Método {method_required} não implementado em {name}.')
            else:
                if not callable(namespaces[method_required]):
                    raise NotImplementedError(f'{method_required} deve ser método, não atributo em {name}.')

            # Não permitir a subscrição de atributos em classes filhas de A.
            if 'coisa_classe' in namespaces:
                del namespaces['coisa_classe']
                raise NameError('Não há como sobrescrever attr. coisa_classe')

            return type.__new__(mcs, name, bases, namespaces, **kwds)

        # permitir que somente classes filhas 'A' ou 'B' existam:
        else:
            raise NameError(f'De metaclass "{mcs.__name__}", somente podem herdar classes nomeadas "A" ou "B"')


class A(metaclass=Meta):
    coisa_classe_A = 'Não sei'

    @staticmethod
    def fala():
        B.b_fala()


@dataclass
class B(A):

    @staticmethod
    def __new__(cls, *args, **kwargs):
        # Determinar um único objeto para classe (Singleton)

        if not cls._exists:
            cls._exists = object.__new__(cls)
        return cls._exists

        # Configurar nome único para instância.
        # name = 'b_regular_obj'
        # if name not in globals().keys():
        #     raise ValueError(f'Somente é possível instanciar classe "{cls.__name__}" '
        #                      f'usando variável "{name}"')

    _exists = None
    count: int = field(default=1, init=False)
    coisa_classe_B = 'Tambem Não sei'

    def sei_la(self):
        return self.coisa_classe_B

    @staticmethod
    def b_fala():
        return 'classe B falou'


b_regular_obj = B()
d = B()
e = B()
a = A()

print(id(b_regular_obj))
print(id(d))
print(id(e))

# criando classe a partir de type.

class Pai:
    nome = 'Jose'


C = type(
    'C',  # Nome da classe
    (Pai,),  # Se herda de alguem
    {'attr': 'Olá mundo'})  # atributos

c = C()
# print(c.nome)
