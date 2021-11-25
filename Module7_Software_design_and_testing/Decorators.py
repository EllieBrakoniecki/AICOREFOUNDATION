#%%
from typing import ClassVar


class Dummy:
    def __init__(self):
        print('I am running the constructor')
    
    @classmethod
    def dummy_class_method(cls):
        print('I am running the class method')

dummy = Dummy()
dummy.dummy_class_method()

#%%
class Celsius:
    """ 
    This is a Temperature Class 

    Inside this class, you can: 
    - Set a Temperature in either Degrees Celsius or Farenheit 
    - Convert a Temperature between Degrees Celsius or Farenheit 
    - Set a Temperatue to 0 
    - Check if a Temperature is valid between -273 and 3000 
    """
    def __init__(self, temperature=0 : float)->None:
        print("creating an instance using initialiser")
        self.temperature = temperature

    @classmethod
    def standard(cls):
        """

        Function to set a temperature to zero using a new instance of the class 
    
        returns: Celsius object with temperature 0 degrees Celsius 

        """
        print("creating an instance using a class method")
        return cls(0)

    @classmethod
    def initialise_with_fahrenheit(cls, value : float ) -> Celsius:
        """Initialise Celsius class given a temperature in Fahrenheit

        Parameters
        ----------
        value : float
            The temperature in fahrenheit

        Returns
        -------
        Celsius object 
        """
        return cls(cls.convert_to_celsius(value))

    @property
    def temperature(self):
        print("Calling getter function..")
        return self.__temperature
    
    @temperature.setter
    def temperature(self, value):  
        print("Calling setter function")          
        self.__temperature = value

    def convert_to_fahrenheit(self):
        """Converts the value of the temperature from celsius to fahrenheit

        Returns
        -------
        float 
            temperature in fahrenheit     
        """
        fahrenheit = ((self.temperature * 1.8) + 32)
        return fahrenheit

    @staticmethod
    def convert_to_celsius(value):
        """Converts the value of the temperature from fahrenheit to celsius 

        Parameters
        ---------
        value : float
        Returns
        -------
        float 
            temperature in celsius  
        """
        return (value - 32)/1.8

    @staticmethod
        """Checks if the temperature is a valid value  

        Parameters
        ---------
        value : float
        Returns
        -------
        bool   
        """
    def is_temperature_valid(value):
        return True if -273.15 <= value <= 3000 else False

#%%

temp = Celsius(37)

temp.convert_to_fahrenheit()
# temp1 = Celsius.standard()
# temp1.convert_to_fahrenheit()
# temp.is_temperature_valid(-300)
# temp2 = Celsius.initialise_with_fahrenheit(100)



#%%
temp = Celsius(37)
temp.__dict__.items()
temp.convert_to_fahrenheit()
temp.get_temperature()
temp.set_temperature(40)
temp.get_temperature()
temp.convert_to_fahrenheit()
#%%

# %%

#%%
from dataclasses import dataclass
@dataclass
class Celsius:
    temperature : float

    @classmethod
    def standard(cls):
        print("creating an instance using a class method")
        return cls(0)

    @classmethod
    def initialise_with_fahrenheit(cls, value):
        return cls(cls.convert_to_celsius(value))

    @property
    def temperature(self):
        print("Calling getter function..")
        return self.__temperature
    
    @temperature.setter
    def temperature(self, value):  
        print("Calling setter function")          
        self.__temperature = value

    def convert_to_fahrenheit(self):
        fahrenheit = ((self.temperature * 1.8) + 32)
        return fahrenheit

    @staticmethod
    def convert_to_celsius(value):
        return (value - 32)/1.8

    @staticmethod
    def is_temperature_valid(value):
        return True if -273.15 <= value <= 3000 else False
#%%
temp3 = Celsius(300)

#%%
@dataclass(order=True)
class Date:
    year: int
    month: int
    day: int # First positional argument
  

date = Date(2,11,2021)
# %%
