stock = {
    'banana': 6,
    'apple': 0,
    'orange': 32,
    'pear': 15}
prices = {
    'banana': 4,
    'apple': 2,
    'orange': 1.5,
    'pear': 3}

result = 0
for key in stock.keys():
    result += stock.get(key, 0) * prices.get(key, 0)

print(result)

