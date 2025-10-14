#%%

import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv",sep=";")
transacoes.head()

clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes.head()

clientes = clientes.rename(columns={'idCliente': 'IdCliente'})

#%%

transacoes.merge(clientes, 
                 how='left',
                 on=['IdCliente'],
                 suffixes=["Transacao","Cliente"],
                   )

#%%

transacao_produto = pd.read_csv("../data/transacao_produto.csv",sep=";")
produtos = pd.read_csv("../data/produtos.csv",sep=";")

produtos['IdProduto'] = produtos['IdProduto'].astype(str)
transacao_produto['IdProduto'] = transacao_produto["IdProduto"].astype(str)
#%%

produtos = produtos[produtos["DescNomeProduto"] == "Presença Streak"]

(transacoes.merge(transacao_produto, on="IdTransacao", how='left')
            .merge(produtos, on=["IdProduto"],how="inner")
            .groupby(by="IdCliente")["IdTransacao"]
            .count()
            .sort_values(ascending=False)
            .head(1)
            )

