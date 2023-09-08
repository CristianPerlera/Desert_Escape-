import random
print("""Welcome to Camel!
You have stolen a camel to make your way across the great Mobi desert.
The bandits want their camel back and are chasing you down! Survive your
desert trek and out run the bandits.""")
# Question 1: Variable Starting Values
done = False
miles = 0
thirst = 0
tired = 0 
bandits = -20
drinks = 3

while not done:
    print("""
          A. Drink from your canteen.
          B. Ahead moderate speed.
          C. Ahead full speed.
          D. Stop for the night.
          E. Status check.
          Q. Quit.""")
    choice = input("Your choice? ").upper()#.upper() makes it so the player can use capital or lower case letter.
    #Question 2: Different Choices
    if choice == "q".upper():
      done = True
    elif choice == "e".upper():
      print(f"Miles taveled: {miles}")
      print(f"Drinks in canteen: {drinks}")
      print(f"The bandits are {miles - bandits} miles behind you.")
      
    elif choice == "d".upper():
      tired = 0
      print("The camel is happy")
      bandits += random.randint(7, 14)
      
    elif choice == "c".upper():
      miles += random.randint(10, 20)
      print(f"You have traveled {miles} miles.")
      thirst += 1
      tired += random.randint(1, 3)
      bandits += random.randint(7, 14)
      
    elif choice == "b".upper():
      miles += random.randint(5, 12)
      print(f"You have traveled {miles} miles.")
      tired += 1
      bandits += random.randint(7, 14)
      
    elif choice == "a".upper():
      if drinks > 0:
        print("You drank water. You are no longer thirsty")
        drinks -= 1
        thirst = 0
      else:
        print("You have no water left!")
        
    elif choice != "a" or "b" or  "c" or "d" or "e" or  "e":
         print("Please choose a, b, c, d, e, q")
      
      
    #Question 3: Post-Turn Events
    if thirst > 6:
      print("You died of thirst!")
      done = True
    elif thirst > 4 and thirst < 6:
      print("You are thirsty.")

    if tired > 8:
      print("Your camel is dead")
      done = True 
    elif tired > 5 and tired < 8:
      print("Your camel is getting tired.")

    #Question 4: Warnings
    if bandits == 0:
       print("You have been captured!")
       done = True
    elif bandits < 15:
      print("The bandits are getting close")

    if miles >= 200:
      print("You escaped the dessert, yay!")
      done = True
        
    #Honors Question - Oasis
