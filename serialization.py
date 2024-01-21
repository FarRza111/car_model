from car_factory import  CarFactory
from car import CarWanted


import json
from car import Car, SpeedyCar, WeakCar, CarWanted

class CarEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (Car, SpeedyCar, WeakCar, CarWanted)):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)

def serialize_car(car):
    return json.dumps(car, cls=CarEncoder)

def deserialize_car(car_json, car_type):
    car_data = json.loads(car_json)
    return CarFactory.create_car(car_type, **car_data)


if __name__ == "__main__":
    car_wanted = CarWanted('Model X', 'Tesla', 50000, 300)
    car_json = serialize_car(car_wanted)
    print(car_json)  # This will print the JSON string representation of the car object

    # Example of Deserializing a Car Object
    # Assuming 'car_json' is the JSON string you got from serialization
    deserialized_car = deserialize_car(car_json, 'carwanted')
    print(deserialized_car.provide_full_details())  # This should show the details of the recreated car object
