import copy

warehouse = list()
warehouse.append({'name': 'Lolly Pop', 'price': 0.4, 'weight': 133})
warehouse.append({'name': 'Licorice', 'price': 0.1, 'weight': 251})
warehouse.append({'name': 'Chocolate', 'price': 1, 'weight': 601})
warehouse.append({'name': 'Sours', 'price': 0.01, 'weight': 513})
warehouse.append({'name': 'Hard candies', 'price': 0.3, 'weight': 433})

print('Source list of candies')
for item in warehouse:
    print(item)

warehouse_copy = copy.deepcopy(warehouse)
print('Discounted list')
for item in warehouse_copy:
    if item['weight'] > 300:
        item['price'] = item['price'] * 0.8
    print(item)    

print('\n\n\n')

class Delicacy:
    def __init__(self, name, price, weight):
         self.name = name
         self.price = price
         self.weight = weight

    def __str__(self):
        return f'Name: {self.name} <> Price: {self.price} <> Weight: {self.weight}'

warehouse = list()

warehouse.append(Delicacy('Lolly Pop', 0.4, 133))
warehouse.append(Delicacy('Licorice', 0.1, 251))
warehouse.append(Delicacy('Chocolate', 1, 601))
warehouse.append(Delicacy('Sours', 0.01, 513))
warehouse.append(Delicacy('Hard candies', 0.3, 433))

# Deepcopy
'''new_warehouse = copy.deepcopy(warehouse)
for item in new_warehouse:
    if item.weight > 300:
        item.price *= 0.8'''

# Normal copy
new_warehouse = copy.copy(warehouse)
for item in new_warehouse:
    if item.weight > 300:
        item.price *= 0.8

print('*' * 20)
print('Source list of candies')
for item in warehouse:
    print(item)

print('*' * 20)
print('Price proposal')
for item in new_warehouse:
    print(item)

# USING SHALLOW COPY DOES NOT ALLOW US TO HAVE BOTH VERSIONS OF THE LIST LIVE AT THE SAME TIME.