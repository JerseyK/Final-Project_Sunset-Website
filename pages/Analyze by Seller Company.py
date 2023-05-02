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
    page_title="Analyze by Seller Company",
    page_icon ="🌅",
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
st.write('##', seller_selection, "(", symbol,")")

#############################################
# Plots side by side
#############################################

fig1 = px.pie(data[data["fyear"] == 2019], values='salecs', names='ctype', title='2019')
fig2 = px.pie(data[data["fyear"] == 2022], values='salecs', names='ctype', title='2022')

### now need to tie company into the data selection...
st.write("#### The pie charts below describe the breakdown of (", symbol,")'s sales:")

## two columns
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(fig1, theme="streamlit", use_container_width=True)

with col2:
    st.plotly_chart(fig2, theme="streamlit", use_container_width=True)




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

### columns with accounting data
## 2019 Rates


## WORK ON METRICS!!!👈 👈 👈 👈 👈  
st.subheader('2022 Accounting Data:')

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
    st.metric(label="Earnings Per Share (Basic)", value="$"+str(acct.iloc[-1,9])+' M', delta=acct.iloc[-1,21]) # make this -1 so it is the last in the dataset
    st.metric(label="Capital Expenditures", value="$"+str(acct.iloc[-1,7])+' M', delta=acct.iloc[-1,19]) # make this -1 so it is the last in the dataset

st.write('describe  what it means ')



# divider line
st.divider() # Draws a horizontal line

## Raw table
# with st.expander("Cleaned DataFrame"):
#     '''
#     CIK: represents bla bal bal
#     '''
#     st.table(raw_data)

# Filtered Table
with st.expander("Filtered Compustat DataFrame"):
    st.table(data)
# with st.expander("Cleaned Acct DataFrame"):
#     st.table(raw_acct_data)
with st.expander("Filtered Accounting DataFrame"):
    st.table(acct)



