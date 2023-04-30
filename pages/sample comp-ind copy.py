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
# st.markdown(' # MATCH TITLE TO TAB TITLE OR MAKE IT *Overall Seller Distrubution*') 
# below is another way to do the headers/write text can either use """ or ''' before & after the text
#  """
# # Header 1 (can make this a)
# ## subhearder
# """

# below is another another wat to do it
# st.title(' MATCH TITLE TO TAB TITLE OR MAKE IT *Overall Seller Distrubution*')

#############################################
# Data
#############################################
raw_data = pd.read_csv('data/test.csv')

'''
# overall site
## describing what is happeing


image at the bootome of the industry breakdown by sales - just form the first csv file
## Industry: bla bla bal
'''
## Goes on the overall page!!!
# ## overall pie chart
# fig0_1 = px.pie(raw_data, values='sales', names='seller', title = "Total Sales from Compustat For each Seller")
# st.plotly_chart(fig0_1, theme="streamlit", use_container_width=True)


st.bar_chart(data = raw_data[raw_data["year"] == 2019], x = 'seller', y = 'sales', use_container_width=True)
# make x the industry

'''
### List of sellers in the industry
if we want we can have to top preformer in the idnstry ??
'''


#############################################
# Sidebar
#############################################
with st.sidebar:
    st.sidebar.subheader("Seller Company")

    seller = list(raw_data.seller.unique())
    seller_selection = st.sidebar.selectbox(
        "Select Seller Company", seller)
    
    '''
    ---
    [Source code and contributors here.](https://github.com/donbowen/portfolio-frontier-streamlit-dashboard)
    '''


#############################################
# Filtered
#############################################
data = raw_data[raw_data["seller"] == seller_selection]
symbol = "SOL"  # make symbol = seler_selection but differernt column in the df (try below code)
# symbol = data['symbol'].values[0]

#############################################
# Header and Info
#############################################
st.write('#', seller_selection, "(", symbol,")")

#############################################
# Plots side by side
#############################################

fig1 = px.pie(data[data["year"] == 2019], values='sales', names='buyer', title='2019')
fig2 = px.pie(data[data["year"] == 2022], values='sales', names='buyer', title='2022')


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
## 2019 Rates

st.metric(label="Gas price", value=data.iloc[-1,3], delta=data.iloc[-1,7]) # make this -1 so it is the last in the dataset

# divider line
st.divider() # 👈 Draws a horizontal line

## Raw table
with st.expander("Raw DataFrame"):
    '''
    CIK: represents bla bal bal
    '''
    st.table(raw_data)

# Filtered Table
with st.expander("Filtered DataFrame"):
    st.table(data)



