
import random
# gets a number from the user between 1 and 10
print('lets play a game - give me 3 random numbers from 1 to 10')
userrand1 = input()
userrand2 = input()
userrand3 = input()
# changes the user input from a string to an integer
userrandfloat1 = float(userrand1)
userrandint1 = int(userrandfloat1)
userrandfloat2 = float(userrand2)
userrandint2 = int(userrandfloat2)
userrandfloat3 = float(userrand3)
userrandint3 = int(userrandfloat3)
# creates a random number
comrand = random.randint(1,10)
# prints if the user input matches the random number with true or false
if userrandint1 == comrand:
    print('true')
elif userrandint2 == comrand:
    print('true')
elif userrandint3 == comrand:
    print('true')
else:
    print('false')