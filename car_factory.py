from car import Car, SpeedyCar, WeakCar, CarWanted

class CarFactory:
    @staticmethod
    def create_car(type, *args, **kwargs):
        match type:
            case 'car':
                return Car(*args, **kwargs)
            case 'speedycar':
                return SpeedyCar(*args, **kwargs)
            case 'weaker':
                return WeakCar(*args, **kwargs)
            case 'carwanted':
                return CarWanted(*args, **kwargs)
            case '_':
                print('....')


if __name__ == "__main__":
    car_factory = CarFactory()
    t = car_factory.create_car('weaker', 3.2)
    print(t.show_full_info())


