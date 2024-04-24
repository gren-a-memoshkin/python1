#проверка формата телефонного номера re
import re
phone_numbers = [input("введите номер телефона: ")]
for number in phone_numbers:
    if re.match(r'[78][0-9]{10}', number) and len(number) == 11:
        print("соответсвует формату")
    else:
        print("не соответсвует формату")