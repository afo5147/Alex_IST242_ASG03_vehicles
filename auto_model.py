'''
This file will be for model of the vehicles in the garage.
'''

class AutoModel:
    '''
    This is for the medel of the car along with it's prodution year.
    '''

    # constructor
    def __init__(self, name: str, in_production: bool, years: list):
        if not years:
            raise ValueError("The years list cannot be empty.")
        self._name = name
        self._in_production = in_production
        self._years = list(years) 

    # Properties below

    @property
    def get_name(self) -> str:
        return self._name

    @property
    def get_in_production(self) -> bool:
        return self._in_production

    @property
    def get_years(self) -> list[int]:
        return list(self._years) #this is going to return a copy of the lsit.
    
    @property
    def get_first_year(self) -> int:
        return self._years[0] #This is going to return the oldest production year.
    
    def __str__(self) -> str:
        return (
            f"{self._name} in production = {self._in_production}"
            f" release year = {self._years}"
        )