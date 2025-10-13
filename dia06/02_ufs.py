#%%

import pandas as pd
import requests

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.44472.124 Safari/537.36'
}

response = requests.get(url, headers=headers)

dfs = pd.read_html(response.text)
uf = dfs[1]

uf

#%%

def str_to_float(x:str):    
        x = (x.replace(" ","")
                    .replace(",",".")
                    .replace("\xa0", "")
                    )
        return float(x)


#%%


uf["Área (km²)"] = uf["Área (km²)"].apply(str_to_float)
uf["População (Censo 2022)"] = uf["População (Censo 2022)"].apply(str_to_float)
uf["PIB (2015)"] = uf["PIB (2015)"].apply(str_to_float)
uf["PIB per capita (R$) (2015)"] = uf["PIB per capita (R$) (2015)"].apply(str_to_float)

#%%

def exp_to_anos(exp:str):
        return float(exp.replace(",",".")
                     .replace(" anos", ""))

uf["Expectativa de vida (2016)"] = uf["Expectativa de vida (2016)"].apply(exp_to_anos)

#%%

uf