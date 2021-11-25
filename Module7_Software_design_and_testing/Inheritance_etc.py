
#%%
import datetime as dt

class Greeter():
    def __init__(self):
        pass
        
    def greet(self, store):
        print(f" Good morning, welcome to {store}! \n How's your {day()} {part_of_day()} going?")

def day():
    days_of_the_week = {1 : "Monday", 2 : "Tuesday", 3 : "Wednesday", 4 : "Thursday", 5 : "Friday", 6 : "Saturday", 7 : "Sunday"}
    return days_of_the_week[dt.date.today().day]
    
def part_of_day():
    hour_now = dt.time(dt.datetime.now().hour).hour
    return "morning" if hour_now < 12 else "afternoon" 

greeter = Greeter()
greeter.greet("Asda")  
#%%
import datetime as dt

dt.date.today().day
days_of_the_week = {0 : "Monday", 1 : "Tuesday", 2 : "Wednesday", 3 : "Thursday", 4 : "Friday", 5 : "Saturday", 6 : "Sunday"}
days_of_the_week[dt.date.today().day]
dt.date.today().timetuple()

now = dt.datetime.now()
time_now = dt.time(now.hour, now.minute)
hour_now = time_now.hour
mins_now = time_now.minute

#%%
class SpeakMixin:
    def speak(self):
        name = self.__class__.__name__.lower()
        print(f'The {name} says: "hello... I mean... woof!"')


class RollOverMixin:
    def roll_over(self):
        print('Look at me, I am rolling!')

class Dog(RollOverMixin, SpeakMixin):
    pass

class Cat(SpeakMixin):
    pass

jake = Dog()
jake.speak()
jake.roll_over()
# %%

# Mixin class for private methods
# Create a mixin class named AsDictMixin
# This class will be just inherited, so don't use a constructor for it
# You just need to define the following method: to_dict(self) which returns a dict 
# representation of the object that inherits this mixin class.
# You might want to use the __dict__ method, which returns a dictionary 
# representation of an object.
# The class should look like this:

class AsDictionaryMixin:
    def to_dict(self):
        temp_dict = {}
        for key, value in self.__dict__.items():
            if not self._is_internal(key):
                temp_dict[key] = self._represent(value)
        return temp_dict
        

    def _represent(self, value):
        if isinstance(value, object):
            if hasattr(value, 'to_dict'):
                return value.to_dict()
            else:
                return str(value)
        else:
            return value

    def _is_internal(self, prop):
        return prop.startswith('_')


class Person(AsDictionaryMixin):
    def __init__(self, name, address, salary):
        self.name = name
        self.address = address
        self._salary = salary


#%%
ivan = Person('Ivan', 'London', '100000000')
ivan.to_dict()




# %%
