#%%
import sys
print(sys.path)
sys.path.append("/Users/eleanorbrakoniecki/scratch/AICOREFOUNDATION/07OOP_practicals/Import_challenge_practical/import_challenge/sports")
print(sys.path)

#from Climbing.climbing import Sport
import Climbing.climbing

skiier1 = Climbing.climbing.Sport("skiing")
skiier1.equipment()
skiier2 = Sport("volleyball")
skiier2.equipment()

# %%
Aicore/advanced_python_practical/import_challenge/sports/climbing