desserts = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisu', 'Chocolate Cake']

for dessert in desserts:
    if dessert == 'Churros':
        print(f'Yes! One of my favorites {dessert}!')
    else:
        print(f'No, sorry i dont like {dessert}')


for dessert in desserts:
    if dessert == 'Churros':
        print(f'Yes! One of my favorites {dessert}!')
        break

for dessert in desserts:
    if dessert == 'Churros':
        continue
    print(f'Other Desserts i like are {dessert}!')

for dessert in desserts:
    if dessert == 'Churros':
        pass
    print('Other desserts I like are', dessert)
