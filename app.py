from pandas_datareader import data as pdr
from datetime import date
import yfinance as yf
yf.pdr_override()
import pandas as pd
import datetime

# Tickers list
# We can add and delete any ticker from the list to get desired ticker live data
ticker_list=['GOOG', 'AAPL', 'DJIA', 'DOW', 'LB', 'EXPE', 'PXD', 'MCHP', 'CRM', 'JEC' , 'NRG', 'HFC', 'NOW']

today = date.today()

# We can get data by our choice by giving days bracket
#start_date= "2017–01–01"
#end_date="2022–08–31"

dic = {'Select start date': datetime.datetime(2017, 1, 1, 0, 0)}
st_dt = 0
for key, datetime_obj in dic.items():
     datetime_str = datetime_obj.strftime("%Y-%m-%d")
     st_dt = datetime_str

files=[]
def getData(ticker):
    print(ticker)
    data = pdr.get_data_yahoo(ticker, start=st_dt, end=today)
    dataname= ticker+'_'+str(today)
    files.append(dataname)
    SaveData(data, dataname)

# Create a data folder in your current dir.
def SaveData(df, filename):
    df.to_csv('./data/'+filename+'.csv')

#This loop will iterate over ticker list, will pass one ticker to get data, and save that data as file.

for tik in ticker_list:
    getData(tik)

for i in range(0,11):
    df1 = pd.read_csv('./data/'+ str(files[i])+'.csv')
    print (df1.head())