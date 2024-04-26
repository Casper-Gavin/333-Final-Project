from Liquor import Liquor

class Bartender:
    def __init__(self):
        self.drinkQueue = []
        self.calorieCountWhole = 0

    def addDrink(self, newDrinkName, drinkDictionary):
        if len(self.drinkQueue) < 5:
            newDrink = Liquor()
            newDrink.changeDrink(newDrinkName, drinkDictionary)
            self.drinkQueue.append(newDrink)
            print("your order was accepted!")
            return 1
        else:
            print("We are too busy to accept your order!")
            return -1

    def makeDrink(self):
        if len(self.drinkQueue) > 0:
            drink = self.drinkQueue.pop(0)
            print("Your " + drink.drinkName + " is made!")
            return 1
        else:
            print("There are no drinks in the queue")
            return -1
        
    def totalCalories(self):
        total = 0
        for drink in self.drinkQueue:
            total += drink.checkCalories()
        print("Total order calories: " + str(total))
        return total