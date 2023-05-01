#############################################
# Getting started
#############################################
# 1. open this code
# 2. open terminal
# 3. change directory (cd) to this file
# 4. command line: conda activate streamlit-env
# 5.command line streamlit run Welcome.py
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
    page_title="Project - Sunset",
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
'''
# The Impact of COVID-19 on the Supply Chain from a Financial Persepective
## describing what is happeing


image at the bootome of the industry breakdown by sales - just form the first csv file
## Industry: bla bla bal
'''
## Goes on the overall page!!!
# ## overall pie chart
# fig0_1 = px.pie(raw_data, values='sales', names='seller', title = "Total Sales from Compustat For each Seller")
# st.plotly_chart(fig0_1, theme="streamlit", use_container_width=True)

data_2019 = raw_data[raw_data["fyear"] == 2019]
data_2022 = raw_data[raw_data["fyear"] == 2022]

'''
### 2019
'''
st.bar_chart(data = data_2019, x = 'GICS Sector', y = 'salecs', use_container_width=True, height = 700)

'''
### 2022
as can be seen by the below bar chart, there is quite a bit of missing compustat data for 2022
'''
st.bar_chart(data = data_2022, x = 'GICS Sector', y = 'salecs', use_container_width=True, height = 700)

'''
### List of sellers in the industry
if we want we can have to top preformer in the idnstry ??
'''

with st.expander("Raw DataFrame"):
    st.table(raw_data)
with st.expander("2019 DataFrame"):
    st.table(data_2019)
with st.expander("2022 DataFrame"):
    st.table(data_2022)
