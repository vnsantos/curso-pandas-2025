#%%

import pandas as pd

idades = [
    32,38,30,31,23,27,32,37
]

series_idades = pd.Series(idades)
series_idades

#%%

idades[0]
series_idades[0]

#%%

series_idades[-1]

#%%

series_idades = series_idades.sort_values()
series_idades

#%%

series_idades[0]

#%%

series_idades.iloc[0]

#%%

series_idades.iloc[-1]

#%%

series_idades.iloc[:3]

#%%

series_idades.iloc[::-1]

#%%

idades = [
    32,38,30,31,23,27,32,37
]

indexs = [
    "vinicius", "julia","pedro","maria","joao","aurora","alice","apolo"
]

series_idades = pd.Series(idades, index = indexs)
series_idades

#%%

series_idades.iloc[[4]]