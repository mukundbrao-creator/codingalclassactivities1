a = int(input("Enter value #1: "))
b = int(input("Enter value #2: "))
c = int(input("Enter value #3: "))
avg = (a + b + c) / 3
print("The average is: ", avg)

if avg > a and avg > b and avg > c:
    print("%d is higher than %d, %d, and %d." %(avg, a, b, c))
elif avg > a and avg > b:
    print("%d is higher than %d and %d." %(avg, a, b))
elif avg > a and avg > c:
    print("%d is higher than %d and %d." %(avg, a, c))
elif avg > b and avg > c:
    print("%d is higher than %d and %d." %(avg, b, c))
elif avg > a:
    print("%d is higher than ONLY %d." %(avg, a))
elif avg > b:
    print("%d is higher than ONLY %d." %(avg, b))
elif avg > c:
    print("%d is higher than ONLY %d." %(avg, c))
else:
    print("Invalid input. Check if you typed correctly.")

