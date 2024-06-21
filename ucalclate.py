def calculate_discount(homework_points, test_points, num_of_visits):
    discount = 0

    if homework_points >= 70 or 80 and test_points >= 80:
        discount = 3000
    elif homework_points >= 70 or 80 and test_points >= 60 and num_of_visits >= 8:
        discount = 2500
    elif homework_points >= 70 or 80 and test_points >= 60:
        discount = 2000
    elif homework_points >= 50 or 60 and test_points >= 80:
        discount = 2000
    elif homework_points >= 50 or 60 and test_points >= 60 and num_of_visits >= 6:
        discount = 2000
    elif homework_points >= 50 or 60 and test_points >= 60:
        discount = 1000

    return discount

homework_points = int(input("Введите баллы за Д/З: "))
test_points = int(input('Введите баллы за тест: '))
num_of_visits = int(input('Введите количество посещений: '))
final_discount = calculate_discount(homework_points, test_points, num_of_visits)
print(f'Сумма скидки: {final_discount}')