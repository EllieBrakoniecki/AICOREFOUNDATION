#%%
# Range checker 
def in_range(lowerb, upperb, number):
    if lowerb <= number <= upperb:
        print(f"{number} is between {lowerb} and {upperb}")
    else:
        print(f"{number} is NOT between {lowerb} and {upperb}.")

l = float(input('Enter a lower bound'))
u = float(input('Enter an upper bound'))
x = float(input('Enter a number'))

in_range(l,u,x)
# %%
# Default arguments

def print_attributes(clothing_dictionary, attributes_to_print=all):
    if attributes_to_print == all:
        for key, value in clothing_dictionary.items():
            print(key, ":", value)
    else: 
        for key in attributes_to_print:
            if key not in clothing_dictionary:
                print(f"{key} key not found")
            else: 
                print(key, ":", clothing_dictionary[key])

clothing_attributes = {"Size" : 10, "Type" : "T shirt", "Colour" : "Blue"}
attribute_list = ["Size", "Colour"]
print_attributes(clothing_attributes,attribute_list)
print_attributes(clothing_attributes)
attribute_list = ["Material", "Size"]
print_attributes(clothing_attributes, attribute_list)

# %%
#Profile checker

# Note: could use string method isalpha() for quicker check!
def name_validation(name): 
    banned_character_set = set(["!", "@", "£", "$", "%", "^", "&", "&", "*", "(", ")"])
    name_as_set = set(name)
    intersection_name_and_banned_chars = name_as_set.intersection(banned_character_set)
    if len(intersection_name_and_banned_chars):
        for item in intersection_name_and_banned_chars:
            print(f"{item} is not allowed")
        return False
    return True

def age_validation(age):
    if age <=12:
        print("You must be older than 12 to create a profile")
        return False
    return True

def email_validation(email):
    if "@" not in email:
        print("Invalid email address")
        return False
    return True
 
def profile_validation(name, age, email):
    is_name_valid = name_validation(name)
    is_age_valid = age_validation(age)
    is_email_valid = email_validation(email)
    if not (is_name_valid and is_age_valid and is_email_valid):
        print("Invalid details supplied to create profile. Please edit and try again")
    else:
        print("Your profile has been created successfully")

profile_validation("Ellie*%", 8, "elliebrakoniecki.com")
profile_validation("Ellie", 13, "eleanor@brakoniecki.com")

# %%
# Recursive factorial function

def recursive_factorial(n):
    if isinstance(n, float) or n < 0:
        return print("n must be a non-negative integer")
    elif n <= 1:
        return n
    else:
        return n * recursive_factorial(n-1)
    
recursive_factorial(10)

# %%
#  Recursive fibonacci function

def recursive_fibonacci(n):
    if isinstance(n, float) or n < 0:
        return print("n must be a non-negative integer")
    elif n <= 1:
        return n
    else:
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

recursive_fibonacci(8)

# %%
# Fibonacci function using a for loop

def fibonacci_list(n=100): #print the first n fibonacci numbers using a for loop
    list_of_fibonacci =[]
    for i in range(0, n+1):
        if i <= 1:
            list_of_fibonacci.append(i)
        else:
            nth_term = list_of_fibonacci[i-1] + list_of_fibonacci[i-2]
            list_of_fibonacci.append(nth_term)
    return list_of_fibonacci

print(fibonacci_list(10))

def is_multiple_of_7(n):
    return True if n % 7 == 0 else False

def is_number_greater_or_equal_100_or_less_than_50(n):
    return False if 50 <= n < 100 else True

fibonacci_list_to_100 = fibonacci_list()
fibonacci_list_and_multiple_of_7 = [x for x in fibonacci_list_to_100 if is_multiple_of_7(x)]
print(fibonacci_list_and_multiple_of_7)
fibonacci_and_not_in_range_50_to_100 = [x for x in fibonacci_list_to_100 if is_number_greater_or_equal_100_or_less_than_50(x)]
print(fibonacci_and_not_in_range_50_to_100)


# %%
# checking if number < 50 or >= 100 inside the for loop of the previous function

def fibonacci_list(n=100): #print the first n fibonacci numbers using a for loop
    list_of_fibonacci =[]
    for i in range(0, n+1):
        if i <= 1:
            list_of_fibonacci.append(i)
        else:
            nth_term = list_of_fibonacci[i-1] + list_of_fibonacci[i-2]
            if nth_term < 50:
                print(f"{nth_term} is less than 50")
            elif nth_term >= 100:
                print(f"{nth_term} is greater than or equal to 100")
            list_of_fibonacci.append(nth_term)
    return list_of_fibonacci

print(fibonacci_list(20))

# %%
