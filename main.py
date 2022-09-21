import yfinance as yf

fang = ['FB','AMZN','NFLX','GOOG']
tickers = [yf.Ticker(ticker) for ticker in fang]
tickers

goog = yf.Ticker('goog')
data = goog.history()
data.head()