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

#2D lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][1])
matrix[0][1] = 99
print(matrix[0][1])

for row in matrix:
    for item in row:
        print(item)