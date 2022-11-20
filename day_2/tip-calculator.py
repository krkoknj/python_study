print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? "))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
peoples = int(input("How many people to split the bill? "))

percentage = percentage * 0.01 + 1

print(f"per={percentage}")

pay = round(total_bill * percentage / peoples, 2)

print(f"Each person should pay: ${pay}")