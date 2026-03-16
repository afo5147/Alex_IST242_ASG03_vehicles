'''
This will be the main file for the garage.
'''
from vehicle import Vehicle

class Garage:
    '''
    This class will be the garage to hold all the vehicles.
    '''

    # constructor
    def __init__(self):
        self._vehicles: list[Vehicle] = []

    @property
    def vehicles(self) -> list[Vehicle]:
        return list(self._vehicles) # This is going to show a copy of the vehicles in the garage.
    
    def add_vehicles(self, vehicle: Vehicle) -> None:
        self._vehicles.append(vehicle) #This is going to be to add a vehicle to the garage.

    def empty_garage(self) -> None:
        self._vehicles.clear() #This is going to be to empty the garage of all vehicles.

    def sort_by_release_year(self) -> None:
        self._vehicles.sort() #This is going to sort the vehicles in the garage by their release year.

    def __str__(self) -> str:
        return "\n".join(str(V) for V in self._vehicles) #This is going to print the vehicles in the garage.