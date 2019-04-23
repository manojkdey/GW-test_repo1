# Dependencies
import pandas as pd
import numpy as np

# Name of the CSV file
ruralUrbanFile = 'urban-vs-rural-majority.csv'
gdpData = 'GDP-per-capita-in-the-uk-since-1270.csv'
# The correct encoding must be used to read the CSV in pandas
df = pd.read_csv(ruralUrbanFile, encoding="ISO-8859-1")
df.head()

# The correct encoding must be used to read the CSV in pandas
df = pd.read_csv(gdpData)
df.head()