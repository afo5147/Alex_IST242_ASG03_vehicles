'''
This file will be specifically for the truck class of vehicles in the garage.
'''

from vehicle import Vehicle
from manufacturer import Manufacturer
from auto_model import AutoModel

class Truck(Vehicle):
    '''
    This represents a truck which can either be a dually or not.
    '''

    # constructor
    def __init__(self, manufacturer: Manufacturer, model: AutoModel, mpg: float, is_dually: bool = False):
                super().__init__(manufacturer, model, mpg)
                self._is_dually = is_dually
    @property
    def is_dually(self) -> bool:
        return self._is_dually

    # Specify the abstract method
    def num_of_wheels(self) -> int:
        return 6 if self._is_dually else 4
    
    # Print Truck information
    def __str__(self) -> str:
        return (
            f"({self.manufacturer}) ({self.model}), mpg: {self._mpg:.2f}"
            f" is Dually truck: {self._is_dually}"
        )