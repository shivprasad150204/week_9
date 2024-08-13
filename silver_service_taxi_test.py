# silver_service_taxi_test.py
from silver_service_taxi import SilverServiceTaxi

def main():
    silver_taxi = SilverServiceTaxi("Limo", 100, 2)
    print(silver_taxi)
    silver_taxi.drive(18)
    print(f"Fare: ${silver_taxi.get_fare():.2f}")
    silver_taxi.start_fare()
    silver_taxi.drive(100)
    print(silver_taxi)
    print(f"Fare: ${silver_taxi.get_fare():.2f}")

if __name__ == "__main__":
    main()
