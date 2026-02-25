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

    # construcotor
    def __init__(self,
                 manufacturer: Manufacturer,
                 model: AutoModel,
                 mpg: float):
        super().__init__(manufacturer, model, mpg)