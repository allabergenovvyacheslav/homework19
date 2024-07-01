data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])]

def calculate_structure_sum(data_structure):

    '''решение для подсчёта суммы всех чисел и длин всех строк в параметре data_structure'''

    # расчёт вёлся следующим образом:
    # 1 + 2 + 3 + len('a') + 4 + len('b') + 5 + 6 + len('cube') + 7 + .... + 35 = 99

    total = 0  #создаем переменую для возврата суммы всех элементов
    if isinstance(data_structure, str):  # проверка отношения параметра к строкам
        return len(data_structure)  # возврат длины строк
    elif isinstance(data_structure, int):  # проверка отношения параметра к числам
        return data_structure  # возвращаем числа
    elif isinstance(data_structure, dict):  # проверка отношения параметра к словарю
        for keys, values in data_structure.items(): #циклом перебираем ключи и значения в параметре и объединяем в пару
            total += calculate_structure_sum(keys)  # добавляем ключи в сумму
            total += calculate_structure_sum(values)  # добавляем значения в сумму
    elif isinstance(data_structure, (list, tuple, set)):  # проверка отношения параметра множество в кортеже в списке
        for index in data_structure:  # перебираем циклом параметр
            total += calculate_structure_sum(index)  # рекурсивная функция, добавляем сумму элементов в переменую

    return total  # возвращаем общую сумму

result = calculate_structure_sum(data_structure)
print(result)