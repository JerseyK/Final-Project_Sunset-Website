#############################################
# Getting started
############################################# 
# 1. Open this code
# 2. Open terminal
# 3. Change directory (cd) to this file
# 4. Command Line: conda activate streamlit-env
#            To create ENV :: Command Line: conda env create -f environment.yml
# 5. Command Line streamlit run Welcome.py
# 6. Continue coding!

# Note: 
# To activate this environment, use
#
#     conda activate streamlit-env
#
# To deactivate an active environment, use
#
#     conda deactivate


### Adding New Packages:
# if adding new packages to the .py file you MUST also add them to the requirements.txt file
# After doing so update the environment (MUST BE IN THE SAME FOLDER as the prior environment)
# Command Line: conda env update --name streamlit-env --file environment.yml --prune


### Creating Pages:
# - Create a folder called `pages` &  add other `.py` files there
#   - This file is the main file and should NOT be in the `pages` folder
# - The name of the `.py` files is what the "page" will be titled in the sidebar
# for more detail visit: https://docs.streamlit.io/library/get-started/multipage-apps/create-a-multipage-app

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
'''
# Impact of COVID-19 on Supply Chain from a Financial Perspective
The COVID-19 pandemic has had a significant impact on the global economy and disrupted supply chains across various industries. As a result, we conducted an analysis of the financial factors affecting several companies. We focused on companies that are in the S&P 500 as of 2022 and used data from financial reports in 2019 and 2022 to gain insights into how the pandemic has affected their financial performance.

#### Initial Hypotheses
1. The amount of technology based companies would increase in 2022. 
2. The amount of contracts involving healthcare/pharmaceutical companies would also increase. 


## Industry Analysis
The Global Industry Classification Standard (GICS) comprises 11 sectors that provide a comprehensive framework for organizing companies based on their primary business activities. However, after cleaning our data to compare the changes between 2019 and 2022, we found that only 8 sectors remained: **Materials**, **Industrials**, **Consumer Discretionary**, **Consumer Staples**, **Health Care**, **Financials**, **Information Technology**, and **Communication Services**. These sectors will be the focus of our analysis to gain insights into the changing trends and performance of companies within these industries.

### Comparing 2019 and 2022 industry sales (`salecs`)

'''
#############################################
# Data
#############################################
raw_data = pd.read_csv('data/compustat_final.csv')
data_2019 = raw_data[raw_data["fyear"] == 2019]
data_2022 = raw_data[raw_data["fyear"] == 2022]

#############################################
# Charts & Tables/DataFrames
#############################################
### creating the charts
chart_2019 = alt.Chart(data_2019).mark_bar().encode(
    y=alt.Y('salecs', scale=alt.Scale(domain=[0, 1600000])),
    x=alt.X('GICS Sector'))

chart_2022 = alt.Chart(data_2022).mark_bar().encode(
    y=alt.Y('salecs', scale=alt.Scale(domain=[0, 1600000])),
    x=alt.X('GICS Sector'))

### displaying the charts
col1, col2 = st.columns(2)
with col1:
    col3, col4 = st.columns(2)
    with col3:
        '''
        #### 2019
        '''
        st.altair_chart(chart_2019, use_container_width=True, theme = 'streamlit')
    with col4:
        sums2019 = data_2019.groupby('GICS Sector')['salecs'].sum()
        st.write(sums2019)

with col2:
    col3, col4 = st.columns(2)
    with col3:
        '''
        #### 2022
        '''
        st.altair_chart(chart_2022, use_container_width=True, theme = 'streamlit')
    with col4:
        sums2022 = data_2022.groupby('GICS Sector')['salecs'].sum()
        st.write(sums2022, use_container_width = True)

#############################################
# Table/DataFrame
#############################################
'''
### Companies in Each Industry
'''
grouped = raw_data.groupby('GICS Sector')['Symbol'].apply(lambda x: list(set(x)))
st.dataframe(grouped, use_container_width = True)

# divider line
st.divider() # Draws a horizontal line

#############################################
# DataFrames
#############################################
st.subheader('DataFrames')
with st.expander("2019 DataFrame"):
    st.table(data_2019)
with st.expander("2022 DataFrame"):
    st.table(data_2022)
