# Фирма дава следните комисионни на търговците си според града, в който работят и обема на продажбите:
# Напишете конзолна програма, която чете име на град (текст) и обем на продажби (реално число),
# въведени от потребителя, и изчислява и извежда размера на търговската комисионна според горната таблица.
# Резултатът да се изведе форматиран до 2 цифри след десетичната точка.
# При невалиден град или обем на продажбите (отрицателно число) да се отпечата "error".

city = input()
sales = float(input())
commission = 0


if city != "Sofia" and city != "Varna" and city  != "Plovdiv":
    print("error")
elif sales < 0:
    print("error")
elif city == "Sofia":
    if sales >= 0 and sales <= 500:
        commission = 5
    elif sales > 500 and sales <= 1000:
        commission = 7
    elif sales > 1000 and sales <= 10000:
        commission = 8
    elif sales > 10000:
        commission = 12
    total_commission = sales * commission / 100
    print(f'{total_commission:.2f}')
elif city == "Varna":
    if sales >= 0 and sales <= 500:
        commission = 4.5
    elif sales > 500 and sales <= 1000:
        commission = 7.5
    elif sales > 1000 and sales <= 10000:
        commission = 10
    elif sales > 10000:
        commission = 13
    total_commission = sales * commission / 100
    print(f'{total_commission:.2f}')
elif city == "Plovdiv":
    if sales >= 0 and sales <= 500:
        commission = 5.5
    elif sales > 500 and sales <= 1000:
        commission = 8
    elif sales > 1000 and sales <= 10000:
        commission = 12
    elif sales > 10000:
        commission = 14.5
    total_commission = sales * commission / 100
    print(f'{total_commission:.2f}')


