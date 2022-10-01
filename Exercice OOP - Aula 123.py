from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import List


class Error(Exception):
    def __init__(self, message):
        super().__init__(message)


@dataclass
class Conta(ABC):

    @property
    @abstractmethod
    def agencia(self) -> str:
        raise NotImplementedError

    @property
    @abstractmethod
    def numero(self) -> int:
        raise NotImplementedError

    @property
    @abstractmethod
    def saldo(self) -> float:
        raise NotImplementedError

    @saldo.setter
    @abstractmethod
    def saldo(self, valor) -> None:
        raise NotImplementedError

    @abstractmethod
    def sacar(self, valor: float) -> None:
        raise NotImplementedError

    @abstractmethod
    def depositar(self, valor: float) -> None:
        raise NotImplementedError


@dataclass
class ContaCorrente(Conta):
    __agencia: str
    __numero: int
    __saldo: float = field(default=0, init=False)
    __limite: float = field(default=1000, init=False)

    @property
    def agencia(self) -> str:
        return self.__agencia

    @property
    def numero(self) -> int:
        return self.__numero

    @property
    def saldo(self) -> float:
        return self.__saldo

    @saldo.setter
    def saldo(self, valor) -> None:
        raise Error('Saldo somente pode ser modificado por depósito ou saque.')

    @property
    def limite(self) -> float:
        return self.__limite

    def sacar(self, valor: float) -> None:
        cliente_autenticado = Banco.autenticacao(self.agencia, self.numero)
        if self.saldo + self.limite > valor and cliente_autenticado:
            self.__saldo -= valor
            print(f'Cliente {cliente_autenticado.nome} \n'
                  f'(Conta n: {self.numero} \n'
                  f'Agência n. {self.agencia} \n'
                  f'Sacou {valor} \n'
                  f'Novo saldo {self.saldo} \n')
        else:
            raise Error('Cliente não autenticado ou saldo insuficiente.')

    def depositar(self, valor: float) -> None:
        self.__saldo += valor
        print(f'Conta n: {self.numero} \n'
              f'Agência n. {self.agencia} \n'
              f'Sacou {valor} \n'
              f'Novo saldo {self.saldo} \n')


@dataclass
class ContaPoupanca(Conta):
    __agencia: str
    __numero: int
    __saldo: float = field(default=0, init=False)

    @property
    def agencia(self) -> str:
        return self.__agencia

    @property
    def numero(self) -> int:
        return self.__numero

    @property
    def saldo(self) -> float:
        return self.__saldo

    @saldo.setter
    def saldo(self, valor) -> None:
        raise Error('Saldo somente pode ser modificado por depósito ou saque.')

    def sacar(self, valor: float) -> None:
        cliente_autenticado = Banco.autenticacao(self.agencia, self.numero)
        if self.saldo > valor and cliente_autenticado:
            self.__saldo -= valor
            print(f'Cliente {cliente_autenticado.nome} \n'
                  f'(Conta n: {self.numero} \n'
                  f' agência n. {self.agencia}) \n'
                  f'sacou {valor} \n'
                  f'Novo saldo {self.saldo} \n')

    def depositar(self, valor: float) -> None:
        self.__saldo += valor


@dataclass
class Pessoa(ABC):

    @property
    @abstractmethod
    def nome(self) -> str:
        raise NotImplementedError

    @nome.setter
    @abstractmethod
    def nome(self, value) -> None:
        raise NotImplementedError

    @property
    @abstractmethod
    def idade(self) -> int:
        raise NotImplementedError


@dataclass
class Cliente(Pessoa):
    __nome: str
    __idade: int
    __conta: [ContaCorrente | ContaPoupanca]

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def conta(self):
        return self.__conta

    @property
    def idade(self):
        return self.__idade


def _agencias() -> list:
    agencias_bancarias = ['181-0', '183-4', '189-2']
    return agencias_bancarias


class Banco:
    agencias = _agencias()
    contas_numero = []
    clientes = []
    info_clientes: List[Cliente] = []

    @classmethod
    def adicionar_cliente(cls, new: Cliente) -> None:

        if new.conta.agencia not in cls.agencias:
            raise Error('Agência não encontrada.')
        else:
            cls.info_clientes.append(new)
            cls.contas_numero.append(new.conta.numero)
            cls.clientes.append(new.nome)

    @classmethod
    def autenticacao(cls, agencia, numero) -> [str | None]:
        if agencia in cls.agencias and numero in cls.contas_numero:
            for cliente in cls.info_clientes:
                if numero == cliente.conta.numero:
                    return cliente
        else:
            raise Error('Falha na autenticação.')

    @classmethod
    def sacar(cls, agencia, conta, valor):
        cliente = cls.autenticacao(agencia, conta)
        cliente.conta.sacar(valor)

    @classmethod
    def depositar(cls, agencia, conta, valor):
        cliente = cls.autenticacao(agencia, conta)
        cliente.conta.depositar(valor)


CC_1 = ContaCorrente('181-0', 123)
person = Cliente('Ned', 60, CC_1)
banco = Banco()
banco.adicionar_cliente(person)
person.conta.depositar(4000)
person.conta.sacar(1000)
Banco.sacar('181-0', 123, 1000)
