#Given the temperature determine whats suitable to wear.

temp = input("Enter the temperature (sunny, rainy, snowy): ")

if temp == "sunny":
    print("Wear something cool!")
elif temp == "rainy":
    print("Grab your raincoat!")
elif temp == "snowy":
    print("Grab your coat!")
else:
    print("Wear what you like!")