# myapp/views.py

from django.shortcuts import render
import pandas as pd
import plotly.express as px

def groundwater_map(request):
    # Load the data from CSV
    data = pd.read_csv('state-wise.csv')

    # Assuming 'State Name' is the column containing state names and 'Stage of Goundwater Development (%)' is the column containing the development stage data
    fig = px.choropleth(data,
                        locations='State Name',
                        locationmode='country names',
                        color='Stage of Goundwater Development (%)',
                        hover_name='State Name',
                        color_continuous_scale=px.colors.sequential.Plasma,
                        title='Stage of Groundwater Development in Indian States',
                        scope='asia',  # Adjust the scope as per your requirement
                        )

    fig.update_geos(showcountries=True, countrycolor="Black")  # Add country borders

    # Convert the figure to HTML
    plot_div = fig.to_html(full_html=False, include_plotlyjs=False)

    # Render the template with the plot
    return render(request, 'groundwater_map.html', context={'plot_div': plot_div})
