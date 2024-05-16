import random
    #this module is in the external libraries
from pathlib import Path

for i in range(3):
    print(random.random())
    print(random.randint(1,20))

members = ['John', 'Paul', 'George', 'Ringo']
leader = random.choice(members)
print(leader)

#exercise 2-dice-roll


class Dice:
    def roll(self, dice1_sides, dice2_sides):
        dice1 = random.randint(1, dice1_sides)
        dice2 = random.randint(1, dice2_sides)
        roll_result = (dice1, dice2)
        return roll_result


dice = Dice()
print(dice.roll(6, 3))

#file paths with Python

path = Path()
#print(path.glob('*.xls'))
    # this would find all excel files
print(path.glob('*.py'))
    # this would find all python files
    # after you run this you get a generator object
    # this can be iterate over:

for file in path.glob('*.py'):
    print(file)
