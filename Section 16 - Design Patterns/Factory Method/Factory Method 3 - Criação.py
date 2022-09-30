from abc import ABC, abstractmethod
from dataclasses import dataclass


class AbstractProductVehicle(ABC):

    @property
    @abstractmethod
    def vehicle(self) -> str:
        raise NotImplementedError('Should implement method.')


class ConcreteLuxuryVehicleProduct(AbstractProductVehicle):

    @property
    def vehicle(self) -> str:
        return 'Luxury car'


class ConcretePopularVehicleProduct(AbstractProductVehicle):

    @property
    def vehicle(self) -> str:
        return 'Popular car'


class ConcreteMotoProduct(AbstractProductVehicle):

    @property
    def vehicle(self) -> str:
        return 'Moto'


class ConcreteTruckProduct(AbstractProductVehicle):

    @property
    def vehicle(self) -> str:
        return 'Truck'


class ConcreteVanProduct(AbstractProductVehicle):

    @property
    def vehicle(self) -> str:
        return 'Van'


class AbstractServiceCreator(ABC):

    @property
    @abstractmethod
    def type(self):
        raise NotImplementedError('Should implement method.')

    @abstractmethod
    def factory_get_vehicle(self) -> AbstractProductVehicle:
        raise NotImplementedError('Should implement method.')

    @abstractmethod
    def pick_up_customer(self):
        raise NotImplementedError('Should implement method.')


@dataclass
class ConcreteNorthZoneVehicleCreator(AbstractServiceCreator):
    __type: str
    __name_client: str

    @property
    def type(self):
        return self.__type

    # Factory Method: The subclasses decide how classes will be created.

    def factory_get_vehicle(self) -> AbstractProductVehicle:
        if self.__type == 'luxury':
            return ConcreteLuxuryVehicleProduct()
        elif self.__type == 'popular':
            return ConcretePopularVehicleProduct()
        elif self.__type == 'moto':
            return ConcreteMotoProduct()
        elif self.__type == 'truck':
            return ConcreteTruckProduct()
        elif self.__type == 'van':
            return ConcreteTruckProduct()
        else:
            assert 0, 'The requested vehicle does not exist.'

    def pick_up_customer(self):
        vehicle_chosen = self.factory_get_vehicle()
        print(f'{vehicle_chosen.vehicle} is chasing client {self.__name_client}')


@dataclass
class ConcreteSouthZoneVehicleCreator(AbstractServiceCreator):
    __type: str
    __name_client: str

    @property
    def type(self):
        return self.__type

    # Factory Method: The subclasses decide how classes will be created.

    def factory_get_vehicle(self) -> AbstractProductVehicle:
        if self.__type == 'luxury':
            return ConcreteLuxuryVehicleProduct()
        elif self.__type == 'popular':
            return ConcretePopularVehicleProduct()
        elif self.__type == 'van':
            return ConcreteTruckProduct()
        else:
            assert 0, 'The requested vehicle does not exist.'

    def pick_up_customer(self):
        vehicle_chosen = self.factory_get_vehicle()
        print(f'{vehicle_chosen.vehicle} is chasing client {self.__name_client}.')


if __name__ == '__main__':
    from random import choice

    vehicles_availables_north = ['popular', 'luxury', 'moto', 'truck', 'van']
    name = 'Raul'
    for i in range(10):
        chosen_vehicle = choice(vehicles_availables_north)
        # Client program calls factory class to construct an object of concrete product classes and set it on attr.
        vehicle = ConcreteNorthZoneVehicleCreator(chosen_vehicle, name)
        # Now, how variable vehicle is an instance of concrete product classes, can call a method given by Abs class.
        vehicle.pick_up_customer()
    vehicles_availables_south = ['popular', 'luxury', 'van']
    name = 'Tuco'
    for i in range(10):
        chosen_vehicle = choice(vehicles_availables_south)
        # Client program calls factory class to construct an object of concrete product classes and set it on attr.
        vehicle = ConcreteSouthZoneVehicleCreator(chosen_vehicle, name)
        # Now, how variable vehicle is an instance of concrete product classes, can call a method given by Abs class.
        vehicle.pick_up_customer()
