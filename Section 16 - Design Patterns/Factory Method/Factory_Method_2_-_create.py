from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List


class ProductVehicle(ABC):

    @property
    @abstractmethod
    def vehicle(self) -> str:
        raise NotImplementedError('Should implement method.')


class ConcreteLuxuryVehicle(ProductVehicle):

    @property
    def vehicle(self) -> str:
        return 'Luxury car'


class ConcretePopularVehicle(ProductVehicle):

    @property
    def vehicle(self) -> str:
        return 'Popular car'


class ConcreteMoto(ProductVehicle):

    @property
    def vehicle(self) -> str:
        return 'Moto'


class ConcreteTruck(ProductVehicle):

    @property
    def vehicle(self) -> str:
        return 'Truck'


class ConcreteVan(ProductVehicle):

    @property
    def vehicle(self) -> str:
        return 'Van'


class ProductFilial(ABC):

    def __post_init__(self):
        raise NotImplementedError('Should implement method.')

    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError('Should implement method.')

    @property
    @abstractmethod
    def vehicles_availables(self) -> list:
        raise NotImplementedError('Should implement method.')


@dataclass
class ConcreteNorthFilial(ProductFilial):
    __name: str = field(default='North Filial')
    __vehicles_availables: List = field(default_factory=list, init=False)

    def __post_init__(self):
        self.__vehicles_availables = ['luxury', 'moto', 'truck', 'van']

    @property
    def name(self) -> str:
        return self.__name

    @property
    def vehicles_availables(self) -> list:
        return self.__vehicles_availables


@dataclass
class ConcreteSouthFilial(ProductFilial):
    __name: str = field(default='South Filial')
    __vehicles_availables: List = field(default_factory=list, init=False)

    def __post_init__(self):
        self.__vehicles_availables = ['luxury', 'moto', 'truck', 'popular']

    @property
    def name(self) -> str:
        return self.__name

    @property
    def vehicles_availables(self) -> list:
        return self.__vehicles_availables


@dataclass
class ConcreteWestFilial(ProductFilial):
    __name: str = field(default='West Filial')
    __vehicles_availables: List = field(default_factory=list, init=False)

    def __post_init__(self):
        self.__vehicles_availables = ['luxury', 'moto', 'van', 'popular']

    @property
    def name(self) -> str:
        return self.__name

    @property
    def vehicles_availables(self) -> list:
        return self.__vehicles_availables


@dataclass
class ConcreteEastFilial(ProductFilial):
    __name: str = field(default='East Filial')
    __vehicles_availables: List = field(default_factory=list, init=False)

    def __post_init__(self):
        self.__vehicles_availables = ['luxury', 'var']

    @property
    def name(self) -> str:
        return self.__name

    @property
    def vehicles_availables(self) -> list:
        return self.__vehicles_availables


@dataclass
class ServiceFactory:
    __type: str
    __local: str
    __name_client: str
    __vehicle_chosen: ProductVehicle = field(default=None, init=False)
    __filial_chosen: ProductFilial = field(default=None, init=False)

    @property
    def type(self):
        return self.__vehicle_chosen

    @property
    def vehicle_chosen(self):
        return self.__vehicle_chosen

    def __post_init__(self):
        self.__vehicle_chosen = self.factory_get_vehicle(self.__type)
        self.__filial_chosen = self.factory_get_filial(self.__local)

    @staticmethod
    def factory_get_vehicle(_type: str) -> ProductVehicle:
        if _type == 'luxury':
            return ConcreteLuxuryVehicle()
        elif _type == 'popular':
            return ConcretePopularVehicle()
        elif _type == 'moto':
            return ConcreteMoto()
        elif _type == 'truck':
            return ConcreteTruck()
        elif _type == 'van':
            return ConcreteTruck()
        else:
            assert 0, 'The requested vehicle does not exist.'

    @staticmethod
    def factory_get_filial(_filial: str) -> ProductFilial:
        if _filial == 'north zone':
            return ConcreteNorthFilial()
        elif _filial == 'south zone':
            return ConcreteSouthFilial()
        elif _filial == 'west zone':
            return ConcreteWestFilial()
        elif _filial == 'east zone':
            return ConcreteEastFilial()
        else:
            assert 0, 'The requested filial does not exist.'

    # Not along creation classes. But, execution dependent validation on Factory class.
    def pick_up_customer(self):
        _vehicle_type = self.__vehicle_chosen.vehicle
        _filial_name = self.__filial_chosen.name
        if self.check_service(_vehicle_type):
            print(f'{_vehicle_type} from {_filial_name} is chasing the client {self.__name_client}.')
        else:
            print(f'{_vehicle_type} not available in {_filial_name}. Sorry, {self.__name_client}.')

    def check_service(self, _vehicle_type: str) -> bool:
        if _vehicle_type.strip().lower() in self.__filial_chosen.vehicles_availables:
            return True


if __name__ == '__main__':
    from random import choice

    vehicles_availables = ['popular', 'luxury', 'moto', 'truck', 'van']
    region = ['north zone', 'south zone', 'west zone', 'east zone']
    name = 'Raul'
    for i in range(20):
        chosen_vehicle = choice(vehicles_availables)
        chosen_region = choice(region)
        vehicle = ServiceFactory(chosen_vehicle, chosen_region, name)
        vehicle.pick_up_customer()
