# wk10ex01_calories_burned.py

def calories_burned(minutes, rate):
    return minutes * rate

sessions = int(input("Number of sessions: "))

total = 0
calories_list = []

for i in range(sessions):
    minutes = float(input("Minutes: "))
    rate = float(input("Calories per minute: "))

    calories = calories_burned(minutes, rate)
    calories_list.append(calories)
    total += calories

for i in range(len(calories_list)):
    print("Session", i + 1, "=", calories_list[i], "calories")

print("Total Calories Burned =", total)
