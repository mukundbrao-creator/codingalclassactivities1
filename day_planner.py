print("===== Smart School Day Planner =====")
print("Answer three quick questions and I can help you plan your day!\n")
day = input("What day is it today? (Monday through Sunday) ").strip().capitalize()
weather = input("What is today's weather? (rainy / cloudy / sunny) ").strip().lower()
homework = input("Is your homework done yet? (yes/no) ").strip().lower()

print()
print(f"Here is the plan for your {day}.")
print("-" * 35)

if day in ("Saturday", "Sunday"):
    print("Day Type: Weekend | Enjoy your time at home!")
elif day == "Monday":
    print("Day Type: School Day | Pack your daily planner.")
elif day == "Friday":
    print("Day Type: Last Day | Return your library books.")
elif day in ("Tuesday", "Wednesday", "Thursday"):
    print("Day Type: Regular School Day | Stay focused!")
else: 
    print("Day not recognized. Please check your spelling.")
if weather == "sunny" and homework == "yes":
    print("Head to the park - homework is done.")
if weather == "rainy" or weather == "cloudy":
    print("Pack your umbrella - it may get wet outside.")
if not (homework == "yes"):
    print("Your homework is not done - complete it before going outside!")

if weather == "rainy" and not (homework == "yes"):
    print("Stay inside, finish your homework, and watch your favourite show.")
elif weather == "sunny" and homework == "yes" and not (day in ("Saturday", "Sunday")):
    print("You are all set for a great day at school!")
elif day in ("Saturday", "Sunday") and weather == "sunny":
    print("Perfect weekend weather! Head out and play outside!")
else: 
    print("You got this! Take it one step at a time!")

print()
print("Plan complete! Have a wonderful day!")