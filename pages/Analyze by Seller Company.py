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
st.markdown('- MARKET: Sale Types (On-site, Merchant, Sale of equipment, Direct to Consumer, eCommerce, Food, etc.)') 
st.markdown('- COMPANY: Companies (Apple Inc, Wal-Mart Stores Inc, etc.)')
st.markdown('- GEOREG: Geographic Region (United States, International, China, Europe, etc.)') 
st.markdown('- GOVDOM: US Government (US Gov, DOD, Medicaid/Medicare)') 
st.markdown('- GOVFRN: Foreign Government (Europe, Asia Pacific, Middle East, Other)')

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
st.subheader('2022 Values Analysis:')
col1, col2, col3, col4, col5 = st.columns(5)
with col1: 
    st.metric(label="AP", value="$"+str(acct.iloc[-1,5])+' M', delta=acct.iloc[-1,17]) # make this -1 so it is the last in the dataset
    st.metric(label="AT", value="$"+str(acct.iloc[-1,6])+' M', delta=acct.iloc[-1,18]) # make this -1 so it is the last in the dataset
    st.metric(label="CAPX", value="$"+str(acct.iloc[-1,7])+' M', delta=acct.iloc[-1,19]) # make this -1 so it is the last in the dataset
    st.metric(label="COGS", value="$"+str(acct.iloc[-1,8])+' M', delta=acct.iloc[-1,20]) # make this -1 so it is the last in the dataset
    st.metric(label="EPSFX", value="$"+str(acct.iloc[-1,9])+' M', delta=acct.iloc[-1,21]) # make this -1 so it is the last in the dataset
    st.metric(label="GP", value="$"+str(acct.iloc[-1,10])+' M', delta=acct.iloc[-1,22]) # make this -1 so it is the last in the dataset
    st.metric(label="INVT", value="$"+str(acct.iloc[-1,11])+' M', delta=acct.iloc[-1,23]) # make this -1 so it is the last in the dataset
    st.metric(label="NI", value="$"+str(acct.iloc[-1,12])+' M', delta=acct.iloc[-1,24]) # make this -1 so it is the last in the dataset
    st.metric(label="RECT", value="$"+str(acct.iloc[-1,13])+' M', delta=acct.iloc[-1,25]) # make this -1 so it is the last in the dataset
    st.metric(label="SALE", value="$"+str(acct.iloc[-1,14])+' M', delta=acct.iloc[-1,26]) # make this -1 so it is the last in the dataset
    
st.write('describe  what it means ')

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



