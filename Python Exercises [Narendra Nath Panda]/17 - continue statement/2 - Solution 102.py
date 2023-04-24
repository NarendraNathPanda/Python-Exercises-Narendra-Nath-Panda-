# Solution I:
names = ['Narendra', 'Shreyasree', 'Shreya', None, 'Tanushree']

for name in names:
    if name is None:
        continue
    print(name)


# Solution II:

names = ['Narendra', 'Shreyasree', 'Shreya', None, 'Tanushree']
for name in names:
    if not isinstance(name, str):
        continue
    print(name)