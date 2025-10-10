#%%

import pandas as pd

idades = [
    32,38,30,31,23,27,32,37
]

nomes = [
    "vinicius", "julia","pedro","maria","joao","aurora","alice","apolo"
]

series_idades = pd.Series(idades)
series_nomes = pd.Series(nomes)

#%%

df = pd.DataFrame()
df["idades"] = series_idades
df["nomes"] = series_nomes
df

#%%

df.iloc[0]["nomes"]

#%%

df.iloc[-1]["idades"]