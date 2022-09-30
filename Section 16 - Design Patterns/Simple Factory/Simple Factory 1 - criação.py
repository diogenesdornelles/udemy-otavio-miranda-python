from abc import ABC, abstractmethod

# Example n. 1:


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


class Moto(ProductVehicle):
    def pick_up_customer(self) -> None:
        print('Moto is chasing the customer.')


class Truck(ProductVehicle):
    def pick_up_customer(self) -> None:
        print('Truck is chasing the customer.')


# Class factory contain method that return an instance of Products children, by polymorphism.
class VehicleFactory:
    @staticmethod
    def factory_get_vehicle(_type: str) -> ProductVehicle:
        if _type == 'luxury':
            return ConcreteLuxuryVehicle()
        elif _type == 'popular':
            return ConcretePopularVehicle()
        elif _type == 'moto':
            return Moto()
        elif _type == 'truck':
            return Truck()
        else:
            assert 0, 'The requested vehicle does not exist.'


if __name__ == '__main__':
    from random import choice
    vehicles_available = ['popular', 'luxury', 'moto', 'truck']
    for i in range(20):
        chosen = choice(vehicles_available)
        # Client program calls factory class to construct an object of concrete product classes in specific method.
        vehicle = VehicleFactory.factory_get_vehicle(chosen)
        # Now, how variable vehicle is an instance of concrete product classes, can call a method given by Abs class.
        vehicle.pick_up_customer()



