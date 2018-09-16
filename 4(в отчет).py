import math
constC= 12
constD= 100
print("Введите вероятность совершения собития для Андрея, Маши и Тани через пробел")
constN= [float(i) for i in input().split()]
print("Вероятность попадания в Андрея молнии за 100 дней равна")
print((100/3)**(constN[0]/constC*constD)/math.factorial(math.ceil(constN[0]/constC*constD))*math.exp(-100/3))