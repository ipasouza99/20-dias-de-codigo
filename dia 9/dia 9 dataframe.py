import pandas as pd
import numpy as np 

data = {'vendas': [100,200,300,400,500,600,700,800,900,1000]}
df = pd.DataFrame(data) 

media = df['vendas'].mean()
mediana = df['vendas'].median()
desvio_padrao = df['vendas'].std() 
maximo = df['vendas'].max()
minimo = df['vendas'].min()

print(f"Valor da média é:", media)
print(f"Valor da Mediana é:", mediana)
print(f"Valor do Desvio Padrão é:", desvio_padrao)
print(f"Valor do Máximo é:", maximo)
print(f"Valor do Mínimo é:", minimo)




