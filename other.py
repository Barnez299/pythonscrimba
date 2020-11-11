even = []
odd = []

for x in range(10):
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)

print(even, odd)

odds = [ x % 2 == 0 for x in range(20)]

print(odds)