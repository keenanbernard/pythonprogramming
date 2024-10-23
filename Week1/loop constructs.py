string = 'looping'

for item in string:
    print(item)


favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisu', 'Chocolate Cake']

for i in favorites:
    print(f'Dessert {i}')

count = 0
while count < len(favorites):
    print(favorites[count])
    count += 1

for idx, item in enumerate(favorites): # includes the index of the list
    print(f'Dessert {idx} {item}')
