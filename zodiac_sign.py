
def sodiac_sign(date,month):
    sign = ""

    if month == 1:
        if date < 21:
            sign = "Aries"
        else:
            sign = 'Taurus'

    if month == 2:
        if date < 20:
            sign = 'Taurus'
        else:
            sign = 'Gemini'

    if month == 3:
        if date < 21:
            sign = 'Gemini'
        else:
            sign = 'Cancer'

    if month == 4:
        if date < 22:
            sign = 'Cancer'
        else:
            sign = 'Leo'

    if month == 5:
        if date < 23:
            sign = 'Leo'
        else:
            sign = 'Virgo'

    if month == 6:
        if date < 23:
            sign = 'Virgo'
        else:
            sign= 'Libra'

    if month ==7:
        if date < 23:
            sign = 'Libra'
        else:
            sign = 'Scorpio'

    if month == 8:
        if date < 22:
            sign = 'Scorpio'
        else:
            sign='Sagittarius'

    if month ==9:
        if date <22:
            sign = 'Sagittarius'
        else:
            sign = 'Copricon'

    if month==10:
        if date <20:
            sign='Copricon'
        else:
            sign='Aquarius'

    if month ==11:
        if date <19:
            sign='Aquarius'
        else:
            sign='Pisces'

    if month ==12:
        if date <21:
            sign='Pisces'
        else:
            sign='Aries'

    return sign

date = int(input("Enter a date: "))
month = str(input("Enter a month: "))

if (month in range(1, 12)) and (date in range(1, 31)):
    sign = sodiac_sign(date, month)
    print(f'Your sodiac zign is: {sign}')
else:
    print('wrong date and month!')
