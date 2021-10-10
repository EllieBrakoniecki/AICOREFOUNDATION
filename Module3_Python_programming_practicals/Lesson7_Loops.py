#%% 
#Counting even and odd numbers using a for loop
def count_even_and_odd(i = 1, j = 100):
    even, odd = 0, 0
    for n in range(i, j + 1):
        if n % 2 == 0:
            even += 1
        else:
            odd +=1
    print (f"There are {even} even numbers between {i} and {j}")
    print (f"There are {odd} odd numbers between {i} and {j}")

count_even_and_odd()
count_even_and_odd(33, 77)


# %%
#check if a string is a palindrome - method 1
def is_palindrome1(string):
    n = len(string) // 2
    k = 1
    for i in range(n):
        if string[i] != string[i - k]:
            print(f"{string} is not a palindrome")
            return False 
        else:
            k+=2
    print(f"{string} is a palindrome")
    return True


print(is_palindrome1("racecar"))
print(is_palindrome1("1122334455675544332211"))
print(is_palindrome1("elephant"))
print(is_palindrome1("ABBA"))


#%%
# palindrome - method 2, more efficient

def is_palindrome2(string): 
    reverse_string = string[::-1]
    if string == reverse_string:
        print(f"{string} is a palindrome")
        return True
    else:
        print(f"{string} is not a palindrome")
        return False
        
print(is_palindrome2("racecar"))
print(is_palindrome2("1122334455675544332211"))
print(is_palindrome2("elephant"))
print(is_palindrome2("ABBA"))

# %%
# Create a list comprehension that squares even arguments, and adds 1 to and squares odd arguments

my_list = [34,52,71,39,22,73,92]
even_and_odd = [i ** 2 if i % 2 == 0 else (i + 1) ** 2 for i in my_list]
print(even_and_odd)

# %%
# Budget calculator

order_list = [("tom", 0.87, 4), ("sug", 1.09, 3), ("ws", 0.29, 4), ("juc", 1.89, 1), ("fo", 1.29, 2)]
names = {"tom":"Tomatoes", "sug":"Sugar", "ws":"Washing Sponges", "juc":"Juice", "fo":"Foil"}

order_value = [round(i[1] * i[2], 2) for i in order_list]
quantity_list = [i[2] for i in order_list]
name_list = [i[0] for i in order_list]

budget = 10.00
running_total = 0
#formatted_running_total = "{:.2f}".format(running_total)
receipt = []
print(f"Current total: £{running_total}") # format here? 
for i in range(len(order_list)):
    running_total += order_value[i]
    key = name_list[i]
    full_name = names[key]
    print(f"Adding {quantity_list[i]} {full_name}")
    if order_value[i] > budget:
        print("budget exceeded")
        break
    receipt.append(running_total) # format here? 
    print(f"Current total: £{running_total}") # and here? 
    budget -= order_value[i]

print(receipt)

# %%
# Dictionaries & list comprehensions

ellie_skills = {"Ellie" : ["C++", "Data"]}
fred_skills = {"Fred" : ["OOP", "SQL"]}
mylist = [ellie_skills, fred_skills]

last_letter_first_skill_last_dict = mylist[-1]["Fred"][0][-1]
print(last_letter_first_skill_last_dict)

length_of_names = [len(key) for dict_item in mylist for key in dict_item]
print(length_of_names)
print(sum(length_of_names))

# %%
# Filter shop_dict using list comprehension to find only items with values of over 1.00
# Assign them to a list called filtered_shop by their full names, not their codes, using names_dict.

shop_dict = {"tom":0.87, "sug":1.09, "ws":0.29, "cc":1.89, "ccz":1.29}
names_dict = {"tom":"Tomatoes", "sug":"Sugar", "ws":"Washing Sponges", "cc":"Coca-Cola", "ccz":"Coca-Cola Zero"}

items_with_value_over_1 = [key for key in shop_dict if shop_dict[key] > 1.00]
print(items_with_value_over_1)
filtered_shop = [names_dict[key] for key in items_with_value_over_1]
print(filtered_shop)

# %%
# Shape Maker

def shape_maker(n):
    j = 0
    for i in range(1, 2 * n):
        if i < n:
            print("*" * i)
        else:
            print("*" * (i - j))
            j += 2

shape_maker(5)
shape_maker(20)

#%%
# Write a program to check whether each number from 10 to 50 is prime

def primes_between_two_numbers(number1, number2):
    if number1 <= 2:
        list_of_primes = [2]
    else:
        list_of_primes = []
    for i in range(number1, number2 + 1):
        for j in range(2, i):
            if (i % j) == 0:
                print(f"{i} is not a prime number as {j} is a factor of {i}")
                break
            elif j == i - 1:
                list_of_primes.append(i)
    return list_of_primes

primes_between_two_numbers(1, 5)

# %%
# while loop version of program above
def primes_between_two_numbers(number1, number2): 
    if number1 <= 2:
        list_of_primes = [2]
        number1 = 3
    else:
        list_of_primes = []
    
    for i in range(number1, number2 + 1):

        j = 2
        while (i % j) != 0 and j < i:
            if j == i - 1:
                list_of_primes.append(i)
            j += 1
    return(list_of_primes)

primes_between_two_numbers(1, 50)
# %%
