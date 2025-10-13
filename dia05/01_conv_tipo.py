#%%

import pandas as pd

#%%

df = pd.read_csv("../data/clientes.csv", sep=";")


#%%

df["qtdePontos"].astype(float)

#PARA CONVERTER UTILIZAR O ASTYPE

#%%

replace = {"000-00-00 00:00:00.000": "2024-02-01 09:00:00.000"}

df["DtCriacao"] = pd.to_datetime(df["DtCriacao"].replace(replace))

#%%

df["DtCriacao"].dt.month