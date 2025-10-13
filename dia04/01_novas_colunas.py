#%%

import pandas as pd
import numpy as np

df = pd.read_csv("../data/clientes.csv",sep=";")
df.head()

#%%

df["pontos_100"] = df["qtdePontos"] + 100
df.head()

#essa operação é mais rapida e performatica do que utilizar um for
#%%

nova_coluna=[]
for i in df["qtdePontos"]:
    nova_coluna.append(i+100)

nova_coluna

#%%

df["emailTwitch"] = df["flEmail"] + df["flTwitch"]
df.head()

#%%
df["flEmail"] * df["flTwitch"]

#INTERSECÇÃO

#%%

df["qtdeSocial"] = df["flEmail"] +	df["flTwitch"] + 	df["flYouTube"] +	df["flBlueSky"]	+ df["flInstagram"]
df

#%%

df["totalSocial"] = df["flEmail"] *	df["flTwitch"] * 	df["flYouTube"] *	df["flBlueSky"]	* df["flInstagram"]
df

#%%

df["qtdePontos"].describe()

#%%

df["logPontos"] = np.log(df["qtdePontos"]+1)
df["logPontos"].describe()

#%%

import matplotlib.pyplot as plt

plt.hist(df["logPontos"])
plt.grid(True)
plt.show()
