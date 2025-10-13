#%%

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes

#%%

clientes = clientes.dropna(how="all", subset=["DtCriacao", "qtdePontos"])

#%%

