bill_total = 214.99
discount1 = 10
discount2 = 20

if 100 < bill_total < 200:
    print('Bill is greater than 100')
    bill_total = bill_total - discount1
elif bill_total > 200:
    print('Bill is greater than 200')
    bill_total = bill_total - discount2
else:
    print('Bill is less than 100')

print(f'Total bill: {bill_total}')