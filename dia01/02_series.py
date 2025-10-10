#%%

idades = [
    32,38,30,31,23,27,32,37
]

idades

media = sum(idades) / len(idades)
print("Media: ", media)

diffs = 0

for i in idades:
    diffs += (i - media) ** 2

variancia = diffs / (len(idades)-1)

print("Variância:", variancia)

#%%

import pandas as pd

idades = [
    32,38,30,31,23,27,32,37
]

series_idades = pd.Series(idades)
series_idades

#%%

media_idades = series_idades.mean()
var_idades = series_idades.var()
summary_idades = series_idades.describe()
summary_idades