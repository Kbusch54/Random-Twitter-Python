import datetime
import pandas as pd
import time
from pandas_market_calendars import get_calendar
import yfinance as yf

tickers_list = ['GOOG', 'TSLA', 'META']


data = yf.download(tickers_list,period='5d',interval='15m',)['Adj Close'].fillna(method='ffill')
data2 = yf.download(tickers_list,start='2023-7-6')
print('data2',data2)

# print(data)

# # print('idx',idxx[8].date())
# last_row_date = '2023-06-30 15:45:00'
# # print('something',data.loc[data.index.time == pd.to_datetime(last_row_date).time()])
# last_row = data.loc[data.index.time == pd.to_datetime(last_row_date).time()]
# print('last row indeex',last_row )
# # Generate the new timestamps
# new_timestamps = pd.date_range(start='2023-06-30 16:00:00', periods=70, freq='15min')
# print('new timestamps',new_timestamps)
# Create a DataFrame for the new points
# print('last row col1',last_row.index)
# print('last row col2',last_row['Column2'])
# new_points = pd.DataFrame(index=new_timestamps)
# new_points['Adj Close'] = last_row['Adj Close']
# new_points['Column1'] = last_row['Column1']
# new_points['Column2'] = last_row['Column2']
# print('new points',new_points)

# Append the new points to the original data
# data = data.append(new_points)

# # Save the updated data to a text file
# with open('filled_stock_data.txt', 'w') as file:
#     file.write(data.to_string())
# print('market close',market_close)
# print('market close my guy',market_close[str(idxx[0].date())],('2023-06-30') in market_close)
# print('checkcking market close',market_close[idxx[2]])
# Fill in missing values during after-market hours
# openTime = datetime.time(9,30,0)
# closeTime = datetime.time(15,45,0)
# lastValue = {}
# for idx, row in data.iterrows():

#     lastValue = [idx,row]
#     print('last value',lastValue)
#     if idx.time() > closeTime and idx.time() < openTime:
#         prev_close = data['Adj Close'][idx.date() - pd.DateOffset(days=1)].iloc[-1]
#         data['Adj Close'].loc[idx] = prev_close
#         print('prev close',prev_close)
#         print('other thing',data['Adj Close'].loc[idx])

# # Save the filled data to a text file
# with open('filled_stock_data.txt', 'w') as file:
#     file.write(data.to_string())