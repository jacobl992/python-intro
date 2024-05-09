#simple for loop
for item in range(10):
    print(item)

#shopping list example
prices = [10, 12.5, 8, 2.2, 16, 3, 5, 1, 0.77, 7]
total = 0

for price in prices:
    total += price
print(f'Total: £{total}')
