#https://algotrading101.com/learn/yahoo-finance-api-guide/

import streamlit as st
import yahoo_fin.stock_info as si
from yahoo_fin.stock_info import get_data
import datetime
import pandas as pd

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

amazon_weekly= get_data("amzn", start_date="01/01/2017", end_date="09/21/2022", index_as_date = True, interval="1wk")
print(amazon_weekly)

currentDate = datetime.date.today()
firstDayOfMonth = datetime.date(currentDate.year, currentDate.month, 1)

ticker_list = ["amzn", "aapl", "ba"]
historical_datas = {}
for ticker in ticker_list:
    historical_datas[ticker] = get_data(ticker)

#print(historical_datas["aapl"])
print(historical_datas["ba"])
print(historical_datas["ba"].isnull().sum())

#dow_list = si.tickers_dow()
#print(dow_list)

#print("Tickers in Dow Jones:", len(dow_list))
#print(dow_list[0:10])

ticker_list = si.tickers_nasdaq()
print("List of tickers: ", len(ticker_list))
print("Tickers: ", ticker_list[0:10])

st.markdown("""# *Finance Data Analysis*""")

title_col1,title_col2,title_col3 = st.columns([3,3,3])
with title_col1:
    ticker_name1 = st.selectbox('Select Ticker :',ticker_list,index = 12)
with title_col2:
    ticker_name2 = st.selectbox('Select Ticker :',ticker_list,index = 1)
with title_col3:
    ticker_name3 = st.selectbox('Select Ticker :',ticker_list,index = 2)


title_col1,title_col2,title_col3 = st.columns([3,3,3])
with title_col1:
    st_date = st.date_input('Start Date :',firstDayOfMonth)
with title_col2:
    en_date = st.date_input('End Date :',currentDate)
with title_col3:
    if st.button('Compare'):
        print("Compare pressed!")
    else:
        print("Compare not pressed!")


title_col1,title_col2,title_col3 = st.columns([3,3,3])
with title_col1:
    ticker_details1 = get_data(ticker_name1, start_date=st_date, end_date=en_date, index_as_date = True)
    if (len(ticker_details1) > 0):
        # display the details of stock 
        st.subheader(f'{ticker_name1} Stock Data')
        st.write(ticker_details1.head(3))
    else:
        st.write("No Data Found!")
with title_col2:
    ticker_details2= get_data(ticker_name2, start_date=st_date, end_date=en_date, index_as_date = True)
    if (len(ticker_details2) > 0):
        # display the details of stock 
        st.subheader(f'{ticker_name2} Stock Data')
        st.write(ticker_details2.head(3))
    else:
        st.write("No Data Found!")
with title_col3:
    ticker_details3= get_data(ticker_name3, start_date=st_date, end_date=en_date, index_as_date = True)
    if (len(ticker_details3) > 0):
        # display the details of stock 
        st.subheader(f'{ticker_name3} Stock Data')
        st.write(ticker_details3.head(3))
    else:
        st.write("No Data Found!")

title_col1,title_col2,title_col3 = st.columns([3,3,3])
with title_col1:
    st.subheader(ticker_name1)
    df1 = ticker_details1.drop(["adjclose","volume","ticker"], axis=1)
    st.line_chart(df1)
with title_col2:
    st.subheader(ticker_name2)
    df2 = ticker_details2.drop(["adjclose","volume","ticker"], axis=1)
    st.line_chart(df2)
with title_col3:
    st.subheader(ticker_name3)
    df3 = ticker_details1.drop(["adjclose","volume","ticker"], axis=1)
    st.line_chart(df3)

def get_charts(stock_details1,stock_details2,stock_details3):
    # line chart for open
    st.subheader('Open Price Stock Data')
    df1 = stock_details1.drop(["high","low","close","adjclose","volume","ticker"], axis=1)
    df1.rename(columns={'open': ticker_name1}, inplace=True)
    df2 = stock_details2.drop(["high","low","close","adjclose","volume","ticker"], axis=1)
    df2.rename(columns={'open': ticker_name2}, inplace=True)
    df3 = stock_details3.drop(["high","low","close","adjclose","volume","ticker"], axis=1)
    df3.rename(columns={'open': ticker_name3}, inplace=True)
    df = pd.concat([df1, df2, df3], axis=1)
    st.dataframe(df, 1500, 300)
    st.line_chart(df)

    # line chart for low
    st.subheader('Low Price Stock Data')
    df1 = stock_details1.drop(["high","open","close","adjclose","volume","ticker"], axis=1)
    df1.rename(columns={'low': ticker_name1}, inplace=True)
    df2 = stock_details2.drop(["high","open","close","adjclose","volume","ticker"], axis=1)
    df2.rename(columns={'low': ticker_name2}, inplace=True)
    df3 = stock_details3.drop(["high","open","close","adjclose","volume","ticker"], axis=1)
    df3.rename(columns={'low': ticker_name3}, inplace=True)
    df = pd.concat([df1, df2, df3], axis=1)
    st.dataframe(df, 1500, 300)
    st.line_chart(df)

    # line chart for high
    st.subheader('High Price Stock Data')
    df1 = stock_details1.drop(["low","open","close","adjclose","volume","ticker"], axis=1)
    df1.rename(columns={'high': ticker_name1}, inplace=True)
    df2 = stock_details2.drop(["low","open","close","adjclose","volume","ticker"], axis=1)
    df2.rename(columns={'high': ticker_name2}, inplace=True)
    df3 = stock_details3.drop(["low","open","close","adjclose","volume","ticker"], axis=1)
    df3.rename(columns={'high': ticker_name3}, inplace=True)
    df = pd.concat([df1, df2, df3], axis=1)
    st.dataframe(df, 1500, 300)
    st.line_chart(df)

    # line chart for close
    st.subheader('Close Price Stock Data')
    df1 = stock_details1.drop(["high","open","low","adjclose","volume","ticker"], axis=1)
    df1.rename(columns={'close': ticker_name1}, inplace=True)
    df2 = stock_details2.drop(["high","open","low","adjclose","volume","ticker"], axis=1)
    df2.rename(columns={'close': ticker_name2}, inplace=True)
    df3 = stock_details3.drop(["high","open","low","adjclose","volume","ticker"], axis=1)
    df3.rename(columns={'close': ticker_name3}, inplace=True)
    df = pd.concat([df1, df2, df3], axis=1)
    st.dataframe(df, 1500, 300)
    st.line_chart(df)

get_charts(ticker_details1,ticker_details2,ticker_details3)
