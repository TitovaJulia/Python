numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

# Находим индекс пропущенного элемента (None)
missing_index = numbers.index(None)

# Фильтруем список для расчета среднего арифметического
filtered_numbers = [num for num in numbers if num is not None]

# Считаем сумму и количество элементов для среднего
total_sum = sum(filtered_numbers)
count = len(filtered_numbers)

# Вычисляем среднее арифметическое
average = total_sum / (count + 1)  # +1 для учета пропущенного элемента

# Заменяем пропущенный элемент средним арифметическим
numbers[missing_index] = average

print("Измененный список:", numbers)
