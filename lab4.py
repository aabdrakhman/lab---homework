from dataclasses import dataclass

@dataclass 
class Person:
    full_name: str
    age: int

    def __str__(self) -> str:
        return f"ФИО: {self.full_name}, возраст: {self.age}"


@dataclass
class Engine:
    power: int
    company: str

    def __str__(self) -> str:
        return f"Сила {self.power}, производитель {self.company}"


@dataclass
class Driver(Person):
    experience: int

    def __str__(self) -> str:
        return super().__str__() + f" Опыт вождения {self.experience}"


@dataclass
class Car:
    marka: str
    car_class: str
    weight: float
    driver: Driver
    engine: Engine

    def start(self) -> str:
        return "Поехали"

    
    def stop(self) -> str:
        return "Останавливаемся"


    def turnRight(self) -> str:
        return "Поворот направо"

    
    def turnLeft(self) -> str:
        return "Поворот налево"


    def __str__(self) -> str:
        return f"Автомобиль: {self.marka}. Водитель: {self.driver}. Мотор: {self.engine}"


@dataclass
class Lorry(Car):
    carrying: float

    def __str__(self) -> str:
        return super().__str__() + f"Грузоподъемность {self.carrying}"


@dataclass
class SportCar(Car):
    speed: float

    def __str__(self) -> str:
        return super().__str__() + f"Скорость {self.speed}"
