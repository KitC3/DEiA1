from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from joblib import load
import numpy as np
import pandas as pd
import pickle
import io   
import re

from app import app

style = {'padding': '1.5em'}

layout = html.Div([
    dcc.Markdown("""
        ### Predict
        Use the controls below to predict the decommision time, based on the variables elected from the dataset. A string of the data is required.
        
        If applicable the decommission time of a building can also be inputted, to see the performance of the model.

    """),

    html.Div(id='prediction-content', style={'fontWeight': 'bold'}),


    html.Div([
    dcc.Markdown('###### Data Input'),
    dcc.Input(
            id='data_input',
            placeholder="",
            value= """2006.0,1.0,0.0,206.0,0,0,0,0,0,0,0,0,0,0,1,168866.875,438434.25,4041CK,Kesteren,7.0,5670.0,1285.0,810.0,1275.0,855.0,85.0,90.0,0.0,0.0,515.0,590.0,115.0,805.0,2.7,2040.0,195.0,255.0,490.0,195.0,305.0,230.0,260.0,115.0,180.0,60.0,40.0,585.0,85.0,227.0,1560.0,3250.0,40-60 midden,32.7,330.0,480.0,5.0,Nijverheidsweg4.0"""

        ),
    ], style=style),
    
    html.Div([
    dcc.Markdown('###### Decommision Time'),
    dcc.Input(
            id='decommision_time',
            placeholder="",
            value=11
        ),
    ], style=style),


html.Img(src='https://raw.githubusercontent.com/KitC3/DEiA1/main/dashboard_rest.png')])


@app.callback(
    Output('prediction-content', 'children'),
    [Input('data_input', 'value'),
     Input('decommision_time', 'value')])
def predict(data_input, decommision_time):
    col = """bouwjaar,WoningType,NR_CEL,oppervlakte,heeft_bijeenkomst_functie,heeft_cel_functie,heeft_gezondheids_functie,heeft_industrie_functie,heeft_kantoor_functie,heeft_logies_functie,heeft_onderwijs_functie,heeft_overig_functie,heeft_sport_functie,heeft_winkel_functie,heeft_woon_functie,X,Y,post_code,woonplaats,baro,INWONER,INW_014,INW_1524,INW_2544,INW_65PL,GEBOORTE,P_NL_ACHTG,P_WE_MIG_A,P_NW_MIG_A,TOTHH_EENP,TOTHH_MPZK,HH_EENOUD,HH_TWEEOUD,GEM_HH_GR,WONING,WONVOOR45,WON_4564,WON_6574,WON_7584,WON_8594,WON_9504,WON_0514,WON_1524,WON_MRGEZ,P_KOOPWON,P_HUURWON,WON_HCORP,WON_NBEW,WOZWONING,G_GAS_WON,G_ELEK_WON,M_INKHH,P_LINK_HH,UITKMINAOW,OAD,STED,straat_naam_nr"""
    col_names = re.sub("[^\w]", " ",  col).split()
    df = pd.read_csv(io.StringIO(data_input), sep=",", header=None, names = col_names)
    filename = 'model/finalized_model.sav'
    pipeline = pickle.load(open(filename, 'rb'))
    y_pred_log = pipeline.predict(df)
    y_pred = y_pred_log[0]
    
    if float(decommision_time) > 0:
        difference = ((y_pred - float(decommision_time)) / float(decommision_time)) * 100
        if difference < 0:
            results = f'The predicted decomission time is {y_pred:.2f} years which is {difference:.2f}% under the actual decommision time ({decommision_time} years).'
        else:
            results = f'The predicted decomission time is {y_pred:.2f} years which is {difference:.2f}% over the actual decommision time ({decommision_time} years).'
    else:
        results = f'The predicted decomission time is {y_pred:.2f} years.'

    return results
