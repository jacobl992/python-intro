#coordinates example
for x in range(4):
    print(x)
    for y in range(3):
        print(f'({x}, {y})')

#challenge F-shape without string multiplier
numbers = [5, 2, 5, 2, 2]

for number in numbers:
    output = ''
    for i in range(number):
        output += 'x'
    print(output)