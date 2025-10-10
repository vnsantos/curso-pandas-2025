#%%

import pandas as pd

#LENDO ARQUIVO
df = pd.read_csv("../data/clientes.csv")
df

#%%

#SALVANDO ARQUIVO
df.to_csv("clientes.csv", index=False)

#%%

df.to_parquet("clientes.parquet", index=False)

#%%

df_2 = pd.read_parquet("clientes.parquet")
df_2

#%%

df.to_excel("clientes.xlsx", index=False)

#%%

df_3 = pd.read_excel("clientes.xlsx")
df_3
