import unittest
from Additive import Additive
from Liquor import Liquor
from Bartender import Bartender

class TestManager(unittest.TestCase):
    def setUp(self):
        self.additiveData = {"Juice": 20, "Bitters": 60, "Soda Water": 10}
        self.drinkData = {"Vodka": 50, "Beer": 30}

    def testAdditiveClass(self):
        self.assertEqual(Additive.__init__(self), None)

    def testAdditiveEditAdditiveCalories(self):
        self.add = Additive()
        self.add.editAdditive(10, "Bitters")
        self.assertEqual(self.add.calories, 10)

    def testAdditiveEditAdditiveName(self):
        self.add = Additive()
        self.add.editAdditive(10, "Bitters")
        self.assertEqual(self.add.name, "Bitters")

    # Liquor class
    def testLiquorClass(self):
        self.assertEqual(Liquor.__init__(self), None)

    def testLiquorChangeDrink(self):
        self.Liq = Liquor()
        self.Liq.changeDrink("Beer", self.drinkData)
        self.assertEqual(self.Liq.calorieCount, 30)

    # integration test 1
    def testLiquorAddToDrinkRan(self):
        self.Liq = Liquor()
        self.assertEqual(self.Liq.addToDrink("Bitters", self.additiveData), 1)

    # # integration test 2
    def testLiquorAddToDrinkCorrect(self):
        self.Liq = Liquor()
        self.Liq.addToDrink("Bitters", self.additiveData)
        self.assertEqual(self.Liq.additiveList[0].name, "Bitters")

    def testLiquorCheckCalories(self): # liquor has a base calorie amount of 50
        self.Liq = Liquor()
        self.Liq.addToDrink("Bitters", self.additiveData)
        self.Liq.addToDrink("Juice", self.additiveData)
        self.assertEqual(self.Liq.checkCalories(), 130)

    # integration test 3
    def testLiquorRemoveDrink(self):
        self.Liq = Liquor()
        self.Liq.addToDrink("Bitters", self.additiveData)
        self.Liq.addToDrink("Juice", self.additiveData)
        self.Liq.removeFromDrink("Bitters")
        self.assertEqual(len(self.Liq.additiveList), 1)

    # integration test 4
    def testLiquorRemoveDrinkFailed(self):
        self.Liq = Liquor()
        self.Liq.addToDrink("Bitters", self.additiveData)
        self.Liq.addToDrink("Juice", self.additiveData)
        self.Liq.removeFromDrink("Not Bitters")
        self.assertEqual(self.Liq.removeFromDrink("Not Bitters"), -1)

    # integration test 5
    def testLiquorRemoveWithCheckCalories(self):
        self.Liq = Liquor()
        self.Liq.addToDrink("Bitters", self.additiveData)
        self.Liq.addToDrink("Juice", self.additiveData)
        self.Liq.removeFromDrink("Bitters")
        self.assertEqual(self.Liq.checkCalories(), 70)
    
    # Bartender class
    def testBartenderClass(self):
        self.assertEqual(Bartender.__init__(self), None)

    # integration test 6
    def testBartenderAddDrinkSuccess(self):
        self.bar = Bartender()
        self.assertEqual(self.bar.addDrink("Vodka", self.drinkData), 1)

    # integration test 7
    def testBartenderAddDrinkToQueue(self):
        self.bar = Bartender()
        self.bar.addDrink("Vodka", self.drinkData)
        self.bar.addDrink("Vodka", self.drinkData)
        self.assertEqual(len(self.bar.drinkQueue), 2)

    # integration test 8
    def testBartenderAddDrinkFail(self):
        self.bar = Bartender()
        self.bar.addDrink("Vodka", self.drinkData)
        self.bar.addDrink("Vodka", self.drinkData)
        self.bar.addDrink("Vodka", self.drinkData)
        self.bar.addDrink("Vodka", self.drinkData)
        self.bar.addDrink("Vodka", self.drinkData)
        self.assertEqual(self.bar.addDrink("Vodka", self.drinkData), -1)

    # integration test 9
    def testBartenderMakeDrinkSuccess(self):
        self.bar = Bartender()
        self.bar.addDrink("Vodka", self.drinkData)
        self.assertEqual(self.bar.makeDrink(), 1)

    # integration test 10
    def testBartenderMakeDrinkFail(self):
        self.bar = Bartender()
        self.assertEqual(self.bar.makeDrink(), -1)

    # integration test 11
    def testbartenderTotalCaloriesBasic(self):
        self.bar = Bartender()
        self.bar.addDrink("Vodka", self.drinkData)
        self.bar.addDrink("Vodka", self.drinkData)
        self.assertEqual(self.bar.totalCalories(), 100)

    # integration test 12
    def testbartenderTotalCaloriesAdvanced(self):
        self.bar = Bartender()
        self.bar.addDrink("Vodka", self.drinkData)
        self.bar.addDrink("Beer", self.drinkData)
        self.bar.drinkQueue[0].addToDrink("Bitters", self.additiveData)
        self.bar.drinkQueue[1].addToDrink("Juice", self.additiveData)
        self.bar.drinkQueue[1].addToDrink("Soda Water", self.additiveData)
        self.assertEqual(self.bar.totalCalories(), 170)

if __name__ == '__main__': 
    unittest.main()