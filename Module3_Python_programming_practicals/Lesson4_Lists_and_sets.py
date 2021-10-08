#%%
# Username list

username_list = ["ellieb", "sarac", "joannar"]
print(type(username_list))
print(len(username_list))
print(type(username_list[0]))
print(len(username_list[-1]))

# %%
# List elements

list1 = ["ellie", 1.65, ["Croatia", "Italy"], 19.7, True]
list2 = [0] * 10
list3 = [list1, list2]
list4 = []
list4.append(list3[0][3])
list4.append(list3[1][3])
print(list4)


# %%
#Car number plate year

number_plate_list = ["G06 WTR", "WL11 WFL", "QW68 PQR"]
year_of_registration = [item[-6 : -4] for item in number_plate_list]
print(year_of_registration)
type(year_of_registration[0])
len(year_of_registration)

year_of_registration = [int(year_of_registration[i]) for i in range(len(year_of_registration))]
print(year_of_registration)
type(year_of_registration[0])
# %%
# Name character intersection
# Find the characters which appear in every name

names = ("Joe", "Jane", "Jake", "Jenny", "Juliet")

list_of_sets = [set(item) for item in names]
print(list_of_sets)

# characters_in_all_names = list_of_sets[0].intersection(list_of_sets[1], list_of_sets[2], list_of_sets[3])

# generalized version: 
characters_in_all_names = list_of_sets[0]
for i in range(1,len(list_of_sets)):
    characters_in_all_names = characters_in_all_names.intersection(list_of_sets[i])    
print(characters_in_all_names)

# %%
# Multiplying list elements

list1 = [0] * 10
print(list1)
set1 = set(list1)
print(set1)
print(len(set1))

# %%
