import math

natural, full, rational, vesh, trash, odd, even, ez = [], [], [], [], [], [], [], []
num = input()
num = num.split(",")
print(num[:])
for i in num:
    if isfinite(i) == 0:
        if i.find("sqrt") == 0 or i == "pi" or i == "e":
            vesh.append(i)
    else:
        print(float(i))
       # if i >= 0 and i-int(i) == 0:







# print(compleks[:])
# print(natural[:])
# print(full[:])
# print(rational[:])
# print(even[:])
# print(ez[:])
# print(odd[:])
# print(vesh[:])


