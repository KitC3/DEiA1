from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app

layout = [dcc.Markdown("""
#### The Project Goal and Data

The goal of the project is to predict the decommission time of a building in the Netherlands by using open source data. This end product would then be presented as a minimum valuable product (MVP)
for the company New Horizon. 

#### The Data and Evaluation Protocol
All the data that was used is publically available.

BAG: https://www.kadaster.nl/zakelijk/registraties/basisregistraties/bag

CBS: https://www.cbs.nl/nl-nl/dossier/nederland-regionaal/geografische-data/gegevens-per-postcode

Leefbarometer: https://data.overheid.nl/en/dataset/leefbaarometer-2-0

All datasets were preprocesed and the combined resulting in a dataset containing 130,110 buildings. 90% was split into a training set and 10% was left for the test set.

#### Model Selection
Various regression models were run such as simple linear models to ensemble models. The Random Forest Regression model performed the best, when evaluating using the Mean Absolute Error (MAE).

"""),

html.Img(src='https://raw.githubusercontent.com/KitC3/DEiA1/main/dashboard_rest.png')]
