from random import random, randint

loyalty_customer = bool(randint(0,1))
customer_bill = randint(90,200)

print(f'Bill: {customer_bill}')
print(f'Loyalty Status: {loyalty_customer} \n')

if loyalty_customer and customer_bill > 100:
    customer_bill = customer_bill - float((customer_bill / 100) * 20)
    print(f'20% Discount Applied')
elif customer_bill > 100:
    customer_bill = customer_bill - float((customer_bill / 100) * 10)
    print(f'10% Discount Applied')
else:
    print(f'Discount not applied ...')

print(f'\nTotal bill is {float(customer_bill)}')