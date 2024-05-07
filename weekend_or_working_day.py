# Напишете програма която, чете ден от седмицата (текст), на английски език - въведен от потребителя.
# Ако денят е работен отпечатва на конзолата - "Working day", ако е почивен - "Weekend".
# Ако се въведе текст различен от ден от седмицата да се отпечата - "Error".

day_of_week = input()

if day_of_week == "Monday":
    print("Working day")
elif day_of_week == "Tuesday":
    print("Working day")
elif day_of_week == "Wednesday":
    print("Working day")
elif day_of_week == "Thursday":
    print("Working day")
elif day_of_week == "Friday":
    print("Working day")
elif day_of_week == "Saturday":
    print("Weekend")
elif day_of_week == "Sunday":
    print("Weekend")
else:
    print("Error")

