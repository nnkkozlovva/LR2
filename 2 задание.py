salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
money_needed = 0
current_spend = spend
for month in range(1, months + 1):
    monthly_deficit = current_spend - salary

    if monthly_deficit > 0:
        money_needed += monthly_deficit

    current_spend *= (1 + increase)

money_needed = round(money_needed)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_needed)