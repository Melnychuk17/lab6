# Значення змінної x, що позначає деяку суму грошей в валюті p, замінити величиною
# цієї ж суми в гривнях.
# Мельничук Олена Костянтинівна 122В

from enum import Enum
class converter (Enum):
    USD = 1
    EUR = 2
    CZK = 3
    PLN = 4
while True:
    while True:
        try:
            p=int(input('Currency: '))
            break
        except KeyError:
            print('Please enter a currency')
    while True:
        try:
            x=float(input('Amount of money: '))
            break
        except ValueError:
            print('Enter the amount of money')

    if p == converter.USD.value:
        print(x*24.3)
    elif p == converter.EUR.value:
        print(x*26.6)
    elif p == converter.CZK.value:
        print(x*1.1)
    elif p == converter.PLN.value:
        print(x*6.3)
    result = input('Want to restart? If yes - 1, no - other: ')
    if result == '1':
        continue
    else:
        break

