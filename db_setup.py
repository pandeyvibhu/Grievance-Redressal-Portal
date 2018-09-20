import pandas as pd

file_loc = "grievances.xlsx"

df = pd.read_excel(file_loc, sheetname="Sheet1", header=0, skiprows=0, index_col=None, parse_cols="A:B", converters={'Category':str})

if retrain:

    print(df)

# Randomizing raw data
df = df.reindex(np.random.permutation(df.index))

print("DataSet = ", len(df))
print(df.shape)

return list(df['Description']), list(df['Category'])