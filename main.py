import streamlit as st

st.set_page_config(page_title="Diet and Nutrition Advisor", page_icon="🥗")

st.title("🥗 Diet and Nutrition Advisor Agent")

name = st.text_input("Enter your name")
age = st.number_input("Enter your age", 1, 100)
gender = st.selectbox("Gender", ["Male", "Female"])
height = st.number_input("Height (cm)", min_value=50.0)
weight = st.number_input("Weight (kg)", min_value=10.0)
activity = st.selectbox("Activity Level", ["Low", "Moderate", "High"])
goal = st.selectbox("Goal", ["Lose", "Maintain", "Gain"])

if st.button("Generate Advice"):

    bmi = weight / ((height / 100) ** 2)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal Weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    st.subheader("Your Details")
    st.write("**Name:**", name)
    st.write("**Age:**", age)
    st.write("**Gender:**", gender)
    st.write("**BMI:**", round(bmi, 2))
    st.write("**Category:**", category)

    st.subheader("🥗 Diet Recommendation")

    if goal == "Lose":
        st.write("Breakfast: Oats + Green Tea")
        st.write("Lunch: Brown Rice + Dal + Salad")
        st.write("Dinner: Grilled Chicken/Paneer + Vegetables")

    elif goal == "Gain":
        st.write("Breakfast: Milk + Banana + Peanut Butter")
        st.write("Lunch: Rice + Chicken/Paneer + Eggs")
        st.write("Dinner: Chapati + Paneer + Fruits")

    else:
        st.write("Breakfast: Idli/Dosa + Sambar")
        st.write("Lunch: Rice + Dal + Vegetables")
        st.write("Dinner: Chapati + Curry + Salad")

    water = weight * 0.035
    st.subheader("💧 Water Intake")
    st.write(f"Drink **{water:.2f} litres** per day.")

    st.subheader("🏃 Exercise")

    if goal == "Lose":
        st.write("• 45 min Brisk Walking")
        st.write("• 30 min Jogging")
        st.write("• 20 min Cycling")
    elif goal == "Gain":
        st.write("• Weight Training - 45 min")
        st.write("• Push-ups - 3 sets")
        st.write("• Squats - 3 sets")
    else:
        st.write("• 30 min Walking")
        st.write("• Yoga - 20 min")
        st.write("• Stretching - 15 min")

    if activity == "Low":
        calories = 2000
    elif activity == "Moderate":
        calories = 2500
    else:
        calories = 3000

    if goal == "Lose":
        calories -= 500
    elif goal == "Gain":
        calories += 500

    st.subheader("🔥 Daily Calories")
    st.write(f"Recommended Calories: **{calories} kcal/day**")

    st.subheader("✅ Healthy Lifestyle Tips")
    st.write("""
- Eat fruits and vegetables.
- Drink enough water.
- Exercise regularly.
- Sleep 7–8 hours.
- Avoid junk food.
- Include protein in meals.
- Eat on time.
- Reduce stress with yoga or meditation.
""")

import streamlit as st

st.set_page_config(page_title="Diet and Nutrition Advisor", page_icon="🥗")

st.sidebar.title("🥗 About")
st.sidebar.write("AI-powered Diet & Nutrition Advisor")
st.sidebar.success("Developed by B. Vikash Naidu")

st.title("🥗 Diet and Nutrition Advisor Agent")

st.image("https://images.unsplash.com/photo-1490645935967-10de6ba17061", width=700)