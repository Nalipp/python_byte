bri = set(['brizil', 'russia', 'india'])

print('india' in bri)
print('usa' in bri)

bric = bri.copy()
bric.add('china')
print(bric)
print(bric.issuperset(bri))
bri.remove('russia')
print(bri)
print(bri & bric)
