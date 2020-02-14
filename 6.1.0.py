# За датою d, m, y визначити дату наступного і попереднього дня. В програмі врахувати
# наявність високосних років.
# Мельничук Олени Костянтинівни 122В

days = range(1, 32)
months = range(1, 13)
years = range(1901, 2020)
while True:
    while True:
        try:
            d, m, y = int(input('Day: ')), \
                      int(input('Month:')), \
                      int(input('Year:'))
            break
        except ValueError:
            print('Enter correct number')

    q31 = [1, 3, 5, 7, 8, 10]
    q30 = [4, 6, 9, 11]
    l = 0
    t = 0

    if d in days and m in months and y in years:
        if y % 4 == 0:
            while m < 1 or m > 12:
                m = int(input("input m!:"))
            if m == 2:
                x = 1
            elif m == 12:
                x = 4
            elif m in q30:
                x = 2
            elif m in q31:
                x = 3

            while d < 1 or (d > 29 and x == 1) or (d > 30 and x == 2) or (d > 31 and x == 3) or (d > 31 and x == 4):
                d = int(input("input d!:"))
# дата наступного дня n
# дата попереднього дня p
            if (d == 29 and x == 1) or (d == 30 and x == 2) or (d > 31 and x == 3):
                n = 1
                t = m + 1
            elif m == 12 and d <31:
                n = d + 1
                t = 12
                l = y
            elif x == 4 and d == 31:
                n = 1
                t = 1
                l = y + 1
            elif m == 1 and d == 1:
                n = 2
                t = 1
                l = y
            else:
                n = d + 1
                t = m
                l = y

            if (d == 1 and x == 1) or (d == 1 and x == 2):
                p = 31
                m -= 1
            elif (m == 3 and d == 1):
                p = 29
                m = 2
            elif (m == 5 and d == 1) or (m == 7 and d == 1) or (m == 10 and d == 1) or (m == 12 and d == 1):
                p = 30
                m -= 1
            elif d == 1 and m == 1:
                p = 31
                m = 12
                y -= 1
            else:
                p = d - 1

            print('The previous day-',p,'/', m,'/', y,".",'The next day-',n,'/', t,'/', l)

        else:
            while m < 1 or m > 12:
                m = int(input("input m!:"))
            if m == 2:
                x = 1
            elif m == 12:
                x = 4
            elif m in q30:
                x = 2
            elif m in q31:
                x = 3

            while d < 1 or (d > 28 and x == 1) or (d > 30 and x == 2) or (d > 31 and x == 3) or (d > 31 and x == 431):
                d = int(input("input d!:"))
            # дата наступного дня n
            # дата попереднього дня p
            if (d == 28 and x == 1) or (d == 30 and x == 2) or (d == 31 and x == 3):
                n = 1
                t = m + 1
                l = y
            elif m == 12 and d == 31:
                n = 1
                t = m
                l = y + 1
            elif m == 12 and d <31:
                n = d + 1
                t = 12
                l = y
            elif d == 1 and m == 1:
                n = 2
                t = 1
                l = y
            else:
                n = d + 1
                t = m
                l = y


            if (d == 1 and x == 1) or (d == 1 and x == 2):
                p = 31
                m -= 1
            elif (m == 3 and d == 1):
                p = 28
                m = 2
            elif (m == 5 and d == 1) or (m == 7 and d == 1) or (m == 10 and d == 1) or (m == 12 and d == 1):
                p = 30
                m -= 1
            elif d == 1 and m == 1:
                p = 31
                m = 12
                y -= 1
            else:
                p = d - 1

            print('The previous day-',p,'/', m,'/', y,".",'The next day-',n,'/', t,'/', l )
    result = input('Want to restart? If yes - 1, no - other: ')
    if result == '1':
        continue
    else:
        break
