from django.shortcuts import render
import joblib

def aqi_dashboard(request):
    # Loading XGBoost model (Ensure the .pkl file is in the main project folder)
    model = joblib.load('aqi_xgboost_model.pkl')
    
    # Placeholder for when we connect the live weather data
    predicted_benzene = 2.4 
    
    # Send the prediction to your HTML page
    context = {'prediction': predicted_benzene}
    return render(request, 'dashboard.html', context)

def shikamaru_drag(request):
    # The easter egg view for all irrelevant buttons
    return render(request, 'shikamaru.html')