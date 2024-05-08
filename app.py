import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_squared_error
import joblib

# Load survival rate prediction model
survival_rate_model = joblib.load('C:/Users/ahmad.wicaksana/Downloads/Data/survival_rate_model.pkl')

# Load ABW prediction model
abw_model = joblib.load('C:/Users/ahmad.wicaksana/Downloads/Data/average_weight_prediction_model.pkl')

# Load biomass prediction model
biomass_model = joblib.load('C:/Users/ahmad.wicaksana/Downloads/Data/biomass.pkl')

# Load revenue prediction model
revenue_model = joblib.load('C:/Users/ahmad.wicaksana/Downloads/Data/revenue.pkl')

# Streamlit app
def main():
    st.title("Shrimp Farming Prediction App")
    
    # Sidebar navigation
    page = st.sidebar.selectbox("Select a model", ["Survival Rate", "Average Body Weight (ABW)", "Biomass", "Revenue"])
    
    if page == "Survival Rate":
        st.header("Survival Rate Prediction")
        # Input form for survival rate prediction
        total_seed = st.number_input("Enter seed", value=100)
        total_fasting_days = st.number_input("Enter fasting", value=100)
        total_feed_given = st.number_input("Enter total feed", value=500)
        cultivation_duration = st.number_input("Enter duration of cultivation cycle", value=60)
        data = [[total_fasting_days, total_feed_given, cultivation_duration, total_seed]]
        prediction = survival_rate_model.predict(data)
        st.write("Predicted survival rate:", prediction)
    
    elif page == "Average Body Weight (ABW)":
        st.header("ABW Prediction")
        # Input form for ABW prediction
        water_quality_index = st.number_input("Enter water quality index", value=100)
        feed_temp_interaction = st.number_input("Enter feed quantity", value=500)
        duration_days = st.number_input("Enter duration ", value=60)
        prev_cycle_avg_weight = st.number_input("Enter weight", value=1000)
        data = [[water_quality_index, feed_temp_interaction, duration_days, prev_cycle_avg_weight]]
        prediction = abw_model.predict(data)
        st.write("Predicted ABW:", prediction)
    
    elif page == "Biomass":
        st.header("Biomass Prediction")
        # Input form for biomass prediction
        duration_days = st.number_input("Enter duration", value=60)
        total_feed_kg = st.number_input("Enter total feed", value=1000)
        morning_temperature = st.number_input("Enter morning temp", value=100)
        evening_temperature = st.number_input("Enter evening temp)", value=100)
        morning_do = st.number_input("Enter data)", value=500)
        evening_do = st.number_input("Enter data", value=60)
        morning_pH = st.number_input("Enter data", value=100)
        morning_salinity = st.number_input("Enter data", value=100)
        evening_salinity = st.number_input("Enter data", value=100)
        evening_pH = st.number_input("Enter data", value=100)
        area = st.number_input("Enter data", value=100)
        data = [[duration_days, total_feed_kg, morning_temperature, evening_temperature, morning_do, evening_do, morning_salinity,
                 evening_salinity, morning_pH, evening_pH, area]]
        prediction = biomass_model.predict(data)
        st.write("Predicted biomass:", prediction)
    
    elif page == "Revenue":
        st.header("Revenue Prediction")
        # Input form for revenue prediction
        cycle_duration = st.number_input("Enter data", value=100)
        shrimp_growth_rate = st.number_input("Enter data", value=100)
        feeding_rate = st.number_input("Enter data", value=100)
        area = st.number_input("Enter data", value=100)
        size = st.number_input("Enter data", value=100)
        weight = st.number_input("Enter data", value=100)
        data = [[cycle_duration, shrimp_growth_rate, feeding_rate, area, size, weight]]
        prediction = revenue_model.predict(data)
        st.write("Predicted revenue:", prediction)

if __name__ == "__main__":
    main()
