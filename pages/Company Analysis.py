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
    page_title="Project - Sunset",
    page_icon ="🌅",
    layout = "wide"
)

###############################################################################
# Starting: "main" page of dashboard
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
    st.sidebar.subheader("Company Analysis")

    seller = list(sorted(raw_data['conm'].unique()))
    seller_selection = st.sidebar.selectbox(
        "Select Company (Seller)", seller)

#############################################
# Filtered
#############################################
### compustat data
data = raw_data[raw_data["conm"] == seller_selection]

# from the filtered data, getting values from the datafame 
symbol = data['Symbol'].values[0]
Industry = data['GICS Sector'].values[0]
SubIndustry = data['GICS Sub-Industry'].values[0]
HeadQ= data['Headquarters Location'].values[0]
Founded = data['Founded'].values[0]

### accounding data
acct = raw_acct_data[raw_acct_data["conm"] == seller_selection]

#############################################
# Header and Info
#############################################
st.title("Company Analysis")
st.write('##', seller_selection, "(", symbol,")")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.write('**Industry:** ',Industry)
with col2:
    st.write('**Sub-Industry:** ',SubIndustry)
with col3:
    st.write('**Headquarters Location:** ',HeadQ)
with col4:
    st.write('**Date Founded:** ',Founded)

#############################################
# Plots side by side
#############################################
### making the plots
fig1 = px.pie(data[data["fyear"] == 2019], values='salecs', names='ctype', title='2019')
fig2 = px.pie(data[data["fyear"] == 2022], values='salecs', names='ctype', title='2022')

### plotting the plots
st.write("#### Breakdown of ", symbol,"'s sales")
## two columns
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(fig1, theme="streamlit", use_container_width=True)

with col2:
    st.plotly_chart(fig2, theme="streamlit", use_container_width=True)

### describing the plots
col1, col2 = st.columns(2)
with col1:
    st.markdown('- **MARKET**: Sale Types (On-site, Merchant, Sale of equipment, Direct to Consumer, eCommerce, Food, etc.)') 
    st.markdown('- **COMPANY**: Companies (Apple Inc, Wal-Mart Stores Inc, etc.)')
with col2:
    st.markdown('- **GEOREG**: Geographic Region (United States, International, China, Europe, etc.)') 
    st.markdown('- **GOVDOM**: US Government (US Gov, DOD, Medicaid/Medicare)') 
    st.markdown('- **GOVFRN**: Foreign Government (Europe, Asia Pacific, Middle East, Other)')

# divider line
st.divider() # Draws a horizontal line

#############################################
# Accounting Data
#############################################
### if have 2022 Accounting data
if pd.notna(acct.iloc[-1,14]):  # looking at the cell value
    st.subheader('2022 Accounting Data')

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1: 
        st.metric(label="Net Sales [sale]", value="$"+str(acct.iloc[-1,14])+' M', delta=acct.iloc[-1,26]) # make this -1 so it is the last in the dataset
        st.metric(label="Total Receivables [rect]", value="$"+str(acct.iloc[-1,13])+' M', delta=acct.iloc[-1,25]) # make this -1 so it is the last in the dataset


    with col2: 
        st.metric(label="Cost of Goods Sold [cogs]", value="$"+str(acct.iloc[-1,8])+' M', delta=acct.iloc[-1,20]) # make this -1 so it is the last in the dataset
        st.metric(label="Accounts Payable - Trade [ap]", value="$"+str(acct.iloc[-1,5])+' M', delta=acct.iloc[-1,17]) # make this -1 so it is the last in the dataset

    with col3:
        st.metric(label="Gross Profit [gp]", value="$"+str(acct.iloc[-1,10])+' M', delta=acct.iloc[-1,22]) # make this -1 so it is the last in the dataset
        st.metric(label="Total Inventories [invt]", value="$"+str(acct.iloc[-1,11])+' M', delta=acct.iloc[-1,23]) # make this -1 so it is the last in the dataset

    with col4:  
        st.metric(label="Net Income (Loss) [ni]", value="$"+str(acct.iloc[-1,12])+' M', delta=acct.iloc[-1,24]) # make this -1 so it is the last in the dataset
        st.metric(label="Total Assets [at]", value="$"+str(acct.iloc[-1,6])+' M', delta=acct.iloc[-1,18]) # make this -1 so it is the last in the dataset

    with col5: 
        st.metric(label="Earnings Per Share (Basic) [epsfx]", value="$"+str(acct.iloc[-1,9])+' M', delta=acct.iloc[-1,21]) # make this -1 so it is the last in the dataset
        st.metric(label="Capital Expenditures [capx]", value="$"+str(acct.iloc[-1,7])+' M', delta=acct.iloc[-1,19]) # make this -1 so it is the last in the dataset

    st.write('***Note:** The numbers in green/red show the percent change from 2019 to 2022*')


### if do NOT have 2022 Accounting data, use the 2019 accounting data
if pd.isna(acct.iloc[-1,14]):  # looking at the cell value
    st.subheader('2019 Accounting Data')

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1: 
        st.metric(label="Net Sales [sale]", value="$"+str(acct.iloc[0,14])+' M') # make this 0 so it is the first in the dataset
        st.metric(label="Total Receivables [rect]", value="$"+str(acct.iloc[0,13])+' M') # make this 0 so it is the first in the dataset

    with col2: 
        st.metric(label="Cost of Goods Sold [cogs]", value="$"+str(acct.iloc[0,8])+' M') # make this 0 so it is the first in the dataset
        st.metric(label="Accounts Payable - Trade [ap]", value="$"+str(acct.iloc[0,5])+' M') # make this 0 so it is the first in the dataset

    with col3:
        st.metric(label="Gross Profit [gp]", value="$"+str(acct.iloc[0,10])+' M') # make this 0 so it is the first in the dataset
        st.metric(label="Total Inventories [invt]", value="$"+str(acct.iloc[0,11])+' M') # make this 0 so it is the first in the dataset

    with col4:  
        st.metric(label="Net Income (Loss) [ni]", value="$"+str(acct.iloc[0,12])+' M') # make this 0 so it is the first in the dataset
        st.metric(label="Total Assets [at]", value="$"+str(acct.iloc[0,6])+' M') # make this 0 so it is the first in the dataset

    with col5: 
        st.metric(label="Earnings Per Share (Basic) [epsfx]", value="$"+str(acct.iloc[0,9])+' M') # make this 0 so it is the first in the dataset
        st.metric(label="Capital Expenditures [capx]", value="$"+str(acct.iloc[0,7])+' M') # make this 0 so it is the first in the dataset
    
    st.write('***Note:** There is no accounting data for 2022 for this company*')

# divider line
st.divider() # Draws a horizontal line

#############################################
# DataFrames
#############################################
st.subheader('DataFrames')

# DataFrames
with st.expander("Compustat DataFrame for Selected Company "):
    st.table(data)

with st.expander("Accounting DataFrame for Selected Company "):
    st.table(acct)



