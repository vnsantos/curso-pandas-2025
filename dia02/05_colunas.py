#%%

import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep=";")
df

#%%

df.shape

#%%

df.info(memory_usage="deep")

#%%
df.dtypes

#%%
renamed_columns = {"QtdePontos": "QtPontos",
                        "DescSistemaOrigem": "SistemaOrigem"}
df.rename(columns=renamed_columns, inplace=True)

#%%

colunas = ["IdCliente", "QtPontos"]

df[colunas]

#%%

#SELECT * FROM df
df

#%%

#SELECT IdCliente FROM df

df[['IdCliente']]

#%%

#SELECT IdCliente, qtPontos FROM df LIMIT 5

df[["IdCliente","QtPontos"]].head(5)


#%%

#SELECT IdCliente, IdTransacao,QtPontos
#FROM df
#LIMIT 5

df[["IdCliente", "IdTransacao","QtPontos"]].head(5)

#%%

colunas = list(df.columns)
colunas.sort()
colunas

df = df[colunas]
df