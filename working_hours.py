# Да се напише програма, която чете час от денонощието(цяло число) и ден от седмицата(текст) - въведени от потребителя
# и проверява дали офисът на фирма е отворен, като работното време на офисът е от 10-18 часа,
# от понеделник до събота включително

hours_of_day = int(input())
day_of_weeks = input()

if hours_of_day >= 10 and hours_of_day <= 18:
    if day_of_weeks == "Monday":
        print("open")
    elif day_of_weeks == "Tuesday":
        print("open")
    elif day_of_weeks == "Wednesday":
        print("open")
    elif day_of_weeks == "Thursday":
        print("open")
    elif day_of_weeks == "Friday":
        print("open")
    elif day_of_weeks == "Saturday":
        print("open")
    elif day_of_weeks == "Sunday":
        print("closed")

else:
    print("closed")
