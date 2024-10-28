print("-------------------Welcome to Weight Converter--------------------")
print("Before converting, please identify which measurement you are using")
print("------------------------------------------------------------------")
weight = float(input("Enter your weight: "))
unit = {1:'Kilogram', 2:'Pound'}
user_unit = float(input("Select the converter:\n1. Kilogram 2. Pound\nChoose your option: "))

if user_unit == 1:
    new_weight = float(weight * 0.454)
    print(f"Your weight in Kilogram is {new_weight:.2f} kg")
elif user_unit == 2:
    new_weight = float(weight * 2.205)
    print(f"Your weight in Pounds is {new_weight:.2f} lbs")
else:
    print("Invalid option. Please select 1 or 2.")
