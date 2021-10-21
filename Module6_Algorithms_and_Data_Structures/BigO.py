

# %%
def get_number_with_highest_count(counts: dict) -> int:
    max_count = 0
    for number, count in counts.items():
        if count > max_count:
            max_count = count
            number_with_highest_count = number
    return number_with_highest_count


def most_frequent(numbers: list) -> int:
    counts = {}
    for number in numbers:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1

    return get_number_with_highest_count(counts)

#%%
# Default dictionaries and counter
from collections import defaultdict
from collections import Counter

def get_number_with_highest_count(counts: dict) -> int:
    max_count = 0
    for number, count in counts.items():
        if count > max_count:
            max_count = count
            number_with_highest_count = number
    return number_with_highest_count

my_dict = { 1 : 2, 2 : 3, 3 : 4}

def most_frequent1(numbers: list) -> int:
    counts = defaultdict(int) # <-- If the key doesn't exist, defaultdict will create a new key whose value is an integera
    for number in numbers:
        counts[number] += 1

    return get_number_with_highest_count(counts)

def most_frequent2(numbers):
    counts = Counter(numbers)
    print(counts)
    return get_number_with_highest_count(counts)



my_list=[1,1,2,2,2,3,3,3,3]
print(most_frequent1(my_list))
most_frequent2(my_list)

# %%
# processing a text file version 1 
from collections import defaultdict

counts = defaultdict(int)
with open('colours.txt') as text:
    words = text.read().split()   
    even_words = words[1::2]
    for word in even_words:
        counts[word] +=1
print(counts)
# %%
# Processing a text file with a O(1) space complexity
from collections import defaultdict
def my_gen(filename, dict_of_counts):
    with open(filename) as text:
        for j, line in enumerate(text):
            colour = line.split()[1]
            dict_of_counts[colour] +=1
            yield dict_of_counts


filename = 'colours.txt'
counts = defaultdict(int)
gen = my_gen(filename, counts)
# %%
next(gen)
# %%
sort_dict = sorted(counts.items(), key=lambda x:x[1], reverse=True)
ls = [(key , value) for key, value in sort_dict]

# %%
