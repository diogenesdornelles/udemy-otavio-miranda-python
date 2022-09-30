from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum, unique


@unique
class TypeVehicle(Enum):
    LUXURY_CAR = 1
    POPULAR_CAR = 2
    LUXURY_MOTO = 3
    POPULAR_MOTO = 4
    LUXURY_VAN = 5
    POPULAR_VAN = 6
    POPULAR_TRUCK = 7


@unique
class TypeZone(Enum):
    NORTH_ZONE = 1
    SOUTH_ZONE = 2


available_zones = [TypeZone.NORTH_ZONE,
                   TypeZone.SOUTH_ZONE]

available_vehicles = [TypeVehicle.POPULAR_VAN,
                      TypeVehicle.POPULAR_TRUCK,
                      TypeVehicle.POPULAR_CAR,
                      TypeVehicle.LUXURY_VAN,
                      TypeVehicle.POPULAR_MOTO,
                      TypeVehicle.LUXURY_MOTO,
                      TypeVehicle.LUXURY_CAR
                      ]


class AbstractProductLuxuryVehicle(ABC):

    @property
    @abstractmethod
    def vehicle_description(self) -> str:
        raise NotImplementedError('Should implement method.')


class ConcreteZNLuxuryCarProduct(AbstractProductLuxuryVehicle):

    @property
    def vehicle_description(self) -> str:
        return 'Luxury car ZN'


class ConcreteZNMotoLuxuryProduct(AbstractProductLuxuryVehicle):

    @property
    def vehicle_description(self) -> str:
        return 'Luxury moto ZN'


class ConcreteZNVanLuxuryProduct(AbstractProductLuxuryVehicle):

    @property
    def vehicle_description(self) -> str:
        return 'Luxury van ZN'


class ConcreteZSLuxuryCarProduct(AbstractProductLuxuryVehicle):

    @property
    def vehicle_description(self) -> str:
        return 'Luxury car ZS'


class ConcreteZSMotoLuxuryProduct(AbstractProductLuxuryVehicle):

    @property
    def vehicle_description(self) -> str:
        return 'Luxury moto ZS'


class ConcreteZSVanLuxuryProduct(AbstractProductLuxuryVehicle):

    @property
    def vehicle_description(self) -> str:
        return 'Luxury van ZS'


class AbstractProductPopularVehicle(ABC):

    @property
    @abstractmethod
    def vehicle_description(self) -> str:
        raise NotImplementedError('Should implement method.')


class ConcreteZNPopularCarProduct(AbstractProductPopularVehicle):

    @property
    def vehicle_description(self) -> str:
        return 'Popular car ZN'


class ConcreteZNMotoPopularProduct(AbstractProductPopularVehicle):

    @property
    def vehicle_description(self) -> str:
        return 'Popular moto ZN'


class ConcreteZNTruckPopularProduct(AbstractProductPopularVehicle):

    @property
    def vehicle_description(self) -> str:
        return 'Popular truck ZN'


class ConcreteZNVanPopularProduct(AbstractProductPopularVehicle):

    @property
    def vehicle_description(self) -> str:
        return 'Popular van ZN'


class ConcreteZSPopularCarProduct(AbstractProductPopularVehicle):

    @property
    def vehicle_description(self) -> str:
        return 'Popular car ZS'


class ConcreteZSMotoPopularProduct(AbstractProductPopularVehicle):

    @property
    def vehicle_description(self) -> str:
        return 'Popular moto ZS'


class ConcreteZSTruckPopularProduct(AbstractProductPopularVehicle):

    @property
    def vehicle_description(self) -> str:
        return 'Popular truck ZS'


class ConcreteZSVanPopularProduct(AbstractProductPopularVehicle):

    @property
    def vehicle_description(self) -> str:
        return 'Popular van ZS'


class AbstractServiceFactory(ABC):

    @abstractmethod
    def factory_get_luxury_car(self) -> AbstractProductLuxuryVehicle:
        raise NotImplementedError('Should implement method.')

    @abstractmethod
    def factory_get_luxury_moto(self) -> AbstractProductLuxuryVehicle:
        raise NotImplementedError('Should implement method.')

    @abstractmethod
    def factory_get_luxury_van(self) -> AbstractProductLuxuryVehicle:
        raise NotImplementedError('Should implement method.')

    @abstractmethod
    def factory_get_popular_car(self) -> AbstractProductPopularVehicle:
        raise NotImplementedError('Should implement method.')

    @abstractmethod
    def factory_get_popular_moto(self) -> AbstractProductPopularVehicle:
        raise NotImplementedError('Should implement method.')

    @abstractmethod
    def factory_get_popular_van(self) -> AbstractProductPopularVehicle:
        raise NotImplementedError('Should implement method.')

    @abstractmethod
    def factory_get_popular_truck(self) -> AbstractProductPopularVehicle:
        raise NotImplementedError('Should implement method.')


