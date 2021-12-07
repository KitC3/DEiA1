from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app



layout = [
    
dcc.Markdown("""
### Introduction
Welcome to the Dashboard of the Decommission Time Predictor of buildings in the Netherlands from New Horizon, made by group 9.

This web app enables the user to determine the predicted decommission time of a building.
The predicted decommission time is based on historical data from the BAG (Basisregistratie Adressen en Gebouwen) dataset and socio-economic data from the CBS (Centraal Bureau voor de Statistiek).
"""),

html.Img(src='https://raw.githubusercontent.com/KitC3/DEiA1/main/dashboard_intro.png')]
