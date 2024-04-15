# myapp/views.py

from django.shortcuts import render
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np

def groundwater_map(request):
    return render(request, 'groundwater_map.html')


# Load the data
data = pd.read_csv('combined.csv')

def perform_linear_regression(state, future_year):
    # Filter data for the given state
    state_data = data[data['State Name'] == state]

    if state_data.empty:
        return {
            'error': f'No data found for state {state}.'
        }

    # Extract features and target
    X = state_data[['Year']]
    y_net_availability = state_data['Net Groundwater Availability']
    y_stage_development = state_data['Stage of Goundwater Development (%)']

    # Initialize linear regression models
    net_availability_model = LinearRegression()
    stage_development_model = LinearRegression()

    # Fit models
    net_availability_model.fit(X, y_net_availability)
    stage_development_model.fit(X, y_stage_development)

    # Predict for the specific future year
    future_net_availability = net_availability_model.predict([[future_year]])
    future_stage_development = stage_development_model.predict([[future_year]])

    return {
        'future_net_availability': future_net_availability[0],
        'future_stage_development': future_stage_development[0]
    }


def prediction(request):
    if request.method == 'POST':
        user_input_state = request.POST.get('state')
        user_input_year = int(request.POST.get('year'))
        prediction_results = perform_linear_regression(user_input_state, user_input_year)
        return render(request, 'prediction.html', {'prediction_results': prediction_results})
    else:
        return render(request, 'prediction.html')