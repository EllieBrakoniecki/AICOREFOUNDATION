#%%
def greeting():
    print("Hello! Pleased to meet you!")

#when the python interpreter reads the file the name is set to "main"
#if the module is being run or as the module's name if it's being imported. 
#Hence this will not run if the module is being imported
if __name__ == "__main__":
    greeting()
# %%
