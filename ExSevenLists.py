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

#list methods
numbers.append(52)
print(numbers)
numbers.insert(0,10)
    #insert new item at begining of list
print(numbers)
numbers.remove(10)
print(numbers)
numbers.pop()
    #removes last number in list
    #.clear clears entire list
print(numbers.index(4))
    #returns index of value in list
print(52 in numbers)
    #returns boolean value determining  if value in list
numbers.sort()
    #sort in ascending order
    #.reverse would be in descending order
numbers2 = numbers.copy()
    #creates second table with copied data