@dataclass
class ConcreteNorthZoneVehicleFactory(AbstractServiceFactory):

    def factory_get_luxury_car(self) -> AbstractProductLuxuryVehicle:
        return ConcreteZNLuxuryCarProduct()

    def factory_get_luxury_moto(self) -> AbstractProductLuxuryVehicle:
        return ConcreteZNMotoLuxuryProduct()

    def factory_get_luxury_van(self) -> AbstractProductLuxuryVehicle:
        return ConcreteZNVanLuxuryProduct()

    def factory_get_popular_car(self) -> AbstractProductPopularVehicle:
        return ConcreteZNPopularCarProduct()

    def factory_get_popular_moto(self) -> AbstractProductPopularVehicle:
        return ConcreteZNMotoPopularProduct()

    def factory_get_popular_van(self) -> AbstractProductPopularVehicle:
        return ConcreteZNVanPopularProduct()

    def factory_get_popular_truck(self) -> AbstractProductPopularVehicle:
        return ConcreteZNTruckPopularProduct()


@dataclass
class ConcreteSouthZoneVehicleFactory(AbstractServiceFactory):

    def factory_get_luxury_car(self) -> AbstractProductLuxuryVehicle:
        return ConcreteZSLuxuryCarProduct()

    def factory_get_luxury_moto(self) -> AbstractProductLuxuryVehicle:
        return ConcreteZSMotoLuxuryProduct()

    def factory_get_luxury_van(self) -> AbstractProductLuxuryVehicle:
        return ConcreteZSVanLuxuryProduct()

    def factory_get_popular_car(self) -> AbstractProductPopularVehicle:
        return ConcreteZSPopularCarProduct()

    def factory_get_popular_moto(self) -> AbstractProductPopularVehicle:
        return ConcreteZSMotoPopularProduct()

    def factory_get_popular_van(self) -> AbstractProductPopularVehicle:
        return ConcreteZSVanPopularProduct()

    def factory_get_popular_truck(self) -> AbstractProductPopularVehicle:
        return ConcreteZSTruckPopularProduct()


@dataclass
class Client:
    __name: str
    __zone: TypeZone
    __requested_type_car: TypeVehicle
    __new_service: AbstractServiceFactory = field(default=None, init=False)
    __vehicle: AbstractProductLuxuryVehicle | AbstractProductPopularVehicle = field(default=None, init=False)

    def __post_init__(self):

        match self.__zone.name.lower():

            case 'north_zone':

                self.__new_service = ConcreteNorthZoneVehicleFactory()
                match self.__requested_type_car.name.lower():
                    case 'luxury_car':
                        self.__vehicle = self.__new_service.factory_get_luxury_car()

                    case 'luxury_moto':
                        self.__vehicle = self.__new_service.factory_get_luxury_moto()

                    case 'luxury_van':
                        self.__vehicle = self.__new_service.factory_get_luxury_van()

                    case 'popular_car':
                        self.__vehicle = self.__new_service.factory_get_popular_car()

                    case 'popular_moto':
                        self.__vehicle = self.__new_service.factory_get_popular_moto()

                    case 'popular_van':
                        self.__vehicle = self.__new_service.factory_get_popular_van()

                    case 'popular_truck':
                        self.__vehicle = self.__new_service.factory_get_popular_truck()

                    case _:
                        pass

            case 'south_zone':
                self.__new_service = ConcreteSouthZoneVehicleFactory()
                match self.__requested_type_car.name.lower():
                    case 'luxury_car':
                        self.__vehicle = self.__new_service.factory_get_luxury_car()

                    case 'luxury_moto':
                        self.__vehicle = self.__new_service.factory_get_luxury_moto()

                    case 'luxury_van':
                        self.__vehicle = self.__new_service.factory_get_luxury_van()

                    case 'popular_car':
                        self.__vehicle = self.__new_service.factory_get_popular_car()

                    case 'popular_moto':
                        self.__vehicle = self.__new_service.factory_get_popular_moto()

                    case 'popular_van':
                        self.__vehicle = self.__new_service.factory_get_popular_van()

                    case 'popular_truck':
                        self.__vehicle = self.__new_service.factory_get_popular_truck()
                    case _:
                        pass

    def pick_up_client(self):
        print(f'{self.__vehicle.vehicle_description} is chasing client {self.__name}.')


if __name__ == '__main__':
    from random import choice

    for i in range(10):
        name = 'Jojo'
        choices = [name, choice(available_zones), choice(available_vehicles)]
        client = Client(*choices)
        client.pick_up_client()
