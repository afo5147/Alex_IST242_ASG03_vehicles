'''
This file will be for the vehichles in the garage.
'''

from abc import ABC, abstractmethod
# this is only for sorting purposes. -> from functools import total_ordering

from manufacturer import Manufacturer
# from auto_model import AutoModel

class Vehicle(ABC):
    """
    This is the abstract base class (ABC) for all vehicles
    """
    #constructor

    # need to fix the model part once it is done.
    def __init__(self,
                 manufacturer: Manufacturer,
                 #model: Automodel,
                 mpg: float):
        self.__manufacturer = manufacturer
        #self.__model = model
        self.__mpg = mpg

    @property
    def manufacturer(self) -> Manufacturer:
        return self.__manufacturer
    
    @property
    def model(self): # -> AutoModel:
        return self.__model
    
    @property
    def mpg(self): # -> float:
        return self.__mpg
    

