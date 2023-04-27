#############################################
# Getting started
#############################################
# 1. open this code
# 2. open terminal
# 3. change directory (cd) to this file
# 4. command line: conda activate streamlit-env
# 5.command line streamlit run app.py
# 6. continue code

# if adding new packages to the .py file you MUST also add them to the requirements.txt file
# After doing so update the environment (MUST BE IN THE SAME FOLDER as the prior enviorment)
# Command Line: conda env update --name streamlit-env --file environment.yml --prune

#Note: 
# To activate this environment, use
#
#     conda activate streamlit-env
#
# To deactivate an active environment, use
#
#     conda deactivate


#############################################
# Imports/Page Setup
#############################################
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
import altair as alt

# Page config
st.set_page_config(
    page_title="Mapping Demo",
    page_icon ="📊",
    layout = "wide"
)

###############################################################################
# starting: "main" page of dashboard
###############################################################################
st.markdown(' # MATCH TITLE TO TAB TITLE OR MAKE IT *Overall Seller Distrubution*') 
# below is another way to do the headers/write text can either use """ or ''' before & after the text
#  """
# # Header 1 (can make this a)
# ## subhearder
# """

# below is another another wat to do it
# st.title(' MATCH TITLE TO TAB TITLE OR MAKE IT *Overall Seller Distrubution*') 

#############################################
# Sidebar
#############################################
with st.sidebar:
    '''
    ---
    [Source code and contributors here.](https://github.com/donbowen/portfolio-frontier-streamlit-dashboard)
    '''


#############################################
# Plots side by side
#############################################
## data for the figures 
#raw = pd.read_csv('data/sample.csv')
# # sales for each sector,cytpe, date
# data = raw.groupby(['buyer','seller','year'])['sales'].transform(lambda x: sum(x))
data = pd.read_csv('data/sample.csv')
# data2 = data.query()
fig1 = px.pie(data, values='sales', names='buyer', title='2019')
fig2 = px.pie(data, values='sales', names='buyer', title='2022')

## select box
company = st.selectbox(
    'Select a company:',
    ('A', 'B', 'C'))

st.write('You selected:', company) #do not need


#####
# LOOK AT DATAFRAME DEMO CODE for reference: https://docs.streamlit.io/library/get-started/multipage-apps/create-a-multipage-app
#####

### now need to tie company into the data selection...

st.header('2019 vs 2022: descriptive thing')
## two columns
col1, col2 = st.columns(2)

with col1:
   st.plotly_chart(fig1, theme="streamlit", use_container_width=True)

with col2:
   st.plotly_chart(fig2, theme="streamlit", use_container_width=True)

# divider line
st.divider() # 👈 Draws a horizontal line

### columns with accounting data

st.metric(label="Gas price", value=data.iloc[0,2], delta=-0.5, delta_color="inverse")

# divider line
st.divider() # 👈 Draws a horizontal line

## Raw table
with st.expander("Dataframe for above charts"):
    '''
    ### Dataframe
    '''
    st.table(data)



