from abc import ABC, abstractmethod
from dataclasses import dataclass, field

# Example n. 2: All services are operated by Factory.


# Abs class forces all concretes classes to implement same methods.
class ProductVehicle(ABC):
    @abstractmethod
    def pick_up_customer(self) -> None:
        raise NotImplementedError('Should implement method.')


class ConcreteLuxuryVehicle(ProductVehicle):
    def pick_up_customer(self) -> None:
        print('Luxury car is chasing the customer.')


class ConcretePopularVehicle(ProductVehicle):
    def pick_up_customer(self) -> None:
        print('Popular car is chasing the customer.')


class ConcreteMoto(ProductVehicle):
    def pick_up_customer(self) -> None:
        print('Moto is chasing the customer.')


class ConcreteTruck(ProductVehicle):
    def pick_up_customer(self) -> None:
        print('Truck is chasing the customer.')


# Class factory contain attr that is an instance of Products children (composition).
@dataclass
class VehicleFactory:
    __type: str
    __vehicle_chosen: ProductVehicle = field(default=None, init=False)

    @property
    def vehicle_chosen(self):
        return self.__vehicle_chosen

    def __post_init__(self):
        self.__vehicle_chosen = self.factory_get_vehicle(self.__type)

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

    # Wrapper: Method bellow calls same method from object instantiate at attr.
    def pick_up_customer(self):
        self.__vehicle_chosen.pick_up_customer()


if __name__ == '__main__':
    from random import choice
    vehicles_availables = ['popular', 'luxury', 'moto', 'truck']
    for i in range(20):
        chosen = choice(vehicles_availables)
        # Client program calls factory class to construct an object of concrete product classes and set it on attr.
        vehicle = VehicleFactory(chosen)
        # Now, how variable vehicle is an instance of concrete product classes, can call a method given by Abs class.
        vehicle.pick_up_customer()
