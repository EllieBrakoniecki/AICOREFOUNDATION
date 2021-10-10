#%% 
# Create a cylinder class 

import math

class Cylinder:
    def __init__(self, height, radius=1):
        self.height = height
        self.radius = radius
        self.surface_area = 0
        self.volume = 0

    def get_surface_area(self):
        self.surface_area = 2 * math.pi * self.radius * (self.height + self.radius)
        return round(self.surface_area,2)

    def get_volume(self):
        self.volume = math.pi * self.height * self.radius ** 2 
        return round(self.volume,2 )
    
cylinder1 = Cylinder(20,4)
print(cylinder1.get_surface_area())
print(cylinder1.get_volume())

#%%
#Create a Car Class
class Car:
    def __init__(self, model, year=2021):
        self.model = model
        self.year = year
        self.miles_driven = 0

    def drive(self):
        self.miles_driven +=1
        print("vroom")

    def info(self):
        print(f"Number of miles driven: {self.miles_driven}")
        print(f"Model name: {self.model}")
        print(f"Year: {self.year}")

mycar = Car("Tesla", 2020)
mycar.drive()
mycar.info()
mycar.drive()
mycar.info()

#%%
#Create a Vector class which uses some Magic Methods
import math

class Vector:
    def __init__(self, vector_list=[]):
        self.vector_list = vector_list
        self.result = []
        self.vector_length = len(self.vector_list)
    
    def __repr__(self):
        return str(self.vector_list)

    def __add__(self, other):
        self.result = [self.vector_list[i] + other.vector_list[i] for i in range(self.vector_length)]
        return Vector(self.result)

    def __getitem__(self, index):
        return self.vector_list[index]

    def _magnitude(self): # private function
        temp = 0
        for i in range(self.vector_length):
            temp += self.vector_list[i] ** 2
        return math.sqrt(temp)

    def is_greater_than(self,other): #check if this instance of the vector is greater than the vector passed in as argument
        if self._magnitude() > other._magnitude():
            return True
        else: 
            return False
            
l = [2,3,4]
vector1 = Vector(l)
print(vector1)

k = [20] * 3
vector2 = Vector(k)
print(vector2)

j = [100,100,0,0]
vector3 = Vector(j)

list1 = vector1 + vector2
list2 = vector2 + vector3

print(list1)
print(list2)

vector3[1]

print(vector3._magnitude())
vector3.is_greater_than(vector2)
vector2.is_greater_than(vector3)
    

# %%
# Hangman

class Hangman: 
    def __init__(self, secret_word):
        self.secret_word = secret_word
        self.letters_guessed = [_] * len(self.secret_word)
        self.hangman_parts_left_to_draw = 6
    
    def guess_letter(self, letter):
        correct_guess_this_turn = 0
        for i in range(len(self.secret_word)):
            if letter == self.secret_word[i]:
                correct_guess_this_turn +=1
                self.letters_guessed[i] = letter
        if correct_guess_this_turn > 0:
            return True
        else:
            self.hangman_parts_left_to_draw -=1
            return False

    def guess_word(self, word):
        if word == self.secret_word:
            return True
        return False
            

    def play_game(self):
        guess = input(f" Welcome to Hangman! The word to guess is a {len(self.secret_word)} letter word {self.letters_guessed}. Enter your first guess for a letter")
        while self.hangman_parts_left_to_draw > 0:
            if (self.guess_letter(guess)):
                guess_word = input(f"You have guessed correctly and the word is now {self.letters_guessed}. Guess the word.")
                if self.guess_word(guess_word):
                    print(f"You have won, well done! The word was {self.secret_word}")
                    return
            if self.hangman_parts_left_to_draw == 0:
                return print(f"You have lost:( The word was {self.secret_word}")
            guess = input(f"You have guessed incorrectly. Guess another letter {self.letters_guessed}")
          

hangman = Hangman("elephant")
hangman.play_game()


# %%
# Person Class

import datetime

class Person:
    def __init__(self, name, date_of_birth, friends=[]):
        self.name = name
        self.friends = friends
        try:
            datetime.datetime.strptime(date_of_birth, "%Y-%m-%d")
            self.date_of_birth = date_of_birth
        except ValueError: 
            print("This is an incorrect date of birth format. It should be YYYY-MM-DD")

    def __repr__(self):
        return str([self.name, self.date_of_birth, len(self.friends)])

    def __gt__(self, other):
        return True if self.date_of_birth < other.date_of_birth else False
    
    def add_friend(self, other):
    #    assert isinstance(other, Person)
        if not isinstance(other, Person):
            raise TypeError("Object of type Person expected")
        self.friends.append(other.name)
        other.friends.append(self.name)
        


