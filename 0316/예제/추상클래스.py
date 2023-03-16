# abc모듈 import
from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def get_num_wheels(self):
        pass

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass



class Car(Vehicle):
    def get_num_wheels(self):
        return 4

    def start(self):
        print("Car started.")

    def stop(self):
        print("Car stopped.")


class Bike(Vehicle):
    def get_num_wheels(self):
        return 2

    def start(self):
        print("Bike started.")

    def stop(self):
        print("Bike stopped.")

vehicles = [Car(), Bike()]

for vehicle in vehicles:
    vehicle.start()
    vehicle.stop()

