
""" IMPORTAÇÃO DE BIBLIOTECAS """

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")

""" IMPORTAÇÃO DO ARQUIVO .CSV """

df =pd.read_csv('importacoes-exportacoes-etanol-2012-2025.csv', sep = ';')

""" ANÁLISE EXPLORATÓRIA DOS DADOS """

df.info()
df.describe()

""" FORMATANDO COLUNA COMO NUMÉRICA """

df['importado/exportado'] = pd.to_numeric(df['importado/exportado'], errors='coerce')
df['data'] = pd.to_datetime(df['data'])

""" SOMA DE RECEITA POR PRODUTO """

soma_receita = ((df[df['operacao_comercial'] == 'EXPORTAÇÃO']).groupby('produto')['dispendio/receita'].sum()/1000000000).round(2)

fig,ax = plt.subplots(figsize=(5,3))
p = ax.barh(soma_receita.index, soma_receita.values)
ax.bar_label(p)
ax.set_title('Receita Total Exportação (em bilhões de US$)')
ax.spines[['top', 'right']].set_visible(False)

""" SOMA DE RECEITA AO LONGO DO ANO POR PRODUTO """

soma_receita_hidratado = ((df[(df['operacao_comercial'] == 'EXPORTAÇÃO')&
                              (df['produto'] == 'ETANOL HIDRATADO')]).groupby(df['data'].dt.to_period('Y'))['dispendio/receita'].sum()/1000000000).round(2).reset_index()
soma_receita_hidratado['data'] = soma_receita_hidratado['data'].dt.to_timestamp()

soma_receita_anidro = ((df[(df['operacao_comercial'] == 'EXPORTAÇÃO')&
                           (df['produto'] == 'ETANOL ANIDRO')]).groupby(df['data'].dt.to_period('Y'))['dispendio/receita'].sum()/1000000000).round(2).reset_index()
soma_receita_anidro['data'] = soma_receita_anidro['data'].dt.to_timestamp()

fig, ax = plt.subplots(figsize=(11,5))
ax.plot(soma_receita_hidratado['data'], soma_receita_hidratado['dispendio/receita'],soma_receita_hidratado['data'], soma_receita_anidro['dispendio/receita'])
ax.legend(bbox_to_anchor=(1, 1))
ax.set_xlabel('Ano')
ax.set_title('Receita Exportação (em bilhões de US$)')
ax.legend(['Hidratado', 'Anidro'])
ax.spines[['top', 'right']].set_visible(False)

for x,y,y2 in zip(soma_receita_hidratado['data'], soma_receita_hidratado['dispendio/receita'], soma_receita_anidro['dispendio/receita']):
    ax.text(x, y, str(y),
    ha = 'center',
    va = 'bottom')
    ax.text(x, y2, str(y2),
    ha = 'center',
    va = 'bottom')
    
""" VOLUME EXPORTADO POR PRODUTO  """

soma_volume = ((df[df['operacao_comercial'] == 'EXPORTAÇÃO']).groupby('produto')['importado/exportado'].sum()/1000000000).round(2)

fig,ax = plt.subplots(figsize=(5,3))
gb = ax.barh(soma_volume.index, soma_volume.values)
ax.set_title('Volume Exportado por Produto (em bilhões de litros)')
ax.bar_label(gb)
ax.spines[['top', 'right']].set_visible(False)

""" VOLUME EXPORTADO POR PRODUTO AO LONGO DO ANO """

soma_volume_hidratado = ((df[(df['operacao_comercial'] == 'EXPORTAÇÃO')&
                             (df['produto'] == 'ETANOL HIDRATADO')]).groupby(df['data'].dt.to_period('Y'))['importado/exportado'].sum()/1000000000).round(2).reset_index()
soma_volume_hidratado['data'] = soma_volume_hidratado['data'].dt.to_timestamp()

soma_volume_anidro = ((df[(df['operacao_comercial'] == 'EXPORTAÇÃO')&
                          (df['produto'] == 'ETANOL ANIDRO')]).groupby(df['data'].dt.to_period('Y'))['importado/exportado'].sum()/1000000000).round(2).reset_index()
soma_volume_anidro['data'] = soma_volume_anidro['data'].dt.to_timestamp()

fig, ax = plt.subplots(figsize=(11,5))
ax.plot(soma_volume_hidratado['data'], soma_volume_hidratado['importado/exportado'], soma_volume_hidratado['data'], soma_volume_anidro['importado/exportado'])
ax.legend(bbox_to_anchor=(1, 1))
ax.set_xlabel('Ano')
ax.set_title('Volume Exportado por Ano (em bilhões de litros)')
ax.spines[['top', 'right']].set_visible(False)
ax.legend(['Hidratado', 'Anidro'])

for x, y, y2 in zip(soma_volume_hidratado['data'], soma_volume_hidratado['importado/exportado'], soma_volume_anidro['importado/exportado']):
    ax.text(x,y,str(y),
            va = 'bottom',
            ha = 'center')
    ax.text(x,y2,str(y2),
            va = 'bottom',
            ha = 'center')
plt.show()