joe = Person("Joe", "2006-04-04", ["Niall", "Harry"])
jake = Person("Jake", "2009-04-19", ["Nico"])
print(joe)
print(jake)
joe > jake 
joe.add_friend(jake)
print(joe)
print(jake)
#zoe = "Zoe"
#joe.add_friend(zoe) # TypeError raised

# %%
# Shape class

class Shape:
    def __init__(self, num_sides, tesselates=False):
        if num_sides == 0:
            raise ValueError("Number of sides should be greater than 0")
        self.num_sides = num_sides
        self.tesselates = tesselates

    def get_info(self):
        raise NotImplementedError("This function should only be used when inherited")
        return (f"Number of sides : {self.num_sides} , Tesselates : {self.tesselates}")

    def __repr__(self):
        return (self.get_info())

    def __add__(self, other):
        sum_of_sides = self.num_sides + other.num_sides
        return Shape(sum_of_sides, self.tesselates)


class Circle(Shape):
    def __init__(self, num_sides=1):
        super().__init__(num_sides)

    def get_info(self):
        return (f"Number of sides : {self.num_sides} , Tesselates : {self.tesselates}")

circle = Circle(1)
circle.get_info()
print(circle)

class Triangle(Shape):
    def __init__(self, num_sides=3, tesselates=True):
        super().__init__(num_sides, tesselates)

    def get_info(self):
        return (f"Number of sides : {self.num_sides} , Tesselates : {self.tesselates}")

triangle = Triangle()
print(triangle)


class Square(Shape):
    def __init__(self, num_sides=4, tesselates=True):
        super().__init__(num_sides, tesselates)

    def get_info(self):
        return (f"Number of sides : {self.num_sides} , Tesselates : {self.tesselates}")

square = Square()
print(square)

class Pentagon(Shape):
    def __init__(self, num_sides=5):
        super().__init__(num_sides)

    def get_info(self):
        return (f"Number of sides : {self.num_sides} , Tesselates : {self.tesselates}")

pentagon = Pentagon()
print(pentagon)

class Hexagon(Shape):
    def __init__(self, num_sides=6, tesselates=True):
        super().__init__(num_sides, tesselates)

    def get_info(self):
        return (f"Number of sides : {self.num_sides} , Tesselates : {self.tesselates}")

hexagon = Hexagon()
print(hexagon)

class ManySidedPolygon(Shape):
    def __init__(self, num_sides):
        if num_sides > 6:
            super().__init__(num_sides)
        else: 
            raise ValueError("Number of sides should be greater than 6")

    def get_info(self):
        return (f"Number of sides : {self.num_sides} , Tesselates : {self.tesselates}")

octagon = ManySidedPolygon(8)
print(octagon)




# %%
# Hangman

class Hangman: 
    def __init__(self, secret_word):
        self.secret_word = secret_word
        self.letters_guessed = [_] * len(self.secret_word)
        self.hangman_parts_left_to_draw = 6
    
    def guess_letter(self, letter):
        correct_guess_this_turn = 0
        for i in range(len(self.secret_word)):
            if letter == self.secret_word[i]:
                correct_guess_this_turn +=1
                self.letters_guessed[i] = letter
        if correct_guess_this_turn > 0:
            return True
        else:
            self.hangman_parts_left_to_draw -=1
            return False

    def guess_word(self, word):
        if word == self.secret_word:
            return True
        return False
            

    def play_game(self):
        guess = input(f" Welcome to Hangman! The word to guess is a {len(self.secret_word)} letter word {self.letters_guessed}. Enter your first guess for a letter")
        while self.hangman_parts_left_to_draw > 0:
            if (self.guess_letter(guess)):
                guess_word = input(f"You have guessed correctly and the word is now {self.letters_guessed}. Guess the word.")
                if self.guess_word(guess_word):
                    print(f"You have won, well done! The word was {self.secret_word}")
                    return
            if self.hangman_parts_left_to_draw == 0:
                return print(f"You have lost:( The word was {self.secret_word}")
            guess = input(f"You have guessed incorrectly. Guess another letter {self.letters_guessed}")
          

hangman = Hangman("elephant")
hangman.play_game()

# %%
