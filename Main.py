from Bartender import Bartender

def main():
    additiveData = {"Juice": 20, "Bitters": 60, "Soda Water": 10}
    drinkData = {"Vodka": 50, "Beer": 30}

    exitInput = 0

    bar = Bartender()

    print("--- Welcome to the Big Waldorf! ---")

    while True:
            print("Would you like to add a drink, have a drink made, or check the total calories of your order?")
            userInput = input("Type 1 for adding a drink, 2 for making a drink, 3 for checking the total calories, and 0 to exit. ")
            
            if userInput == '0':
                break

            if userInput == '1':
                print("What drink would you like to add? If you don't want a drink, type 0")
                drinkInput = input("We currently have Vodka or Beer (case sensitive): ")

                if drinkInput == '0':
                    break
                
                bar.addDrink(drinkInput, drinkData)
                print("You bought a " + drinkInput +"!")

                while True:
                    print("What additive would you like to put in your drink? If you are done adding things, type 0")
                    additiveInput = input("We currently have Juice, Bitters, or Soda Water (case sensitive): ")
                    
                    if additiveInput == '0':
                        break

                    bar.drinkQueue[-1].addToDrink(additiveInput, additiveData)
                    print("You added a " + additiveInput +"!")


            if userInput == '2':
                 bar.makeDrink()

            if userInput == '3':
                bar.totalCalories()

            else:
                print("Your input was not accepted. Maybe you misclicked?")



if __name__=="__main__":   
    main()