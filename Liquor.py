from Additive import Additive

class Liquor:
    def __init__(self):
        self.calorieCount = 50 # Default is Vodka
        self.drinkName = "Vodka"
        self.additiveList = []

    def checkCalories(self):
        sum = self.calorieCount

        for additive in self.additiveList:
            sum += additive.calories

        return sum
    
    def changeDrink(self, liquorName, drinkDict):
        self.calorieCount = drinkDict[liquorName]
        self.drinkName = liquorName
    
    def removeFromDrink(self, additiveName):
        for additive in self.additiveList:
            if additiveName == additive.name:
                self.additiveList.pop(self.additiveList.index(additive))
                print("Removed " + additiveName + " from your drink!")
                return 1
            
        print("No " + additiveName + " was in your drink. Maybe you spelled it wrong?")
        return -1

    def addToDrink(self, additiveName, calorieDict):
        additive = Additive()
        additive.editAdditive(calorieDict[additiveName], additiveName)
        self.additiveList.append(additive)

        print("Added " + additiveName + " to your drink!")
        return 1

        