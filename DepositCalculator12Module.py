# Процентная ставка в банках
perCent = {'TKB': 5.6, 'SKB': 5.9, 'VTB': 4.28, 'SBER': 4.0}

# Ввод клиентом суммы вклада
ClientMoney = int(input('Введите желаемую сумму вклада: '))

# Рассчёт процентов за год
TKB = perCent['TKB'] * ClientMoney / 100
SKB = perCent['SKB'] * ClientMoney / 100
VTB = perCent['VTB'] * ClientMoney / 100
SBER = perCent['SBER'] * ClientMoney / 100

# Вывод информации о накоплениях пользователю
print('Сумма накоплений за год составит:')
print('Банк ТКБ =', round(TKB, 2))
print('Банк СКБ =', round(SKB, 2))
print('Банк ВТБ =', round(VTB, 2))
print('Банк СБЕР =', round(SBER, 2))

# Поиск наилучшего предложения для клиента
MaxValue = TKB, SKB, VTB, SBER
FindMaxValue = max(MaxValue)
print('Максимальная сумма, которую Вы можете заработать =', round(FindMaxValue, 2))

# IgorZhivilov, QAP-94