import random
    #this module is in the external libraries

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
