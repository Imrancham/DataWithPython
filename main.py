#Scientifics computing Libraries -->
# Pandas (Data structuer and tools)
# numpy (Array & Matrix)
# SciPy ( Integral, Solving PDE, optimization)

# Visualization Libraries
# Matplotlib (graphs and plots)
#Seaborn (plots:heat maps, time serise, violin plot)

#Algorithmic libraries
# Scikit-learn (ML, Regression, classification,..
# Statsmodels ( Explor data, estimate statistical model and perform statistical tests)

import pandas as pd
import numpy as np
# from dbmodule import connection


path = "/Users/imranchamieh/Downloads/imports-85.data"
df = pd.read_csv(path, header=None)

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
df.columns = headers
# print(df.head())
print(df.dtypes)
# print(df.describe(include="all"))
# df.info()
print(df.tail())
#
# to drop a row that contain a NaN use df.dropna() axis =0 -> drops the row axis =1 -> drops column
#df.dropna(subset=["price"], axis=0, inplace=True] inplace=True change the data frame directly

# to relpace date we can use df.replace(missing_value, new_value ) new_value -> mean, mode, ets.
df["normalized-losses"].replace('?', np.NaN)
df["normalized-losses"] = df["normalized-losses"].astype(int)
mean_loss = df["normalized-losses"].mean()
df["normalized-losses"].replace(np.NaN, mean_loss)










### Accessing Databases with Python
## DB-API
## Connecting to database
#cursor() return new cursor object using the connection
#commit() used to commit any transaction to the database
#rollback() causes the database to roll back of any pending transaction
#close() to close the database connection

#
# #creat connection object
# connection = connection('Library', 'root', 'Math4math')
#
# #creat a cursor object
# cursor = connection.cursor()
#
# # run quaries
# cursor.execute('select* from Books ')
# results = cursor.fetchall()
#
# #free resources
# cursor.close()
# connection.close()


