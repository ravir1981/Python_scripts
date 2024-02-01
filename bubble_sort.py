# Bubble Sort
l1 = [8, 10, 6, 2, 4]
swp = True
while swp:
    swp = False
    for i in range(len(l1) - 1):
        if l1[i] > l1[i + 1]:
            swp = True
            l1[i], l1[i + 1] = l1[i + 1], l1[i]
print(l1)

