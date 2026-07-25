field_1 = 25
field_2 = 50
field_3 = 75
field_4 = 100
field_5 = 150
total = field_1 + field_2 + field_3 + field_4 + field_5
average = total / 5
print("Total harvest: ", total, "kg")
print("Average kg per field: ", average, "kg")
price_per_kg = 15
earnings = price_per_kg * total
print("The total earnings are: Rs. ", earnings)
bags = total // 25
leftover = total % 25
print("Total amount of bags: ", bags)
print("Leftover produce: ", leftover, "kg")
last_year = 50
print("Is it greater than last year?", total > last_year)
print("It it the same as last year?", total == last_year)
print("Is it at least as good as last year?", total >= last_year)
total += 30
print("After bonus crops: ", total, "kg")
total -= 15
print("After saving seeds for next year: ", total, "kg")
bags = total // 25
print("Final amount of bags needed: ", bags)