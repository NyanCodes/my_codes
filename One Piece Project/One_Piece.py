import pandas as pd

data = pd.read_csv("OP_Seasons.csv")

print(data.info()) 

# Drop columns based on column index.
# data = data.drop(data.columns[3],axis = 1)

data.iloc[3]