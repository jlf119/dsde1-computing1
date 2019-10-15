
import random
# gets a number from the user between 1 and 10
print('lets play a game - give me a random number from 1 to 10')
userrand = input()
# changes the user input from a string to an integer
userrandfloat = float(userrand)
userrandint = int(userrandfloat)
# creates a random number
comrand = random.randint(1,10)
# prints if the user input matches the random number with true or false
print(userrandint == comrand)