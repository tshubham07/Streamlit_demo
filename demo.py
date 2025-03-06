import streamlit as st

def get_diet_plan(weight):
    if weight < 50:
        return "High-protein diet with healthy fats and complex carbs. Include nuts, dairy, and lean meats."
    elif 50 <= weight < 70:
        return "Balanced diet with moderate protein, fiber-rich foods, and plenty of fruits and vegetables."
    elif 70 <= weight < 90:
        return "Low-carb diet with lean proteins, whole grains, and controlled portion sizes."
    else:
        return "Low-calorie, high-fiber diet with focus on lean proteins and plenty of hydration. Avoid processed foods."

def main():
    st.title("Personalized Diet Plan")
    
    name = st.text_input("Enter your name")
    mobile = st.text_input("Enter your mobile number")
    age = st.number_input("Enter your age", min_value=1, max_value=100)
    height = st.number_input("Enter your height (cm)", min_value=50, max_value=250)
    weight = st.number_input("Enter your weight (kg)", min_value=20, max_value=200)
    
    if st.button("Get Diet Plan"):
        if name and mobile and age and height and weight:
            diet_plan = get_diet_plan(weight)
            st.subheader(f"Diet Plan for {name}")
            st.write(diet_plan)
        else:
            st.warning("Please fill in all details correctly.")

if __name__ == "__main__":
    main()
