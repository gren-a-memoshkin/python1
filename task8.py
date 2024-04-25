#сортировка списков 

import random

list1 = []
list2 = []
list3 = []
list4 = []

for k in range (5):
    list1.append(random.randint(-5,5)*2)
for i in range (3):
    list2.append(random.randint (-5,5)*2)

for i in list1:
    if i >= 0:
        list3.append(i)
    elif i <= 0:
        list4.append(i)
for i in list2:
    if i >= 0:
        list3.append(i)
    elif i <= 0:
        list4.append(i)

print (list1, list2, list3, list4)
   