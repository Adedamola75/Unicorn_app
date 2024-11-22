import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff
import plotly.express as px

def load_data():
    file = "Unicorn_Companies.csv"
    df = pd.read_csv(file)
    df.loc[:,"Valuation ($)"] = df.loc[:,"Valuation"].str.replace("$","").str.replace("B","000000000").astype("int64")
    df.loc[:,"Funding ($)"] = df.loc[:,"Funding"].str.replace("$","").str.replace("Unknown","-1").str.replace("M","000000").str.replace("B","000000000").astype("int64")
    df.drop(columns=["Valuation","Funding"], axis=1,inplace=True)
    df['Date Joined'] = pd.to_datetime(df['Date Joined'])
    df.loc[:,"Year Joined"] = df['Date Joined'].dt.year
    df.loc[:,"Years to unicorn status"] = df["Year Joined"] - df["Year Founded"]
    df.loc[:,"count"] = 1

    return df

# load  the datasets
df = load_data()
st.title("Unicorn Data Companies")


# create filters
industry_list = df["Industry"].unique()
selected_industry = st.sidebar.multiselect("Industry",industry_list)
filtered_industry = df[df["Industry"].isin(selected_industry)]

# country
Country_list = df["Country/Region"]
selected_Country = st.sidebar.multiselect("Country/Region",Country_list)
filtered_Country = df[df["Country/Region"].isin(selected_Country)]

# this is the data if industry is selected and/if none
if selected_industry:
    st.dataframe(filtered_industry)
else:
    st.dataframe(df)

#Country
city_list = df["City"].unique()
selected_city = st.sidebar.multiselect("City",city_list)
filtered_city = df[df["City"].isin(selected_city)]

if selected_city: 
    st.dataframe(filtered_city)

else:
    st.dataframe(df)

#Continenet
Continent_list = df["Continent"]
selected_Continent = st.sidebar.multiselect("Continent",Continent_list)
filtered_Continent = df[df["Continent"].isin(selected_Continent)]

if selected_Continent: 
    st.dataframe(filtered_Continent)

else:
    st.dataframe(df)

# country
Country_list = df["Country/Region"].unique()
selected_Country = st.sidebar.multiselect("Country/Region",Country_list)
filtered_Country = df[df["Country/Region"].isin(selected_Country)]

if selected_Country: 
    st.dataframe(filtered_Country)

else:
    st.dataframe(df)
# calculate some metrics
no_of_companies = len(df)
total_valuation =f"${round(df["Valuation ($)"].sum() / 1000000000,2)}B"
total_funding = df["Funding ($)"].sum()

# display these metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("No of companies",no_of_companies)
with col2:
    st.metric("Total Valuation",total_valuation)
with col3:
    st.metric("Total Funding",total_funding)

#
con = st.container()

with con:
    st.subheader("Charts section")
    bar_plot_1 = sns.countplot(data = df, x = df['Industry'])
    plt.xticks(rotation = 45)
    plt.ylabel("No of Companies")
    st.pyplot(bar_plot_1.get_figure())


    # plotly charts
    # line charts
    line_1 = px.bar(
        df,x = "Industry", y = "count")
    
    st.plotly_chart(line_1)
    
