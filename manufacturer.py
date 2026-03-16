class Manufacturer:
    '''
    This file will be for the manufactuerer of the vehicles in the garage.
    '''

    # constructor - This will pass values and construct an object
    # Private variables have an __ before it and Public variables do not

    def __init__(self, name: str, country: str):
        self._name = name
        self._country = country

    # Properties - This is for the different properties that can be public or private and how it will be presented

    @property
    def get_name(self): # type: () -> str
        return self._name
        
    @property
    def get_country(self):
        return self._country
    
    def __str__(self) -> str:
        return f"{self._name} {self._country}"