from abc import ABC, abstractmethod
from dataclasses import dataclass, field


# Example n. 2: All services are operated by Factory.


# Abs class forces all concretes classes to implement same methods.
class ProductVehicle(ABC):
    @abstractmethod
    def pick_up_customer(self) -> str:
        raise NotImplementedError('Should implement method.')


class ConcreteLuxuryVehicle(ProductVehicle):
    def pick_up_customer(self) -> str:
        return 'Luxury car'


class ConcretePopularVehicle(ProductVehicle):
    def pick_up_customer(self) -> str:
        return 'Popular car'


class ConcreteMoto(ProductVehicle):
    def pick_up_customer(self) -> str:
        return 'Moto'


class ConcreteTruck(ProductVehicle):
    def pick_up_customer(self) -> str:
        return 'Truck'


class ProductFilial(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError('Should implement method.')


@dataclass
class ConcreteNorthFilial(ProductFilial):
    __name: str = field(default='North Filial')

    @property
    def name(self) -> str:
        return self.__name


@dataclass
class ConcreteSouthFilial(ProductFilial):
    __name: str = field(default='South Filial')

    @property
    def name(self) -> str:
        return self.__name


@dataclass
class ConcreteWestFilial(ProductFilial):
    __name: str = field(default='West Filial')

    @property
    def name(self) -> str:
        return self.__name


@dataclass
class ConcreteEastFilial(ProductFilial):
    __name: str = field(default='East Filial')

    @property
    def name(self) -> str:
        return self.__name


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
        else:
            assert 0, 'The requested vehicle does not exist.'

    @staticmethod
    def factory_get_filial(_filial: str) -> ProductFilial:
        if _filial == 'north zone':
            return ConcreteNorthFilial()
        elif _filial == 'south Zone':
            return ConcreteSouthFilial()
        elif _filial == 'west Zone':
            return ConcreteWestFilial()
        elif _filial == 'east zone':
            return ConcreteEastFilial()
        else:
            assert 0, 'The requested filial does not exist.'

    # Wrapper: Method bellow calls same method from object instantiate at attr.
    def pick_up_customer(self):
        _vehicle = self.__vehicle_chosen.pick_up_customer()
        filial_name = self.__filial_chosen.name
        print(f'{_vehicle} from {filial_name} is chasing the client {self.__name_client}.')


if __name__ == '__main__':
    from random import choice

    vehicles_availables = ['popular', 'luxury', 'moto', 'truck']
    region = ['north zone', 'south Zone', 'west Zone', 'east zone']
    name = 'Raul'
    for i in range(20):
        chosen_vehicle = choice(vehicles_availables)
        chosen_region = choice(region)
        # Client program calls factory class to construct an object of concrete product classes and set it on attr.
        vehicle = ServiceFactory(chosen_vehicle, chosen_region, name)
        # Now, how variable vehicle is an instance of concrete product classes, can call a method given by Abs class.
        vehicle.pick_up_customer()
