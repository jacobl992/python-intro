#name and fav colour
name = input('What is your name? ')
fav_colour = input('What is your favourite colour? ')
print(name + ' likes ' + fav_colour)

#birth year calculation
birth_year = input('Birth year: ')
age = 2024 - int(birth_year)
print('Your age is ' + str(age))

#weight converson
weight_metric = input('What is your weight in kg? ')
weight_imperial = round(float(weight_metric) * 2.2, 2)
print('Your weight in pounds is ' + str(weight_imperial) + '.')