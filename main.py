'''
This file will be for the main script for this program.
'''
from manufacturer import Manufacturer

def main():
    m = Manufacturer("Ford", "USA")
    print(m.get_name)
    print(m.get_country)

    pass 

#this will exectute the file when it is ran 
if __name__ == "__main__":
    main()