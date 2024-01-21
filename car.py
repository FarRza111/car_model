from typing import Union

class Car:

    def __init__(self, model:str, brand:str) -> None:
        self.model = model
        self.brand = brand

    def show_full_info(self) -> str:
        return f'This is full info of car: Model - {self.model} Brand - {self.brand}'

class SpeedyCar(Car):

    def __init__(self, model:str, brand:str, price: Union[int, float, None]) -> None:
        super().__init__(model, brand)
        self.price = price

    def show_full_info(self):
        return f'this is full price info: price is {self.price} and {self.model} is model and brand is {self.brand}'

class WeakCar:

    def __init__(self, power: Union[int, float]) -> None:
        self.power = power

    def show_full_info(self) -> str:
        return f'this is the power of car {self.power}'

class CarWanted(SpeedyCar, WeakCar):

    def __init__(self, model:str, brand:str, price: Union[float, int], power: Union[int, float]) -> None:
        SpeedyCar.__init__(self, model, brand, price)
        WeakCar.__init__(self, power)

    def provide_full_details(self)-> str:
        return f'Car model is {self.model}, brand is {self.brand}, price is {self.price}, and power is {self.power}'

if __name__ == "__main__":
    car_wanted = CarWanted('Posledniy', 'BMW', 45000, 300)
    print(car_wanted.provide_full_details())
