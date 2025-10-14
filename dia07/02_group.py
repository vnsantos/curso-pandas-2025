#%%
import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv",sep=";")
transacoes.head()

#%%
transacoes.groupby(by=["IdCliente"]).count()

# %%
transacoes.groupby(by=["IdCliente"], as_index=False)[["IdTransacao"]].count()

#%%

#qtde_transacoes
#total_pontos
#pontos / transacoes

summary = (transacoes.groupby(by=["IdCliente"], as_index=False)
          .agg({"IdTransacao": ['count'],
                "QtdePontos": ['sum','mean']}))

summary

#%%

summary.columns = ["IdCliente","QtdeTransacao","TotalPontos","AvgPontos"]
summary