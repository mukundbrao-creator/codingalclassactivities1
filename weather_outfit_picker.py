temperature = int(input("Enter the temperature in Celsius: "))

if temperature < 20:
    outfit = "jacket"
    print("It is cold today.")
    print("Wear a", outfit)
else: 
    outfit = "t-shirt"
    print("It is warm today.")
    print("Wear a", outfit)

is_raining = input("Is it raining? (yes/no) ").lower()

if is_raining == "yes":
    print("Bring an umbrella!")

wind_speed = int(input("Enter the wind speed in km/h: "))

if wind_speed > 30: 
    needs_windbreaker = "yes"
    print("It is windy today.")
    print("Put a windbreaker over your", outfit)
else: 
    needs_windbreaker = "no"
    print("It is calm today.")
    print("Do not put a windbreaker over your", outfit)

has_puddles = input("Are there puddles on the ground today? (yes/no) ").lower()
if has_puddles == "yes":
    shoes = "boots"
    print("The ground is wet today.")
    print("Wear", shoes)
else: 
    shoes = "sneakers"
    print("The ground is dry today.")
    print("Wear", shoes)
print("")
print("Weather check complete!")

print("===== WEATHER OUTFIT PICKER =====")
print("Temperature:", temperature)
print("Outfit Chosen:", outfit)
print("Raining:", is_raining.upper())
print("Needs Windbreaker:", needs_windbreaker)
print("Shoes Chosen:", shoes.upper())
print("=================================")
