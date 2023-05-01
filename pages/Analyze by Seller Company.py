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
    page_icon ="📊",
    layout = "wide"
)

###############################################################################
# starting: "main" page of dashboard
###############################################################################

#############################################
# Data
#############################################
raw_data = pd.read_csv('data/compustat_final.csv')
raw_acct_data = pd.read_csv('data/accounting_final.csv')
#############################################
# Sidebar
#############################################
with st.sidebar:
    st.sidebar.subheader("Seller Company")

    seller = list(raw_data.conm.unique())
    seller_selection = st.sidebar.selectbox(
        "Select Seller Company", seller)
    
    '''
    ---
    [Source code and contributors here.](https://github.com/donbowen/portfolio-frontier-streamlit-dashboard)
    '''


#############################################
# Filtered
#############################################
#compustat data
data = raw_data[raw_data["conm"] == seller_selection]
symbol = data['Symbol'].values[0]

#accounding data
acct = raw_acct_data[raw_acct_data["conm"] == seller_selection]

#############################################
# Header and Info
#############################################
st.write('#', seller_selection, "(", symbol,")")

#############################################
# Plots side by side
#############################################

fig1 = px.pie(data[data["fyear"] == 2019], values='salecs', names='ctype', title='2019')
fig2 = px.pie(data[data["fyear"] == 2022], values='salecs', names='ctype', title='2022')


#####
# LOOK AT DATAFRAME DEMO CODE for reference: https://docs.streamlit.io/library/get-started/multipage-apps/create-a-multipage-app
#####

### now need to tie company into the data selection...

st.header('2019 vs 2022: descriptive thing')
st.write("#### The pie charts below describe the breakdown of (", symbol,")'s sales:")
ctype1, ctype2 = st.columns(2)
ctype3, ctype4, ctype5 = st.columns(3)
st.markdown('- MARKET: add info here') 
st.markdown('- COMPANY: ')
st.markdown('- GEOREG: ') 
st.markdown('- GOVDOM: ') 
st.markdown('- GOVFRN: ')
## two columns
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(fig1, theme="streamlit", use_container_width=True)

with col2:
    st.plotly_chart(fig2, theme="streamlit", use_container_width=True)



# divider line
st.divider() # Draws a horizontal line

### columns with accounting data
## 2019 Rates


## WORK ON METRICS!!!👈 👈 👈 👈 👈  
st.subheader('Analysis:')
col1, col2, col3, col4, col5 = st.columns(5)
with col1: 
    st.metric(label="AP", value=acct.iloc[-1,5], delta=acct.iloc[-1,17]) # make this -1 so it is the last in the dataset

# divider line
st.divider() # Draws a horizontal line

## Raw table
with st.expander("Cleaned DataFrame"):
    '''
    CIK: represents bla bal bal
    '''
    st.table(raw_data)

# Filtered Table
with st.expander("Filtered COMP DataFrame"):
    st.table(data)
with st.expander("Cleaned Acct DataFrame"):
    st.table(raw_acct_data)
with st.expander("Filtered ACCT DataFrame"):
    st.table(acct)



