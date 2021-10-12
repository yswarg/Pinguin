#!/usr/bin/env python
# coding: utf-8

# # Blogpost case team 10

# In[9]:


#GROUPMEMBERS
#Yswar Gokoel     (500786750)
#Billy Uzel       (500828005)
#Scarlet Hau      (500817271)
#Daan Bouwmeester (500826025)


# # Schiphol API

# In[10]:


import pandas as pd
import requests
import json


# In[11]:


data = []
for i in range(5) :
    
    url = "https://api.schiphol.nl/public-flights/flights?includedelays=false&page=" + str(i) + "&sort=%2BscheduleTime&fromDateTime=2020-12-01T00%3A00%3A00&toDateTime=2020-12-03T00%3A00%3A00&searchDateTimeField=estimatedLandingTime"
    i = i + 1
     
    r = requests.get(url)
    headers = headers = {
      'accept': 'application/json',
	  'resourceversion': 'v4',
      'app_id': '6ec7ae49',
	  'app_key': '0b7a8784dc9b7bd1e7b12d927ff3fab9'}
    response = requests.request('GET', url, headers=headers)
    datatxt = response.text
    dataspl = json.loads(datatxt)
    data = response.json()


# In[12]:


df = pd.DataFrame.from_dict(data['flights'], orient='columns')


# In[13]:


df.head()


# In[14]:


df['aircraftType']


# In[15]:


part1 = pd.DataFrame(dataspl)


# In[16]:


part1.head()


# #### Uitleg en conlusie
# We hebben geprobeerd om data via de API van Schiphol Airport op te halen. Dit heeft ons aardig wat tijd gekost. Als eerste moest er een account aangemaakt wordenn om een API id en API key te krijgen. Dit was uiteindelijk gelukt en we konden toen beginnen met het ophalen van de data. Toen moesten we op de site van Schiphol selecteren van hoeveel dagen we de vlucht informatie wilde verzamelen. Ons plan was om dit te doen van een heel jaar, alleen het was alleen maar mogelijk om dit te doen van 3 dagen. Dus uiteindelijk hebben we gekozen om het te verzamelen van 3 dagen. Totdat we erachter kwamen dat Schiphol het ons nog lastiger had gemaakt. We kwamen erachter dat de API alleen maar 20 resultaten ophaalde.
# 
# Op de site van Schiphol stond hoe we dit konden oplossen. Het kon door middel van de url aan te passen. Dit hebben we vervolgens geprobeerd in een for loop. Uiteindelijk was het wel gelukt om hieruit vervolgens meer dan 20 vluchten te verkrijgen. Maar toen begon het volgende probleem. De data die we hadden opgehaald kwam in dictionairy, waar weer data inzat in een dictionairy, waar nog weer data inzat in een dictionairy. We hebben geprobeerd om deze data overzichtelijk in een dataframe te presenteren. Alleen we kwamen erachter dat dit echt niet zo makkelijk ging. We hebben heel het internet afgezocht naar oplossingen voor het probleem, maar we kwamen er echt niet meer uit.
# 
# Uiteindelijk op woensdag middag, minder dan 24 uur voor de deadline, hebben we als groep besloten dat het niet gaat werken met de API van Schiphol. We baalden daar echt van omdat we al onze tijd gericht hadden op deze API. We hebben gekozen om een csv bestand van datacamp te downloaden en hiermee toch geprobeerd een blogpost mee te maken.

# # Penguins dataset

# ### Importing data and packages

# In[17]:


import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().system('pip install plotly==5.3.1')
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# In[18]:


#Dataset afkomstig van Datacamp
penguins = pd.read_csv('penguins.csv')


# ### Inspecting data

# In[19]:


penguins.head()


# In[20]:


penguins.info()


# In[21]:


penguins.nunique()


# In[22]:


penguins['Island'].value_counts(normalize = True).sort_index()


# In[23]:


penguins['Sex'].value_counts(normalize = True).sort_index()


# In[24]:


#penguins.dropna(inplace=True)
#penguins.info()


# In[25]:


penguins.describe()


# #### Conclusie dataverkenning
# Na het inspecteren van de data met verschillende functies, is er besloten de dataset te laten zoals deze is. Met het verwijderen van 'Na values' worden ook bruikbare values verwijderd. Hierop word zeer weinig data overgehouden. 

# ### Analyzing data true visuals

# #### Culmen ratio

# In[26]:


penguins['CulmenRatio'] = penguins['Culmen Length (mm)'] / penguins['Culmen Depth (mm)']


# In[27]:


penguins['CulmenRatio'].mean()


# In[28]:


fig, axes = plt.subplots()
sns.boxplot(x="Island", y="CulmenRatio", data=penguins).set(title="Relation between CulmenRatio and Island")


# #### Correlation in a heatmap

# In[29]:


penguins[["Body Mass (g)", "Culmen Length (mm)", 'Culmen Depth (mm)', 'Flipper Length (mm)']].corr()


# In[30]:


sns.heatmap(penguins[["Body Mass (g)", "Culmen Length (mm)", 'Culmen Depth (mm)', 'Flipper Length (mm)']].corr(), annot=True, cmap = 'Greens')
plt.show()


# Aan de hand van de heatmap van geconcludeerd worden dat de corelatie tussen body mass en flipper length het sterkt is. Hier zullen wij een voorspellend model van maken.

# #### Slider

# In[31]:


fig = go.Figure()
for island in ['Torgersen', 'Biscoe', 'Dream']:
    df = penguins[penguins.Island == island]
    fig.add_trace(go.Scatter(
        x=df["Culmen Length (mm)"],
        y=df["Culmen Depth (mm)"],
        mode='markers',
        name=island))

    
