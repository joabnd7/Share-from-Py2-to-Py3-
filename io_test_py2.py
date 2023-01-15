
from io import BytesIO
import pandas as pd
import redis

df = pd.DataFrame()

#make a test dataframe the fun way
df.at[0,'ch1']= 100
df.at[1,'ch1']= 1200
df.at[2,'ch1']= 300
df.at[0,'ch2']= 300
df.at[1,'ch2']= 500
df.at[2,'ch2']= 700

#display this nice dataframe
print(' ')
print('------------------------')
print('Original Data Frame:')
print(df)
print('------------------------')
print(' ')

#convert the dataframe quickly in memory to a csv string
text_stream = BytesIO()
df.to_csv(text_stream)

#Python 2 setup a way to send stuff to REDIS (needs to be already running in Ubuntu under Windows WSL)
pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
redis = redis.Redis(connection_pool=pool)
redis.set('ch5','shit')
redis.set('ch7',text_stream.getvalue())

#see Readme for the rest...
