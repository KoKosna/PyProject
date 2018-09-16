import math
constC= 12
constD= 100
print("Введите вероятность совершения собития для Андрея, Маши и Тани через пробел")
constN= [float(i) for i in input().split()]
err=1000
i=0
p=0
while i<1:
    i+=0.005
    if err>= math.fabs(constC*i*((1-i)**((constC-1)))-constN[0]):
        err= math.fabs(constC*i*((1-i)**((constC-1)))-constN[0])
        p=i
#print(constC*p*((1-p)**((constC-1))))
#print(constD*p*((1-p)**((constD-1))))
print(p)
