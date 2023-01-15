
import redis
import pandas as pd
from io import StringIO


#Python 3
#point to the pool dude
pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
redis = redis.Redis(connection_pool=pool)

#go get the items stored by Py2
item1 = redis.get('ch5')
item2 = redis.get('ch7')

print(item1.decode())
print(item2.decode())

#massage the string
s = item2.decode()

#convert back to a Pandas df to march on with
df = pd.read_csv(StringIO(s), sep=',' )

print(df)  #sorry it has an extra column - who cares