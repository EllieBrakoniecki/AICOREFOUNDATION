#%% 
# XOR gate

def XORgate(bool1, bool2):
    return True if (not(bool1 and bool2) and (bool1 or bool2)) else False

print(XORgate(0,0))
print(XORgate(1,0))
print(XORgate(0,1))
print(XORgate(1,1))

# %%
# Comparing integers

x = 10
n = int(input("Enter a number"))
if (n>x):
    print(f"{n} is greater than 10")
else:
    print(f"{n} is less than or equal to 10")

# %%
# Comparing different data types
print(99 > 5)
print(0 == False)
print(1 == True)
print(6.2 < 7)
print(9 >= 9)
print(False < True)

# %%
# Comparing strings

print('AAA' > 'BBB')
print('AAB' > 'AAA')
print('aaa' > 'AAA')
# %%
