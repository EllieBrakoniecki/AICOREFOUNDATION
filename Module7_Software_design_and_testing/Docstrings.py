

#%%
def say_hi(name):
    # This function says hi to the user
    print(f"Hello {name}")

help(say_hi)
#%%

def say_hi(name):
    """ This function says hi to the user """
    print(f"Hello {name}")

help(say_hi)
# %%
# One-line summary
# An empty line
# An elaborated description
def say_hi(name):
    """
    This function says hi to the user

    The purpose of this function is to demonstrate how to document
    a function following the convention established in the PEP257.
    It actually does not do much, and I am writing this to fill
    the docstring... Lorem ipsum dolor sit amet.
    """
    print("Hello {}".format(name))

help(say_hi)

#%%
# Docstring for classes
# The docstring should be the first thing in the class definition.
# Each method should have a docstring. This is excluded if the method is private.
# There is no clear consensus on whether the __init__ method should have a docstring. 
# However, many frameworks refer to the class docstring when defining the __init__ method docstring.
class Date:
    '''
    This class is used to represent a date.

    Attributes:
        year (int): The year of the date.
        month (int): The month of the date.
        day (int): The day of the date.
    '''
    def __init__(self, year: int, month: int, day: int):
        '''
        See help(Date) for accurate signature
        '''
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        '''
        This function is used to return the string representation of the date.

        Returns:
            str: The string representation of the date.
        '''
        return "{0}-{1}-{2}".format(self.year, self.month, self.day)

    def __repr__(self):
        '''
        This function is used to return the string representation of the date.

        Returns:
            str: The string representation of the date.
        '''
        return "{0}-{1}-{2}".format(self.year, self.month, self.day)

    def __eq__(self, other):
        '''
        This function is used to compare the date with other date.

        Args:
            other (Date): The other date to be compared with.

        Returns:
            bool: True if the date is equal to the other date, False otherwise.
        '''
        return self.year == other.year and self.month == other.month and \
            self.day == other.day

    def __lt__(self, other):
        '''
        This function is used to compare the date with other date.

        Args:
            other (Date): The other date to be compared with.

        Returns:
            bool: True if the date is less than the other date, False otherwise.
        '''
        if self.year < other.year:
            return True
        elif self.year == other.year:
            if self.month < other.month:
                return True
            elif self.month == other.month:
                if self.day < other.day:
                    return True
        return False
        
    
    @staticmethod
    def is_date_valid(year, month, day):
        '''
        This function is used to check if the date is valid.

        Args:
            year (int): The year of the date.
            month (int): The month of the date.
            day (int): The day of the date.

        Returns:
            bool: True if the date is valid, False otherwise.
        '''
        return year >= 0 and month >= 1 and month <= 12 and \
            day >= 1 and day <= 31

    @classmethod
    def from_string(cls, date_as_string):
        '''
        This function is used to create a date from a string.

        Args:
            date_as_string (str): The string representation of the date.

        Returns:
            Date: The date created from the string.
        '''
        year, month, day = map(int, date_as_string.split('-'))
        return cls(year, month, day)

help(Date)
# %%
import typing
import Date
help(Date)
# %%
#%% Typing

import requests
from bs4 import BeautifulSoup
def get_html(url: str) -> BeautifulSoup:
    """
    Get the HTML of a URL
    
    Parameters
    ----------
    url : str
        The URL to get the HTML of
    
    Returns
    -------
    str
        The HTML of the URL
    """
    r = requests.get(url)
    if r.status_code == 200:
        return BeautifulSoup(r.text, 'html.parser')
    else:
        return None