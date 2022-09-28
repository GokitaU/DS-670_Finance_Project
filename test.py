#test code
import yahoo_fin.stock_info as si

lists=si.tickers_nasdaq()
#lists=si.tickera_sp500()

prices={}

for ticker in lists:
    prices[ticker]=si.get_data(ticker)

for ticker in lists:
    try:
        prices[ticker]=si.get_data(ticker)
        print(prices[ticker])
    except KeyError:
        print(f'Ticker {ticker} missing data')
        pass
