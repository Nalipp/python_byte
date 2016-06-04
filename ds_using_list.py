shoplist = ['apple', 'mango', 'carrot', 'banana']

print('I have', len(shoplist), 'items to purchase.')

print('These items are:', end=' ')
for item in shoplist:
    print(item, end=', ')

print('\nI also have to buy rice.')

shoplist.append('rice')
print('My shopping list is now', shoplist)

print('I will sort my list now', shoplist)
shoplist.sort()
print('Sorted shopping list is', shoplist)

print('The first item I will buy is', shoplist[0])
olditem = shoplist[0]
print('I bought the', olditem)

for i in shoplist:
    print('I will buy :', i)

print(shoplist)
del(shoplist[0])
print(shoplist)
del(shoplist[1])
print(shoplist)
