import streamlit as st

st.title("Indonesian Food Recommender 🇮🇩🍛")

cf_map = {
    "Very Uncertain": 0.1,
    "Uncertain": 0.3,
    "Maybe": 0.5,
    "Certain": 0.7,
    "Very Certain": 0.9
}

# Convert CF value to verbal level
def verbal_cf(cf):
    if cf < 0.2:
        return "Very Uncertain"
    elif cf < 0.4:
        return "Uncertain"
    elif cf < 0.6:
        return "Maybe"
    elif cf < 0.8:
        return "Certain"
    else:
        return "Very Certain"

# User input
onion = st.selectbox("Does it use Onion?", ["Yes", "No"])
cf_onion_verbal = st.selectbox("How sure are you about the Onion choice?", list(cf_map.keys()))
cf_onion = cf_map[cf_onion_verbal]

coconut_milk = st.selectbox("Does it use Coconut Milk?", ["Yes", "No"])
cf_coconut_verbal = st.selectbox("How sure are you about the Coconut Milk choice?", list(cf_map.keys()))
cf_coconut = cf_map[cf_coconut_verbal]

red_chili = st.selectbox("Does it use Red Chili?", ["Yes", "No"])
cf_chili_verbal = st.selectbox("How sure are you about the Red Chili choice?", list(cf_map.keys()))
cf_chili = cf_map[cf_chili_verbal]

main_ingredient = st.selectbox("Choose Main Ingredient:", ["Chicken", "Beef", "Egg", "Fish"])

# Inference: Dish Type + CF
dish_type = None
cf_dish_type = 0.0

if onion == "No":
    dish_type = "Incomplete"
    cf_dish_type = cf_onion * 1.0  # Rule 4
elif onion == "Yes" and coconut_milk == "Yes":
    dish_type = "Curry"
    cf_dish_type = min(cf_onion, cf_coconut) * 0.8  # Rule 1
elif onion == "Yes" and red_chili == "Yes" and coconut_milk == "No":
    dish_type = "Spicy"
    cf_dish_type = min(cf_onion, cf_chili, cf_coconut) * 0.9  # Rule 2
elif onion == "Yes" and red_chili == "No" and coconut_milk == "No":
    dish_type = "Incomplete"
    cf_dish_type = min(cf_onion, cf_chili, cf_coconut) * 0.7  # Rule 3

# Inference: Recommendation + CF
recommendation = None
cf_recommendation = 0.0

if dish_type == "Curry":
    if main_ingredient == "Chicken":
        recommendation = "Gulai Ayam"
        cf_recommendation = cf_dish_type * 0.95
    elif main_ingredient == "Beef":
        recommendation = "Gulai Daging Sapi"
        cf_recommendation = cf_dish_type * 0.95
    elif main_ingredient == "Egg":
        recommendation = "Gulai Telur"
        cf_recommendation = cf_dish_type * 0.9
    elif main_ingredient == "Fish":
        recommendation = "Gulai Ikan"
        cf_recommendation = cf_dish_type * 0.9
elif dish_type == "Spicy":
    if main_ingredient == "Chicken":
        recommendation = "Ayam Balado"
        cf_recomm_


# Show result
if st.button("Process"):
    st.subheader("Inference Result")
    st.write(f"**Dish Type:** {dish_type}")
    st.write(f"**Dish Type Confidence Level:** {verbal_cf(cf_dish_type)}")
    st.write(f"**Recommendation:** {recommendation}")
    st.write(f"**Recommendation Confidence Level:** {verbal_cf(cf_recommendation)}")
