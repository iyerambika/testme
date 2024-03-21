print("Welcome to the Tip calculator")
total_bill    = float(input("What was the total bill?\n"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
num_people    = int(input("How many people to split the bill?\n"))
total_amount = total_bill + (total_bill * tip_percentage / 100)
amount_per_person = total_amount / num_people
print(f"Each person should pay: ${amount_per_person:.2f}")

