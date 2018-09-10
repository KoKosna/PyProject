import math

natural, full, rational, vesh, compleks, odd, even, ez = [],[],[],[],[],[],[],[]
num = input()
l = num.split(",")
# c = list(map(lambda x: float(x), l))  # переводим список в числа
print(l)
for x in l:
    if x == 'pi' or x == 'e':
        vesh.append(x)
        l.remove(x)
for x in l:
    if x.find('i') != -1:
        compleks.append(x)
        l.remove(x)
newl = list(map(lambda x: float(x), l))
for x in newl:
    rational.append(x)
    int(x)
    if x >= 0 and x-int(x) == 0:
        natural.append(x)
    if x-int(x) == 0:
        full.append(x)
    if x % 2 == 0:
        even.append(x)
    if x % 2 == 1:
        odd.append(x)
for x in natural:
    for i in range(x):
        if x % i == 0:
            break
        elif i == x - 1:
            ez.append(x)


print(compleks[:])
print(natural[:])
print(full[:])
print(rational[:])
print(even[:])
print(ez[:])
print(odd[:])
print(vesh[:])


