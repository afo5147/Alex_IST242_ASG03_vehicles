'''
This file will be specifically for the sedan class of vehicles in the garage.
'''

from vehicle import Vehicle
from manufacturer import Manufacturer 
from auto_model import AutoModel

class Sedan(Vehicle):
    '''
    This represents a sedan vehicle.
    '''

    # constructor
    def __init__(self,
                 manufacturer: Manufacturer,
                 model: AutoModel,
                 mpg: float):
        super().__init__(manufacturer, model, mpg)

    # Specify the abstract method
    def num_of_wheels(self) -> int:
        return 4
    
    # Print Sedan information
    def __str__(self) -> str:
        return (
            f"({self.manufacturer}) ({self.model}), mpg: {self._mpg:.2f}"
        )