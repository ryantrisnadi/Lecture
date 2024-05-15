d = {'foo': 1, 'bar': 2, 'baz': 3}
for v in d:
    print(v)

#@title Solution

for i in range(1, 10):
    for j in range(i):
        print(i, end='')
        
    print()