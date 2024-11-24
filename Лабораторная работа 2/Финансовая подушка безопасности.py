money_capital = 20000 # Подушка безопасности
salary = 5000 # Ежемесячная зарплата
spend = 6000 # Траты за первый месяц
increase = 0.05 # Ежемесячный рост цен

months = 0 # Счетчик месяцев

while money_capital >= 0:
 money_capital += salary # Добавляем зарплату
 money_capital -= spend # Вычитаем расходы
 if money_capital < 0: # Если денег не хватает, останавливаем расчет
  break
 spend *= (1 + increase) # Увеличиваем расходы на 5%
 months += 1 # Увеличиваем счетчик месяцев

print("Количество месяцев, которое можно протянуть без долгов:", months)
