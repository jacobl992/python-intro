#using a try block
try:
    age = int(input('Age: '))
    print(age)
except ValueError:
    print('Invalid value')

