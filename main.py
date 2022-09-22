#https://algotrading101.com/learn/yahoo-finance-api-guide/

import streamlit as st
import yahoo_fin.stock_info as si
from yahoo_fin.stock_info import get_data

amazon_weekly= get_data("amzn", start_date="01/01/2017", end_date="09/21/2022", index_as_date = True, interval="1wk")
print(amazon_weekly)

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
    ticker_name = st.selectbox('Select Ticker :',ticker_list,index = 12)
with title_col2:
    st_date = st.date_input('Start Date :')
with title_col3:
    en_date = st.date_input('End Date :')

ticker_details= get_data(ticker_name, start_date=st_date, end_date=en_date, index_as_date = True)
if (len(ticker_details) > 0):
    st.write(ticker_details)
else:
    st.write("No Data Found!")
