# Да се напише програма която чете ден от седмицата (текст) – въведен от потребителя и
# принтира на конзолата цената на билет за кино според деня от седмицата:

day_of_week = input()

price_ticket = day_of_week



if day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Friday":
    price_ticket = 12
elif day_of_week == "Wednesday" or day_of_week == "Thursday":
    price_ticket = 14
elif day_of_week == "Saturday" or day_of_week == "Sunday":
    price_ticket = 16



print(price_ticket)