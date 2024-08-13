# taxi_simulator.py
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

def print_taxis(taxis):
    """Print the available taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    bill = 0

    while True:
        print("Let's drive!")
        print("q)uit, c)hoose taxi, d)rive")
        option = input(">>> ").strip().lower()

        if option == 'q':
            print(f"Total trip cost: ${bill:.2f}")
            print("Taxis are now:")
            print_taxis(taxis)
            break

        elif option == 'c':
            print("Taxis available:")
            print_taxis(taxis)
            try:
                taxi_choice = int(input("Choose taxi: ").strip())
                if 0 <= taxi_choice < len(taxis):
                    current_taxi = taxis[taxi_choice]
                else:
                    print("Invalid taxi choice")
            except ValueError:
                print("Invalid option")

        elif option == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                try:
                    distance = float(input("Drive how far? ").strip())
                    fare = current_taxi.drive(distance)
                    bill += current_taxi.get_fare()
                    print(f"Your {current_taxi.name} trip cost you ${fare:.2f}")
                except ValueError:
                    print("Invalid distance")
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
