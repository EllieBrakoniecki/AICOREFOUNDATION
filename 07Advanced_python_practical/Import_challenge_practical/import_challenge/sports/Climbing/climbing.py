#%%

class Sport:
    def __init__(self, name):
        self.name = name
        print(name)

    def equipment(self):
        if self.name == "climbing":
            self.equipment = ["harness", "helmet", "shoes"]
            print(self.equipment)
        elif self.name == "skiing":
            self.equipment = ["skis", "helmet", "gloves"]
            print(self.equipment)
        else:
            print("Equipment not listed")
    
climber1 = Sport("climbing")
equipment_climber1 = climber1.equipment()

skiier1 = Sport("skiing")
equipment_skiier1 = skiier1.equipment()

swimmer1 = Sport("swimming")
equipment_swimmer1 = swimmer1.equipment()
# %%
