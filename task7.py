a = int (input ("введите число 1 "))
b = int (input ("введите число 2 "))
c = int (input ("введите число 3 "))
if a == b and b == c:
    print ("цифры одинаковые")
elif a != b and b == c:
     print ("2 цифры одинаковые")
elif a == b and b != c:
    print ("2 цифры одинаковые")
else:
    print ("Одинаковых цифр нет")