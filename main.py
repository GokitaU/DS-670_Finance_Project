#https://algotrading101.com/learn/yahoo-finance-api-guide/

from yahoo_fin.stock_info import get_data

amazon_weekly= get_data("amzn", start_date="01/01/2020", end_date="09/21/2022", index_as_date = True, interval="1wk")
print(amazon_weekly)

ticker_list = ["amzn", "aapl", "ba"]
historical_datas = {}
for ticker in ticker_list:
    historical_datas[ticker] = get_data(ticker)

print(historical_datas["aapl"])

import yahoo_fin.stock_info as si
dow_list = si.tickers_dow()
print(dow_list)

print("Tickers in Dow Jones:", len(dow_list))
print(dow_list[0:10])

x = si.tickers_nasdaq()
print(len(x))