sliders = [
    {'steps':[
    {'method': 'update', 'label': 'Torgensen', 'args': [{'visible': [True, False, False]}]},
    {'method': 'update', 'label': 'Biscoe', 'args': [{'visible': [False, True, False]}]},
    {'method': 'update', 'label': 'Dream', 'args': [{'visible': [False, False, True]}]}]}]
fig.data[0].visible=False
fig.data[1].visible=False
fig.update_layout({'sliders': sliders},
                   xaxis_title='Culmen Length (mm)',
                   yaxis_title="Culmen Depth (mm)",
                   title = 'Relation between culmen length and depth')
fig.show()


# In deze slider visualisatie is de relatie tussen de snavel lengte en snavel diepte te zien op basis van het eiland van de pinguïns. Op het eiland Torgensen is te zien dat de verschillende waarnemingen een grote variatie hebben. Op eiland Biscoe is juist te zien dat er 2 soorten groepen zijn met waarnemingen die dicht bij elkaar liggen. Dit zou bijvoorbeeld kunnen liggen aan de verschillende soorten pinguïns op dit eiland. Als laatste op eiland Dream liggen de waarnemingen ook verspreid over het hele figuur. Als conclusie kunnen we hieruit trekken dat er niet echt een relatie zit tussen de snavellengte en diepte per eiland.

# #### Dropdown menu

# In[32]:


fig = go.Figure()
for island in ['Torgensen', 'Biscoe', 'Dream']:    
    df = penguins[penguins.Island == island]    
    fig.add_trace(go.Scatter(
        x=df["Culmen Length (mm)"], 
        y=df["Culmen Depth (mm)"],
        mode='markers',
        name=island))
    
dropdown_buttons = [  
    {'label': 'Torgensen', 'method': 'update',
     'args': [{'visible': [True, False, False]},           
        {'title': 'Torgensen'}]},  
    {'label': 'Biscoe', 'method': 'update',
     'args': [{'visible': [False, True, False]},          
        {'title': 'Biscoe'}]},  
    {'label': "Dream", 'method': "update",
     'args': [{"visible": [False, False, True]},          
        {'title': 'Dream'}]}]


fig.update_layout(
    {
    'updatemenus':[{
        'type': "dropdown",
        'x': 1.3,'y': 0.5,
        'showactive': True,
        'active': 0,
        'buttons': dropdown_buttons}]},
     xaxis_title='Culmen Length (mm)',
     yaxis_title="Culmen Depth (mm)",
     title = 'Relation between culmen length and depth')

fig.show()


# De dropdown visualisatie is helaas niet helemaal gelukt zoals we dat gehoopt hadden. Het figuur geeft niet precies de juiste data die bij de dropdown knop hoort. Het tweede tabblad van Biscoe en derde tabblad van Dream kloppen wel, alleen de Torgenson data presenteert het figuur niet juist.
# 

# #### Checkboxes

# In[33]:


fig = px.scatter(data_frame=penguins, x='Species', y='Flipper Length (mm)', color='Species')

my_buttons = [{'label': "Scatterplot", 'method': "update", 'args': [{"type": 'scatter'}]},
  {'label': "Boxplot", 'method': "update", 'args': [{"type": 'box', 'mode': 'markers'}]}]

fig.update_layout({
    'updatemenus': [{
      'type':'buttons','direction': 'down',
      'x': 1.3,'y': 0.5,
      'showactive': True, 'active': 0,
      'buttons': my_buttons}]})
fig.show()


# In tegenstelling tot de dropdown visualisatie, klopt de checkbox visualisatie wel. In deze visualisatie is de relatie te zien tussen de vleugellengte en pinguïnsoort te zien. Allereerst is de vleugellengte van de verschilende pinguïnsoorten te zien in de boxplot. We zien dat de Gentoo over het algemeen grotere vleugels hebben dan de andere soorten. De IQR van alle soorten is ongeveer hetzelfde, maar de spreiding bij de Adelie soort is het grootste van de soorten. De mediaan van de Adelie ligt op 190 mm, bij Chinstrap is dit 196 mm en bij de Gentoo is dit 216 mm. Deze resultaten zeggen niet persee iets over alle vogels, want het kan ook zijn dat er een Adelie of Chinstrap pinguïnsoort is met grotere vleugels dan de Gentoo soort.

# ### Predictive model

# #### Relation between weight and flipperlength

# In[34]:


fig = px.scatter(data_frame=penguins,
                x='Body Mass (g)',
                y='Flipper Length (mm)',
                color='Species',
                trendline='ols',
                labels={'species':'Pinguïnsoort', 'body_mass_g':'Gewicht in gram (g)', 'flipper_length_mm':'Vleugel lengte in milimeter (mm)'}, 
                height=600,
                width=1000, 
                title='Relatie tussen gewicht en vleugel grootte per pinguïnsoort')
                
fig.show()


# #### Uitleg en conclusie predictive model
# Het voorspelmodel wat we gemaakt hebben is een voorspelling van de vleugelgrootte op basis van het gewicht van de pinguïns, per pinguïnsoort. De formule per soort is:
# 
# - Adelie: Vleugelgrootte = 165.245 + (0.00667687 * Gewicht in gram)
# - Gentoo: Vleugelgrootte = 171.304 + (0.00903914 * Gewicht in gram)
# - Chinstrap: Vleugelgrootte = 151.381 + (0.0119051 * Gewicht in gram)
# 
# Op basis van deze formules kan dus de vleugelgrootte berekend worden. Helaas is dit de enige voorspelling die we hebben kunnen doen. Dit is het gevolg van tijdsgebrek

# In[ ]:




