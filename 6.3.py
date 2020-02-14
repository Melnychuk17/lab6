# За s-назвою місяця визначити відповідну пору року.
# Мельничук Олена Костянтинівна 122В

from enum import Enum
class month (Enum):
    January = 1
    February = 2
    March = 3
    April = 4
    May = 5
    June = 6
    July = 7
    August = 8
    September = 9
    October = 10
    November = 11
    December = 12
class season (Enum):
    Winter = 1
    Spring = 2
    Summer = 3
    Autumn = 4
while True:
    while True:
        try:
            s=int(input('Month: '))
            break
        except ValueError:
            print('Please enter a month: ')

    if s==month.January.value or s==month.February.value or s==month.December.value:
        print(season.Winter.name)
    elif s==month.March.value or s==month.April.value or s==month.May.value:
        print(season.Spring.name)
    elif s==month.October.value or s==month.September.value or s==month.November.value:
        print(season.Autumn.name)
    elif s==month.June.value or s==month.July.value or s==month.August.value:
        print(season.Summer.name)
    result = input('Want to restart? If yes - 1, no - other: ')
    if result == '1':
        continue
    else:
        break
