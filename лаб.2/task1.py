money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

months = 0  # Счетчик месяцев

# Текущие расходы
current_spend = spend

while True:
    # Бюджет текущего месяца
    budget = money_capital + salary

    # Проверяем, можем ли мы покрыть расходы
    if budget >= current_spend:
        months += 1
        # Уменьшаем подушку безопасности на разницу
        money_capital = budget - current_spend

        # Увеличиваем расходы на 5% для следующего месяца
        current_spend *= (1 + increase)
    else:
        break


# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

print("Количество месяцев, которое можно протянуть без долгов:", months)
