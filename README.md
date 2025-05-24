# Indonesian Food Recommender 🍛

This is a **rule-based expert system** built with **Streamlit** that recommends Indonesian dishes based on selected ingredients and confidence levels. The knowledge behind this system was sourced directly from an expert in Indonesian cuisine.

## 🧠 About the System

The app uses the **Certainty Factor (CF)** method to handle user uncertainty regarding the use of key ingredients such as:
- Onion
- Coconut Milk
- Red Chili

Based on those inputs, the system will:
1. Infer the **type of dish** (e.g., Curry, Spicy, Incomplete).
2. Recommend a specific **Indonesian dish** (e.g., Gulai Ayam, Ayam Balado).
3. Provide **confidence levels** for both the dish type and recommendation.

## 📦 Features

- Interactive ingredient selection.
- Confidence level sliders based on user knowledge.
- Inference engine using if-then rules and CF.
- Recommendations include classic Indonesian dishes like:
  - **Gulai Ayam**
  - **Gulai Daging Sapi**
  - **Ayam Balado**
  - **Gulai Telur**, etc.

## 🛠️ Tech Stack

- **Python 3**
- **Streamlit** for UI
- **Rule-based Expert System** with Certainty Factor logic

## 🚀 Getting Started

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/indonesian-food-recommender.git
   cd indonesian-food-recommender
   ```
2. Install dependencies:
   ```bash
   pip install streamlit
   ```
3. Run the app:
   ```bash
   streamlit run app.py
   ```

## Example Use

Users are asked:
  - Whether the dish uses Onion, Coconut Milk, and Red Chili.
  - How confident they are in their choices.
  - The app then processes the inputs and outputs a recommended Indonesian dish with the reasoning and associated confidence levels.

## Knowledge base

This system is built with rules derived from the knowledge of a real culinary expert, not from AI training or datasets. That makes it interpretable, traceable, and trustworthy in traditional recipe contexts.

## Notes

  - Currently supports 4 main ingredients: Chicken, Beef, Egg, Fish.
  - More ingredients and rule complexity can be added for future expansion.

Made with ❤️ for Indonesian cuisine and expert systems.
