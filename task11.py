#проверка формата телефонного или автомобильного номера re
import re
phone_numbers = [input("введите номер телефона или номер авто: ")] or "номер не введен"
for number in phone_numbers:
    if re.match(r'[+78][0-9]{10}', number) and len(number) <= 12:
        print("соответсвует формату телефонного номера")
    elif re.match(r"[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}", number) and len(number) ==9:
        print ("соответсвует номеру автомобиля")
    else:
        print("не соответсвует формату РФ")