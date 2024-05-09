# Shrimp Farming Predictive Modeling Service

## Overview

This service provides predictive modeling for shrimp farming, focusing on forecasting survival rate, average body weight of shrimp, biomass, and revenue. The predictive models are trained using historical data and can be used to make forecasts for ongoing or upcoming cultivation cycles.

## Features

1. **Data Completeness Evaluation**: Assess the completeness of input data to ensure accurate predictions.
   
2. **Survival Rate and Average Growth Rate Calculation**: Calculate survival rate and average daily growth rate (ADG) of shrimp per cultivation cycle to understand farming performance.

3. **Predictive Modeling**:
   - **Survival Rate Forecast**: Predict survival rate (in percentage) for the end of cultivation or at a specified point of cultivation.
   - **Average Body Weight Forecast**: Forecast the average body weight of shrimp (in grams) at the end of cultivation.
   - **Biomass Forecast**: Estimate the biomass of shrimp (in kilograms) at the end of cultivation.
   - **Revenue Forecast**: Predict the revenue value of harvested shrimp based on forecasted weight and market price.

4. **Deployment**:
   - **Feature Store**: Store engineered features that were used during model development for future reference.
   - **Source Code**: The source code is available on GitHub, along with clear instructions for setting up the service.
   - **API Documentation**: Detailed documentation on how to make API requests to access the predictive modeling service.

## API Documentation

## Setting Up the Service

1. **Clone the Repository**: Clone the GitHub repository containing the source code.

   ```bash
   git clone https://github.com/wicaksatya/shrimp.git
   
2. **Access streamlit**: CStart the Streamlit app to deploy the service locally.

   ```bash
   streamlit run app.py
