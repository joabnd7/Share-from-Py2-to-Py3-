
from io import BytesIO
from io import StringIO
import pandas as pd
import ctypes
import time

import redis

df = pd.DataFrame()


df.at[0,'ch1']= 100
df.at[1,'ch1']= 1200
df.at[2,'ch1']= 300
df.at[0,'ch2']= 300
df.at[1,'ch2']= 500
df.at[2,'ch2']= 700

print(' ')
print('------------------------')
print('Original Data Frame:')
print(df)
print('------------------------')
print(' ')

text_stream = BytesIO()

df.to_csv(text_stream)

#Python 2
pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
redis = redis.Redis(connection_pool=pool)
redis.set('ch5','shit')
redis.set('ch7',text_stream.getvalue())
