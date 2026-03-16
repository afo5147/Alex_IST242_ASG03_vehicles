'''
This file will be for the main script for this program.
'''
from manufacturer import Manufacturer
from auto_model import AutoModel
from sedan import Sedan
from truck import Truck
from garage import Garage

def main():
    # these will be the manufactureres for vehicles in the garage.
    ford = Manufacturer("Ford", "USA")
    honda = Manufacturer("Honda", "Japan")
    bmw = Manufacturer("BMW", "Germany")
    toyota = Manufacturer("Toyota", "Japan")

    # these will be the models for the vehicles in the garage.
    f150_model = AutoModel("F-150", True, list(range(2020, 2023)))
    civic_model = AutoModel("Civic", False, list(range(1996, 1999)))
    m3_model = AutoModel("M3", False, list(range(2015, 2018)))
    tundra_model = AutoModel("Tundra", False, list(range(1987, 1990)))

    # these will be the vehicles in the garage.
    f150 = Truck(ford, f150_model, 20.0)
    civic = Sedan(honda, civic_model, 28.0)
    m3 = Sedan(bmw, m3_model, 30.0)
    tundra = Truck(toyota, tundra_model, 30.0, is_dually=True)

    # this will be the garage to hold the vehicles.
    g = Garage()
    g.add_vehicles(f150)
    g.add_vehicles(civic)
    g.add_vehicles(m3)
    g.add_vehicles(tundra)

    print("Before sorting:")
    print(g)
    print()

    g.sort_by_release_year()

    print("After sorting:")
    print(g)

#this will exectute the file when it is ran 
if __name__ == "__main__":
    main()