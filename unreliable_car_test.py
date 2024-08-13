# unreliable_car_test.py
from unreliable_car import UnreliableCar

def main():
    unreliable_car = UnreliableCar("Unreliable Car", 100, 50)
    print(unreliable_car)
    distance_driven = unreliable_car.drive(30)
    print(f"Distance driven: {distance_driven}")
    print(unreliable_car)

if __name__ == "__main__":
    main()
