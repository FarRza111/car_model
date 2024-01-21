import unittest
from car import Car, CarWanted , WeakCar, SpeedyCar

class TestCar(unittest.TestCase):

    def test_car_creation(self):
        car = CarWanted('Posledniy', 'BMW', 45000, 300)
        self.assertEqual(car.model, 'Posledniy')
        self.assertEqual(car.brand, 'BMW')
        self.assertEqual(car.price,45000)
        self.assertEqual(car.power, 300)

if __name__ == '__main__':
    unittest.main()