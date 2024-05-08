is_hot = False
is_cold = False

if is_hot:
    print('Drink water')
elif is_cold:
    print('Stay warm')
else:
    print('Relax')

#logical operators
    #and
    #or
    #not
    #< and > and !=

#weight converter
weight = float(input('What is your weight (lbs/kgs)? '))
unit_of_weight = input('What is unit did you use? Enter "L" for lbs, "KG" for kilograms: ')

if unit_of_weight == 'L':
    print('Your weight in KG is ' + str(round(weight / 2.2,2)))
elif unit_of_weight == 'KG':
    print('Your weight in lbs is ' + str(round(weight * 2.2, 2)))
else:
    print('Error - Incorrect unit given')

