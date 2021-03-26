#Revise Listing 4.6, ComputeBMI.py, to let users enter
#their weight in pounds and their height in feet and inches. For example, if a person
#is 5 feet and 10 inches, you will enter 5 for feet and 10 for inches. Here is a sample run:

weight = eval(input("Enter weight in pounds"))
feet = eval(input("Enter feet ONLY"))
inches = eval(input("Enter inches ONLY"))

heightInches = feet * 12 + inches

kilograms_pound = 0.45359237
meters_inch = 0.0254

weight_kg = weight * kilograms_pound
height_meters = heightInches * meters_inch

bmi = weight_kg / (height_meters * height_meters)

print("Computed BMI: " + str(bmi))
if bmi < 18.5:
    print("Underweight")

elif bmi < 25:
    print ("normal")

elif bmi < 30:
    print ("Overweight")

else:
    print("Obese")