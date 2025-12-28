# Rent Calculator in Python

# Taking inputs from the user
rent = int(input("Enter your hostel/flat rent = "))
food = int(input("Enter the amount of food ordered = "))
electricity_units = int(input("Enter the total electricity units used = "))
charge_per_unit = int(input("Enter the charge per unit = "))
persons = int(input("Enter the number of persons living in room/flat = "))

# Calculating electricity bill
electricity_bill = electricity_units * charge_per_unit

# Calculating total expense
total_expense = rent + food + electricity_bill

# Calculating per person amount
amount_per_person = total_expense / persons

# Displaying result
print("Each person will pay = ", amount_per_person)
