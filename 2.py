import math
import re
vesh, rational,numbers, compleks, odd, even, ez, natural, full  = [],[],[],[],[],[],[],[],[]


def find_vesh(mass,nmass):
    for i in mass:
        if "sqrt" in i:
            search = re.findall('(\d+)', i)
            kor = int(search[0])
            if math.sqrt(kor) - int(math.sqrt(kor)) != 0:
                nmass.append(i)
        elif i == "pi" or i == "e":
            nmass.append(i)
        else:
            pass

def find_rational(mass,nmass):
    for i in mass:
        try:
            nmass.append(float(i))
        except ValueError:
            pass


def find_full(mass,nmass):
    for i in mass:
        if i-int(i) == 0:
            nmass.append(i)


def find_natural(mass,nmass):
    for i in mass:
        if i >= 0:
            nmass.append(i)


def find_odd(mass,odd,even):
    for i in mass:
        if i == 0:
            break
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)


def find_ez(mass,nmass):
    n = 0
    for i in mass:
        i = int(i)
        if i == 1 or i == 0:
            n = 1
        if i != 1 and i != 0:
            for j in range(2,i):
                if i % j == 0:
                    n = 1
                    break
            else:
                n = 0

        if n == 0:
            nmass.append(i)
        else:
            pass








num = input()
numbers = num.split(",")
print("Введенные числа:",numbers)

compleks = numbers
find_vesh(numbers,vesh)
find_rational(numbers,rational)
find_full(rational,full)
find_natural(full,natural)
find_odd(full,odd,even)
find_ez(natural,ez)
print("Комплексные числа:", compleks)
print("Вещественные числа:", rational + vesh)
print("Рациональные числа:", rational)
print("Целые числа:", full)
print("Натуральные числа:", natural)
print("Четные числа:", even)
print("Нечетные числа", odd)
print("Простые числа:", ez)


# print(compleks[:])
# print(natural[:])
# print(full[:])
# print(even[:])
# print(ez[:])
# print(odd[:])


