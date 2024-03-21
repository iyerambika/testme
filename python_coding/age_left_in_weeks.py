age = float(input())

num_of_weeks_total = 90 * 52
num_of_weeks_spent = age * 52
num_of_weeks_left  = round(num_of_weeks_total - num_of_weeks_spent)
print(f"You have {num_of_weeks_left} weeks left.")