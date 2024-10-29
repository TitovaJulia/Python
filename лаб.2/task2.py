salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# Вычисляем необходимую подушку безопасности
def calculate_needed_capital(salary, spend, increase, months):
    money_capital = 0  # Изначально подушка безопасности равна 0
    for month in range(months):
        # Общие расходы за текущий месяц
        total_monthly_expense = spend * (1 + increase) ** month

        # Недостаток средств после покрытия зарплатой
        deficit = total_monthly_expense - salary

        # Если есть дефицит, добавляем его к подушке безопасности
        if deficit > 0:
            money_capital += deficit

    return round(money_capital)  # Округляем до целого числа

needed_capital = calculate_needed_capital(salary, spend, increase, months)

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", needed_capital)
