# Welcome to our [Team Project Website!](https://jerseyk-final-project-sunset-website-welcome-eoomf2.streamlit.app)

This is a website to showcase our final project for FIN 377 - Data Science for Finance course at Lehigh University. This website was made using [streamlit.io](https://streamlit.io/) to create a dashboard for our visual analysis.

## Table of Contents
1. [Introduction](#introduction)
2. [Methodology](#method)
    1. [Data Collection](#datacol)
    1. [Data Cleaning](#dataclean)
    1. [Merging Compustat & SP500 Datasets](#merg)
    1. [Identifying the Unique `gvkey` to Obtain Accounting Data](#unique)
    1. [Merging Compustat & SP500 List](#list)
    1. [Final Datasets](#final)
3. [Analysis](#analysis)
4. [Conclusion](#conclu)
5. [About the Team](#team)


## Introduction <a name="introduction"></a>
For our final project we decided to explore how the supply chain network has reformed and changed following the pandemic based on customer/supplier contracts from the Compustat Customer Supplier dataset. The main goal of this project was to compare the number of contracts as well as compare the growth of technology companies within the supply chain network. 

The question we proposed at the start of the project was how has the supply chain industry changed following the pandemic? One of our initial hypotheis was that the amount of technology based companies would increase in 2022. The other hypothesis we had was that the amount of contracts involving healthcare/pharmaceutical companies would also increase. 

The COVID-19 pandemic has had a significant impact on the global economy and disrupted supply chains across various industries. As a result, we conducted an analysis of the financial factors affecting several seller companies. We focused on companies that are in the S&P 500 as of 2022 and used data from financial reports in 2019 and 2022 to gain insights into how the pandemic has affected their financial performance.

## Methodology <a name="method"></a>
### Data Collection <a name="datacol"></a>
To create and run our file we used various imports such as `pandas`, `numpy`, `os`, and `seaborn`. In addition to those general python imports, we also used `insufficient_but_starting_eda` from `eda.py` which is located in the [community codebook](https://github.com/LeDataSciFi/ledatascifi-2023/tree/main/community_codebook). We used three different datasets to create one final dataset to be displayed visually through analysis on our dashboard.

[S&P 500](https://github.com/JerseyK/Final-Project_Sunset/blob/d3a36fde0bb19d897fb15effcb85ffb0f04ec78b/inputs/sp500_2022.csv): We scraped data from Wikipedia to create this dataset to filter for SP500 companies.

[Compustat Customer Supplier](https://github.com/JerseyK/Final-Project_Sunset/blob/d3a36fde0bb19d897fb15effcb85ffb0f04ec78b/inputs/cust_supply_2019_2022.csv): This dataset contained raw data provided by Dr. Bowen that showed filings between customers and suppliers between 2019 and 2022.

[Accounting 2018-2022](https://github.com/JerseyK/Final-Project_Sunset/blob/d3a36fde0bb19d897fb15effcb85ffb0f04ec78b/inputs/acct_data.csv): This dataset was also provided by Dr. Bowen and is comprised of accounting variables we requested.


```
comp = pd.read_csv('inputs/cust_supply_2019_2022.csv')
sp500 = pd.read_csv('inputs/sp500_2022.csv')
acct_raw = pd.read_csv("inputs/acct_data.csv"
```


### Data Cleaning <a name="dataclean"></a>

**S&P 500**: There were 503 firms in 2022.

**Compustat Customer Supplier**: We first ran [EDA](https://github.com/JerseyK/Final-Project_Sunset/blob/d3a36fde0bb19d897fb15effcb85ffb0f04ec78b/data_eda.ipynb) on the raw compustat data. We found:
- There are 77901 data entries in this csv
- There are 9 categorical variables
- There are 6 numerical variables
- The unit level is sales
- The only variables with missing data are: 
    - gareac (57.8%) 
    - gareat (57.8%)
    - stype (14.0%)
    - salecs (12.4%)
    - cik (0.6%)
    
These variables describe the seller firm a row of data:   
- **gvkey:** a unique identifier for the company (Global Company Key)
- **sic:** Standard Industrial Classification code, a numerical code used to classify industries
- **cusip:** CUSIP number, a unique identifier for a security
- **cik:** SEC Central Index Key, a unique identifier for a company
- **tic:** stock ticker symbol
- **conm:** company name
- **srcdate:** source date

These variables describe the customer of the firm and say something about the relationship type:
- **cid:** a unique identifier for the customer
- **cnms:** customer name
- **ctype:** customer type
- **gareac:** geographic area code
- **gareat:** geographic area type
- **salecs:** sales in current period (in millions)
- **sid:** segment identifier
- **stype:** segment type


We found that even though more than 50% of geographic  area code (`gareac`) and geographic area type (`gareat`) are missing, these values wouldn't be needed for our analysis and were dropped. We also were not concerned about segment type (`stype`) because we used `GICS Sector` to describe the seller.  Another variable, sales `salecs` had 12.4% missing observations. We saw that when `salecs` were NaN, the buyer was also "not reported"; therefore we dropped the missing observations.

Based off of our EDA, we first dropped all of the observations where the customer name was not reported, this also corresponded to sellers not in the SP500. Next, we dropped any observations where there were no sales reported. 

*For this dataset we are going to consider firms that filed in 2019 are providing information for the 2019 fiscal year. We know that this can lead to some inaccuracies when firms don't file in 2019 for the 2019 fiscal year. For instance if a firm files in January of 2020 our analysis is that this data will correspond with the fiscal year of 2020, when in reality the data most likely corresponds with the 2019 fiscal year.* **Any mention of `gvkey` or firm, is in reference to the seller.**

```
comp2 = comp
comp2 = comp2[comp2['cnms'] != 'Not Reported']
comp3 = comp2.dropna(subset=['salecs'])
```


**Accounting 2018-2022**: We provided Dr. Bowen with a list of unique `gvkeys` along with a request for data for the following accounting variables:
- **fyear:** fiscal year
- **sale:** net sales
- **rect:** receivables/total
- **invt:** inventories
- **ap:** accounts payable - trade
- **ib:** income before extraordinary items
- **ni:** net income (loss)
- **obidp:** operating income before depreciation
- **at:** total assets
- **capx:** capex, dollar amount
- **capxv:** capex ratio for current fiscal year
- **cogs:** cost of goods sold
- **gp:** gross profit
- **epsfx:** eps basic
- **acominc:** net income
    
With this new dataset we then performed [EDA](https://github.com/JerseyK/Final-Project_Sunset/blob/d3a36fde0bb19d897fb15effcb85ffb0f04ec78b/data_eda.ipynb). After running that we found that:
- There are 26905 observations
- The unit level is firm-year
- The variables with missing data are:
    - capxv (16.3%)
    - oibdp (11.4%)
    - invt (8.9%)
    - capx (8.7%)
    - rect (8.5%)
    - acominc (8.3%)
    - ap (8.3%)
    - epsfx (8.1%)
    - ib (8.0%)
    - ni (8.0%)
    - cogs (8.0%)
    - gp (8.0%)
    - sale (8.0%)
    - at (7.7%)
    
    
Based off of our EDA we decided to use `ni` as the variable to represent net income as it had the least missing values. We used the same logic to decide to use `capx` over `capxv`. In turn we were then able to drop the other variables that represented net income `acominc`, `oibdp`, and `ib`, as well as `capxv`. After dropping those variables we had a dataset ready that we could add to by creating variables to show the growth (return) between 2019 and 2022 firms for each accounting variables before merging with the SP500 and Compustat dataset.


### Merging Compustat & SP500 Datasets <a name="merg"></a>
We merged `comp` with `sp500` to create `merged` which merged the two on `CIK`. This final dataset gave us 385 unique firms.
```
comp3 = comp3.rename(columns = {'cik': 'CIK'})
merged = comp3.merge(sp500, on='CIK', how = 'inner')
```


Next, we dropped the filings that were not in 2019 or 2022. We used the indices of the filtered dates (01/01/2020 to 12/31/2021) to be be dropped. This left us with 355 unique firms.
```
merged['date'] = pd.to_datetime(merged['srcdate'])
dates = merged.sort_values(by='srcdate')
```


```
start_date = '2020-01-01'
end_date = '2021-12-31'
filtered_df = merged.query('@start_date <= date <= @end_date')

filtered_indices = filtered_df.index

filtered_out_df = merged.drop(filtered_indices)
```


We created a column `fyear` to simplify later merging. 
```
filtered_out_df['fyear'] = pd.to_datetime(filtered_out_df['srcdate']).dt.year
```


Lastly, we then filtered out any firms that didn't have filings in both 2019 and 2022. We also noticed that there was no 2019 Compustat data for `gvkey = 25313`, so we dropped this firm. This left us with 88 unique firms. This is a number we would be able to use to check on our final merge.
```
filtered = filtered_out_df.groupby('gvkey').filter(lambda x: x['fyear'].max() == 2022)
```

### Identifying the Unique `gvkey` to Obtain Accounting Data <a name="unique"></a>
With the `filtered_out_df` dataset we were able to extract the list of unique `gvkey` to a .csv file to obtain the accounting from Dr. Bowen.
```
listkeys = pd.DataFrame(filtered_out_df['gvkey'].unique())
listkeys.to_csv('inputs/listkeys.csv', index=False)
```

### Merging Accounting & SP500 List <a name="list"></a>

With the cleaned accounting data we were able to merge `listkeys` and `acct_raw` on `gvkey`. There we had 354 unique firms.
```
listkeys2 = listkeys.rename(columns={0: 'gvkey'})

merged_acct_raw_keys = pd.merge(listkeys2,acct_raw,how = 'inner', on='gvkey')
```


The next step was to take that new merged DataFrame and filter it to `fyear` to be 2019 or 2022. We then dropped the variables we deemed unnecessary during data cleaning to make our dataset concise.
```
acct_df = merged_acct_raw_keys.query('fyear == 2019 or fyear == 2022')
acct_df = acct_df[['gvkey', 'fyear', 'ap', 'at', 'capx', 'cogs', 'epsfx', 'gp', 'invt', 'ni', 'rect', 'sale']]
```


Before merging with the `filtered` dataset, we created variables for each accounting variable (`ap`, `capx`, `ni`, etc) to show the growth between 2019 and 2022. 
```
prev_row = acct_df.iloc[0]
for index, row in acct_df.iloc[1:].iterrows():
    if row.values[1] == 2019.0:
        prev_row = row
    elif row.values[1] == 2022.0:
        calc_row = (row - prev_row) / prev_row * 100
        calc_row.rename({k: f"calc_{k}" for k in calc_row.index}, inplace=True)
        acct_df.loc[index, calc_row.index] = calc_row
```


### Final Datasets <a name="final"></a>
For our final dataset we merged elements from the Compustat/SP500 dataset with the accounting dataset. We took `filtered` and kept our desired columns of `gvkey`, `fyear`, `conm`, `Symbol`, `CIK`. The next thing we did was drop duplicates so that we could be able to match firms in the accounting dataset. The final merge left us with 88 unique firms. (The same amount we found earlier in `filtered`). 
```
cleaned_comp = filtered[['gvkey', 'fyear', 'conm', 'Symbol', 'CIK']]
cleaned_comp = cleaned_comp.drop_duplicates()

accounting = pd.merge(cleaned_comp,acct_df, how='left',on=['gvkey','fyear'], indicator=True)
```

We then used `to_csv` to save the final dataset for the dashboard.
```
# accounting data
accounting.to_csv("outputs/accounting_final.csv", index = False)

# compustat data
filtered.to_csv("outputs/compustat_final.csv", index = False)
```

## Analysis <a name="analysis"></a>
For the full analysis please check out our dashboard [here](https://jerseyk-final-project-sunset-website-welcome-eoomf2.streamlit.app/).
The python packaged used were: `pandas`, `numpy`, `ploty.express`, `altair`, and `streamlit`. 


## Conclusion <a name="conclu"></a>
Our final results include 88 companies. We dropped companies in real estate, utilities and energy sectors because of the lack of data from the 2019 and 2022 financial reports. This could be a possible limitation for our analysis, however, we feel that the sample size is still strong enough to be used as a representation of how the supply chain was impacted by the COVID-19 pandemic.

Looking at our results, we see that except for the IT industry and healthcare industry, most industries experienced a decrease in sales. Take these two companies for instance. **NVIDIA Corporation**, an IT company, had a significant increase in the demand for computer-related products, including GPUs, due to the shift towards remote work, distance learning, and increased usage of video streaming services. They been successful in expanding its reach into new markets, such as data centers, autonomous vehicles and AI<sup>[[1]](https://www.nvidia.com/en-us/)</sup>. NVIDIA saw a 147.06% increase in net sales from 2019 to 2022. **CATALENT INC**, a healthcare company, provided advanced delivery technologies, development, and manufacturing services for drugs, biologics, and consumer health products<sup>[[2]](https://www.catalent.com/about-us/overview/)</sup>. They especially collaborated with several pharmaceutical companies to support the development and production of vaccines and therapies. From 2019 to 2002, CATALENT saw a 91.74% increase in net sales.
Overall, despite the challenging business environment subsequent to the COVID-19 pandemic, the IT industry was able to maintain its performance and even improve its sales. This underscores the resilience of the industry and the importance of digitalization in the current business landscape. We can see from our visualization that the IT industry increased in sales by about half a million dollars from 2019 to 2022. These findings support the need for companies to adapt to the changing business landscape by embracing digitalization and other innovative strategies to remain competitive in today's economy.




## About the Team <a name="team"></a>
[Kyra Grodman](https://www.linkedin.com/in/kyragrodman/): BS in Finance and Business Infomation Systems
<br>
[Jersey Krupp](https://www.linkedin.com/in/jersey-ann-krupp/): MS in Financial Engineering
<br>
[Qiyu Yang](https://www.linkedin.com/in/qiyu-yang-672577222/): MS in Financial Engineering


*The snippets of code are from our [Analysis Github Repository](https://github.com/JerseyK/Final-Project_Sunset).*
