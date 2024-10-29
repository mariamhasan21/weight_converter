#Weight Converter (kgs/lbs)
print("-------------------Welcome to Weight Converter--------------------")
print("Before converting, please identify which measurement you are using") #telling the user whether they are using kg or lbs
print("------------------------------------------------------------------")
weight = float(input("Enter your weight: "))
unit = {1:'Kilogram', 2:'Pound'}
user_unit = float(input("Select the converter:\n1. Kilogram 2. Pound\nChoose your option: "))

if user_unit == 1: #takes the keys from the unit dictionary
    new_weight = float(weight * 0.454) #converts lbs to kgs
    print(f"Your weight in Kilogram is {new_weight:.2f} kg")
elif user_unit == 2:
    new_weight = float(weight * 2.205) #converts kgs to lbs
    print(f"Your weight in Pounds is {new_weight:.2f} lbs")
else:
    print("Invalid option. Please select 1 or 2.")
