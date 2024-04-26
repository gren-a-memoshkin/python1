import random

n1 = int(input('Введите колличество кубиков '))
n2 = int(input('Введите колличество попыток '))

result = []

for k in range (n1*n2):
    result.append(random.randint(1,6))

print ('выпало ', result)