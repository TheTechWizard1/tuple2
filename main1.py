mon = int(input('Enter expense for the monday: '))
tue = int(input('Enter expense for the tuesday: '))
wed = int(input('Enter expense for the wednesday: '))
thu = int(input('Enter expense for the thursday: '))
fri = int(input('Enter expense for the friday: '))
sat = int(input('Enter expense for the saturday: '))
sun = int(input('Enter expense for the sunday: '))

common_expense = mon + tue + wed + thu + fri + sat + sun
print(f'The common expense for the week: {common_expense}')

average_expense = (common_expense/7).__round__(2)
print(f'The average expense for the week: {average_expense}')