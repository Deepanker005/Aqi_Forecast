# Real-Time Air Quality (AQI) Forecaster

A multivariate time-series forecasting web application that predicts atmospheric Benzene (C6H6) concentrations using historical meteorological data. 

## Overview
This project analyzes sensor responses from a significantly polluted urban area to predict future air quality levels. The machine learning pipeline handles raw, missing sensor data via linear interpolation and utilizes an XGBoost regressor to model the nonlinear relationships between temperature, absolute humidity, and non-methane hydrocarbon sensor readings.

The frontend is built with Django, featuring a clean, minimalist UI with a flat vector aesthetic and a muted pastel color palette.

## Tech Stack
* **Machine Learning:** Python, XGBoost, Pandas, NumPy, Scikit-Learn
* **Web Framework:** Django
* **Data Visualization:** Matplotlib (Forecast and Feature Importance)
* **Frontend:** HTML5, CSS3 (CSS Grid/Flexbox)

## Key Features
* **Multivariate Forecasting:** Achieved a Root Mean Squared Error (RMSE) of 0.29 µg/m³ by shifting from univariate auto-regression to an XGBoost model utilizing `PT08.S2(NMHC)` sensor data.
* **Production-Ready Data Cleaning:** Replaced default mean imputation with time-series linear interpolation to preserve the temporal integrity of missing sensor blocks.
* **Technical UI Implementation:** A responsive, borderless dashboard design translating raw chemical concentrations into actionable public health insights.
* **Scope Management:** Non-essential navigation routes are intentionally redirected to a custom 404 "Shikamaru" easter egg page to maintain project focus and scope.

## How to Run Locally
1. Clone the repository:
   `git clone https://github.com/[Your-Username]/[Your-Repo-Name].git`
2. Navigate to the project directory:
   `cd "AQI Forecast"`
3. Create and activate a virtual environment:
   `python -m venv venv`
   `source venv/Scripts/activate` (Windows)
4. Install dependencies:
   `pip install -r requirements.txt`
5. Run the local Django server:
   `python manage.py runserver`
6. Access the dashboard at `http://127.0.0.1:8000`
