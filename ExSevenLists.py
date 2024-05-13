#indexing list
names = ['Jake', 'Jim', 'John', 'James', 'Jack', 'Joe', 'Josh']
print(names[2])
print(names[-2])
print(names[0])
print(names[2:5])

#find largest number in list
numbers = [1, 4, 6, 25, 8, 3]
max = 0

for number in numbers:
    if number > max:
        max = number
print(f'({max} is the largest number in list)')

