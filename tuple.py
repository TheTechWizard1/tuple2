data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1,'g')

# Создать два пустых списка letters И numbers
letters = []
numbers = []

# Пройтись циклом for по кортежу data_tuple, добавить все строки в список Letters, а все остальное в Numbers
for i in data_tuple:
    if isinstance(i, str):
        letters.append(i)
    elif isinstance(i, bool):
        letters.append(i)
    else:
        numbers.append(i)

print(letters)
print(numbers)

# Из списка Numbers удалить число 6.13 и переместить True в конец списка Letters, затем вставить число 2 между 3 и 1
numbers.remove(6.13)
letters.remove(True)
letters.append(True)
numbers.insert(1, 2)
print(numbers)


# Отсортировать numbers, реверсировать Letters и изменить пару букв в Letters
numbers.sort()
letters.reverse()
letters[1] = 'A'
letters[3] = "F"

# Измените список Numbers в список квадратов своих же чисел
numbers = [num ** 2 for num in numbers]

# Преобразовать списки Numbers b letters в кортежи
numbers_tuple = tuple(numbers)
letters_tuple = tuple(letters)

print(numbers_tuple)
print(letters_tuple)