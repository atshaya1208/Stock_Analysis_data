import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

connection = st.connection('mysql', type='sql')

st.title("Stock Data Analysis")

st.header("Volatility Analysis")

df_volatility = connection.query('SELECT * FROM volatility')

st.bar_chart(
    data = df_volatility,
    x="ticker",
    y="volatility"
)

st.header("Cumulative Return")

df_cum_per = connection.query('SELECT * FROM cumulative_percentage')

st.line_chart(
    data = df_cum_per,
    x="ticker",
    y="cum_percentage"
)

st.header("Sector-wise Performance")
df_sector_perm = connection.query('SELECT * FROM sector_performance')

st.bar_chart(
    data = df_sector_perm,
    x = "sector",
    y = "cum_percentage"   
)

st.header("Stock Price Correlation")
df_stock_corr = connection.query("SELECT ADANIENT, ADANIPORTS  FROM stock_correlation")
st.dataframe(df_stock_corr)

fig, ax = plt.subplots(figsize=(20, 15))
sns.heatmap(
    df_stock_corr,
    annot=True,
    cmap='RdBu_r',
    center=0,fmt=".2f",
    ax=ax,
)
plt.title("Correlation Matrix of Closing Price between ADANIENT and ADANIPORTS")
st.pyplot(fig)


df_stock_corr = connection.query("SELECT AXISBANK, HDFCBANK  FROM stock_correlation")

fig, ax = plt.subplots(figsize=(20, 15))
sns.heatmap(
    df_stock_corr,
    annot=True,
    cmap='RdBu_r',
    center=0,fmt=".2f",
    ax=ax,
)
plt.title("Correlation Matrix of Closing Price between AXISBANK and HDFCBANK")
st.pyplot(fig)


df_stock_corr = connection.query("SELECT WIPRO, HCLTECH  FROM stock_correlation")

fig, ax = plt.subplots(figsize=(20, 15))
sns.heatmap(
    df_stock_corr,
    annot=True,
    cmap='RdBu_r',
    center=0,fmt=".2f",
    ax=ax,
)
plt.title("Correlation Matrix of Closing Price between WIPRO and HCLTECH")
st.pyplot(fig)


st.title(" Monthly Top Gainers & Losers")
months = ["jan2024_df", "feb2024_df", "march2024_df", "april2024_df", "may2024_df", "june2024_df", "july2024_df", "aug2024_df", "sep2024_df", "oct2024_df", "nov2024_df", "dec2023_df", "nov2023_df"]

tabs = st.tabs(months)
for i in range(len(tabs)):
    with tabs[i]:
        name = months[i]
        st.header(f"Performance for {name}")

        df = connection.query(f"SELECT * FROM {name};")

        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
        
            st.caption("chart 1")
        fig1 = px.bar(df, x='ticker', y='monthly_returns')
        fig1.update_layout(margin=dict(l=20, r=20, t=30, b=20), height=300)
        st.plotly_chart(fig1, use_container_width=True)

        with col2:
            st.caption("chart 2")
        fig2 = px.line(df, x='ticker', y='monthly_returns')
        fig2.update_layout(margin=dict(l=20, r=20, t=30, b=20), height=300)
        st.plotly_chart(fig2, use_container_width=True)

        with col3:
            st.caption("chart 3")
        fig3 = px.area(df, x='ticker', y='monthly_returns')
        fig3.update_layout(margin=dict(l=20, r=20, t=30, b=20), height=300)
        st.plotly_chart(fig3, use_container_width=True)
            
        with col4:
            st.caption("chart 4")
        fig4 = px.area(df, x='ticker', y='open')
        fig4.update_layout(margin=dict(l=20, r=20, t=30, b=20), height=300)
        st.plotly_chart(fig4, use_container_width=True) 
        
        with col5:
            st.caption("chart 5")
        fig5 = px.area(df, x='ticker', y='close')
        fig5.update_layout(margin=dict(l=20, r=20, t=30, b=20), height=300)
        st.plotly_chart(fig5, use_container_width=True)
        
        st.divider()
