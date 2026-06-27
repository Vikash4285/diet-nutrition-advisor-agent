print("===================================")
print("  Diet and Nutrition Advisor Agent")
print("===================================")

# Get user details
name = input("Enter your name: ")
age = int(input("Enter your age: "))
gender = input("Enter your gender (Male/Female): ")
height = float(input("Enter your height (cm): "))
weight = float(input("Enter your weight (kg): "))
activity = input("Enter activity level (Low/Moderate/High): ")
goal = input("Enter your goal (Lose/Maintain/Gain): ")

# Calculate BMI
height_in_meters = height / 100
bmi = weight / (height_in_meters * height_in_meters)

# BMI Category
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal Weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

# Display details
print("\n----- User Details -----")
print("Name:", name)
print("Age:", age)
print("Gender:", gender)
print("Height:", height, "cm")
print("Weight:", weight, "kg")
print("Activity:", activity)
print("Goal:", goal)

print("\nYour BMI is:", round(bmi, 2))
print("BMI Category:", category)
# Diet Recommendation
print("\n----- Diet Recommendation -----")

if goal.lower() == "lose":
    print("Breakfast : Oats + Green Tea")
    print("Lunch     : Brown Rice + Dal + Salad")
    print("Dinner    : Grilled Chicken/Paneer + Vegetables")

elif goal.lower() == "gain":
    print("Breakfast : Milk + Banana + Peanut Butter")
    print("Lunch     : Rice + Chicken/Paneer + Eggs")
    print("Dinner    : Chapati + Paneer + Fruits")

elif goal.lower() == "maintain":
    print("Breakfast : Idli/Dosa + Sambar")
    print("Lunch     : Rice + Dal + Vegetables")
    print("Dinner    : Chapati + Curry + Salad")

else:
    print("Please enter a valid goal (Lose, Maintain, Gain)")

# Water Intake Recommendation
water = weight * 0.035

print("\n----- Water Intake Recommendation -----")
print("Drink", round(water, 2), "litres of water per day.")
# Exercise Recommendation
print("\n----- Exercise Recommendation -----")

if goal.lower() == "lose":
    print("• 45 minutes Brisk Walking")
    print("• 30 minutes Jogging")
    print("• 20 minutes Cycling")

elif goal.lower() == "gain":
    print("• Weight Training - 45 minutes")
    print("• Push-ups - 3 sets")
    print("• Squats - 3 sets")

elif goal.lower() == "maintain":
    print("• 30 minutes Walking")
    print("• Yoga - 20 minutes")
    print("• Stretching - 15 minutes")

else:
    print("No exercise recommendation available.")

# Daily Calorie Recommendation
print("\n----- Daily Calorie Recommendation -----")

if activity.lower() == "low":
    calories = 2000
elif activity.lower() == "moderate":
    calories = 2500
elif activity.lower() == "high":
    calories = 3000
else:
    calories = 2200

# Adjust calories based on goal
if goal.lower() == "lose":
    calories -= 500
elif goal.lower() == "gain":
    calories += 500

print("Recommended Daily Calories:", calories, "kcal")

# Healthy Lifestyle Tips
print("\n----- Healthy Lifestyle Tips -----")

print("1. Eat plenty of fruits and vegetables.")
print("2. Drink enough water every day.")
print("3. Exercise regularly.")
print("4. Sleep for 7-8 hours every night.")
print("5. Avoid junk food and sugary drinks.")
print("6. Include protein in every meal.")
print("7. Eat meals at regular times.")
print("8. Reduce stress through meditation or yoga.")