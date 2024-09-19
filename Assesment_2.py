# Create BMI calculator using python
the_height=float(input("Enter the height in cm:"))
the_weight=float(input("Enter the weight in kg:"))
the_BMI = the_weight/(the_height/100)**2
print("Your Body Mass Index is",the_BMI)