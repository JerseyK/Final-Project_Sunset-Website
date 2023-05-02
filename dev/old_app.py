#############################################
# Getting started
#############################################
# 1. open this code
# 2. open terminal
# 3. change directory (cd) to this file
# 4. if already have venv:
#       command line: conda activate streamlit-env
#    if not, need to activate the environment:
#       command line: conda env create -f environment.yml
#       command line: conda activate streamlit-env
# 5. command line: streamlit run app.py
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

## TO MAKE PAGES:
# make a folder called "pages" w/i the repo and then pages will be created automatically

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
    page_title="Hello",
    page_icon = "📊",
)

###############################################################################
# starting: "main" page of dashboard
###############################################################################
st.markdown('# MATCH TITLE TO TAB TITLE OR MAKE IT *Overall Seller Distrubution*') 
# below is another way to do the headers/write text can either use """ or ''' before & after the text
#  """
# # Header 1 (can make this a)
# ## subhearder
# """

#############################################
# Plots side by side
#############################################
## data for the figures 
data = pd.read_csv('data/result.csv')
fig1 = px.pie(data, values='%', names='Sell', title='MAKE A NEW TITLE HERE')
fig2 = px.pie(data, values='%', names='Sell', title='MAKE A NEW TITLE HERE')


## two columns
col1, col2 = st.columns(2)

with col1:
   st.header("2019")
   st.plotly_chart(fig1, theme="streamlit", use_container_width=True)

with col2:
   st.header("2022")
   st.plotly_chart(fig2, theme="streamlit", use_container_width=True)

# divider line
st.divider() # 👈 Draws a horizontal line

st.metric(label="Gas price", value=data['%'], delta=-0.5,
    delta_color="inverse")

## Raw table
st.table(data)

###############################################################################


###############################################################################


#############################################
# start: plot
#############################################

