# Напишете програма, която чете от конзолата следните три променливи, въведени от потребителя,
# и пресмята цената според цените от таблиците по-горе:
# •	плод  - banana / apple / orange / grapefruit / kiwi / pineapple / grapes;
# •	ден от седмицата  - Monday / Tuesday / Wednesday / Thursday / Friday / Saturday / Sunday;
# •	количество (реално число).
# Резултатът да се отпечата закръглен с 2 цифри след десетичната точка.
# При невалиден ден от седмицата или невалидно име на плод да се отпечата "error".
import math

fruit = input()
day_of_week = input()
quantity = float(input())
price = 0.00


if (fruit != "banana" and fruit != "apple" and fruit != "orange" and fruit != "grapefruit" and
      fruit != "kiwi" and fruit != "pineapple" and fruit != "grapes"):
    print("error")
elif (day_of_week != "Monday" and day_of_week != "Tuesday" and day_of_week != "Wednesday" and
      day_of_week != "Thursday" and day_of_week != "Friday" and day_of_week != "Saturday" and day_of_week != "Sunday"):
    print("error")
elif (day_of_week == "Monday" or day_of_week == "Tuesday" or
      day_of_week =="Wednesday" or day_of_week == "Thursday" or day_of_week == "Friday"):
    if fruit == "banana":
        price = 2.50
    elif fruit == "apple":
        price = 1.20
    elif fruit == "orange":
        price = 0.85
    elif fruit == "grapefruit":
        price = 1.45
    elif fruit == "kiwi":
        price = 2.70
    elif fruit == "pineapple":
        price = 5.50
    elif fruit == "grapes":
        price = 3.85
    total_price = quantity * price
    print(f'{total_price:.2f}')
elif day_of_week == "Saturday" or day_of_week == "Sunday":
    if fruit == "banana":
        price = 2.70
    elif fruit == "apple":
        price = 1.25
    elif fruit == "orange":
        price = 0.90
    elif fruit == "grapefruit":
        price = 1.60
    elif fruit == "kiwi":
        price = 3.00
    elif fruit == "pineapple":
        price = 5.60
    elif fruit == "grapes":
        price = 4.20
    total_price = quantity * price
    print(f'{total_price:.2f}')





