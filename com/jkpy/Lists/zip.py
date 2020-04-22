Month = ['Jan', 'Feb', 'Mar']
Sales = [2000, 2400, 1800]
cost = [1400, 1900, 1200]

result = list(zip(Month, Sales, cost))
print(result)

for month, sale, cost in (zip(Month, Sales, cost)):
    print(f'For the month of {month} the profit is :{sale - cost}')

for month, sale, cost in result:
    print(f'For the month of {month} profit is {sale - cost}')

