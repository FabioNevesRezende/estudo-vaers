import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np


df2018 = pd.read_csv('2018VAERSVAX.csv', encoding="Windows-1252") # https://vaers.hhs.gov/eSubDownload/index.jsp?fn=2018VAERSVAX.csv
df2019 = pd.read_csv('2019VAERSVAX.csv', encoding="Windows-1252") # https://vaers.hhs.gov/eSubDownload/index.jsp?fn=2019VAERSVAX.csv
df2020 = pd.read_csv('2020VAERSVAX.csv', encoding="Windows-1252") # https://vaers.hhs.gov/eSubDownload/index.jsp?fn=2020VAERSVAX.csv
df2021 = pd.read_csv('2021VAERSVAX.csv', encoding="Windows-1252") # https://vaers.hhs.gov/eSubDownload/index.jsp?fn=2021VAERSVAX.csv
df2022 = pd.read_csv('2022VAERSVAX.csv', encoding="Windows-1252") # https://vaers.hhs.gov/eSubDownload/index.jsp?fn=2022VAERSVAX.csv
df2023 = pd.read_csv('2023VAERSVAX.csv', encoding="Windows-1252") # https://vaers.hhs.gov/eSubDownload/index.jsp?fn=2023VAERSVAX.csv

# print(df2018.head())

# print(f'registros {df2023.shape[0]}') # 128319
# print(f'variáveis {df2023.shape[1]}') # 8

# eventos adversos (AE) por ano:

dfAe = pd.DataFrame({'Ano':['2018','2019','2020','2021','2022','2023'], 
                     'AE': [df2018.shape[0],df2019.shape[0],df2020.shape[0],df2021.shape[0],df2022.shape[0],df2023.shape[0]]})


colunasUteis = ['VAX_TYPE']

df2018 = df2018[colunasUteis]
df2019 = df2019[colunasUteis]
df2020 = df2020[colunasUteis]
df2021 = df2021[colunasUteis]
df2022 = df2022[colunasUteis]
df2023 = df2023[colunasUteis]

df2020['VAX_TYPE'] = df2020['VAX_TYPE'].replace('COVID19-2','COVID19')
df2021['VAX_TYPE'] = df2021['VAX_TYPE'].replace('COVID19-2','COVID19')
df2022['VAX_TYPE'] = df2022['VAX_TYPE'].replace('COVID19-2','COVID19')
df2023['VAX_TYPE'] = df2023['VAX_TYPE'].replace('COVID19-2','COVID19')

''' 
print(df2021['VAX_TYPE'].unique())
['COVID19' 'FLUC4' 'DTAPHEPBIP' 'HIBV' 'PNC13' 'RV1' 'UNK' 'FLU4' 'PPV'
 'FLUA3' 'VARZOS' 'MMR' 'DT' 'HPV9' 'DTAP' 'MMRV' 'TDAP' 'FLUR4'
 'DTAPIPVHIB' 'HEPA' 'MNQ' 'FLUX' 'YF' 'ANTH' 'HEP' 'VARCEL' 'RV5' 'HPV4'
 'MENB' 'IPV' 'RAB' 'FLUA4' 'FLUN4' 'DTAPIPV' 'TYP' 'ADEN_4_7' 'CHOL'
 'TTOX' 'FLU3' 'FLUC3' 'HEPAB' 'TD' 'EBZR' 'PNC' 'DF' 'HPVX' 'FLUX(H1N1)'
 'RVX' 'DTP' 'MEN' 'JEV1' 'BCG' 'PER' 'SMALL' 'OPV' 'TDAPIPV' 'FLUN3'
 'FLU(H1N1)' '6VAX-F' 'MNQHIB' 'DTPHEP' 'JEVX' 'DTPPVHBHPB' 'FLUR3' 'DTOX'
 'MU' 'HEPATYP' 'PNC10' 'H5N1']

print(df2022['VAX_TYPE'].unique())
 ['HPV9' 'COVID19' 'FLUX' 'UNK' 'FLU3' 'DTAP' 'HIBV' 'IPV' 'PPV' 'RVX' 'YF'
 'DTAPIPVHIB' 'DTAPIPV' 'MMR' 'VARCEL' 'TDAP' 'FLU4' 'MNQ' 'TYP' 'FLUR4'
 'FLUC4' 'VARZOS' 'HEP' 'HEPA' 'RV5' 'MENB' 'MMRV' 'PNC13' 'TD' 'FLUA4'
 'DTAPHEPBIP' 'RV1' 'ADEN_4_7' 'FLUN4' 'DTPPVHBHPB' 'DF' 'ANTH' 'HPV4'
 'PNC' 'HEPAB' 'FLUC3' 'RAB' 'EBZR' 'FLUN3' 'PNC20' 'DT' 'MEN' 'FLUR3'
 'BCG' 'JEV1' 'PNC15' 'TTOX' 'HPVX' 'FLUX(H1N1)' 'DTAPH' 'DTP' 'FLUA3'
 'CHOL' 'SMALLMNK' 'PNC10' 'SMALL' 'HPV2' 'TBE' 'DTOX' 'JEVX' '6VAX-F'
 'LYME']

print(df2023['VAX_TYPE'].unique())
['COVID19' 'TDAP' 'UNK' 'FLUA4' 'SMALLMNK' 'VARZOS' 'FLUX' 'FLU4' 'HIBV'
 'HPV4' 'HPV9' 'HEPA' 'RV5' 'MNQ' 'DTAPIPV' 'DTAP' 'FLUC4' 'HEP' 'PNC20'
 'TD' 'DTAPIPVHIB' 'MMR' 'MMRV' 'MENB' 'PNC13' 'VARCEL' 'DTAPHEPBIP' 'RV1'
 'PPV' 'FLUN3' 'DTPPVHBHPB' 'FLUR4' 'IPV' 'TYP' 'YF' 'HEPAB' 'FLUN4' 'RVX'
 'PNC15' 'ADEN_4_7' 'ANTH' 'FLU3' 'FLUC3' 'SMALL' 'MEN' 'RAB' 'HPVX'
 'FLUR3' 'DT' 'PNC' 'JEV1' 'BCG' 'TTOX' 'MEA' 'MU' 'FLUA3' 'TBE' 'DF'
 'DTOX' 'DTP' 'RSV' 'CHOL']
'''


totalAeCovid2021 = df2021.loc[( df2021['VAX_TYPE'] == 'COVID19'  )]['VAX_TYPE'].count()
totalAeCovid2022 = df2022.loc[( df2022['VAX_TYPE'] == 'COVID19'  )]['VAX_TYPE'].count()
totalAeCovid2023 = df2023.loc[( df2023['VAX_TYPE'] == 'COVID19'  )]['VAX_TYPE'].count()

print(f'Total AE covid 2021: {totalAeCovid2021}') # total AE covid = 742160
print(f'Total AE covid 2022: {totalAeCovid2022}') # total AE covid = 232270
print(f'Total AE covid 2023: {totalAeCovid2023}') # total AE covid = 77501

percentAeCovid2021 = (totalAeCovid2021 / df2021.shape[0])*100
percentAeCovid2022 = (totalAeCovid2022 / df2022.shape[0])*100
percentAeCovid2023 = (totalAeCovid2023 / df2023.shape[0])*100
print(f'% AE covid em relação a todas as vacinas 2021: {percentAeCovid2021}') # total % AE covid 2021 = 93.10%
print(f'% AE covid em relação a todas as vacinas 2022: {percentAeCovid2022}') # total % AE covid 2022 = 81.92%
print(f'% AE covid em relação a todas as vacinas 2023: {percentAeCovid2023}') # total % AE covid 2023 = 60.39%

df2018 = df2018.groupby('VAX_TYPE').value_counts().sort_values(ascending=False).reset_index(name='counts')
df2019 = df2019.groupby('VAX_TYPE').value_counts().sort_values(ascending=False).reset_index(name='counts')
df2020 = df2020.groupby('VAX_TYPE').value_counts().sort_values(ascending=False).reset_index(name='counts')
df2021 = df2021.groupby('VAX_TYPE').value_counts().sort_values(ascending=False).reset_index(name='counts')
df2022 = df2022.groupby('VAX_TYPE').value_counts().sort_values(ascending=False).reset_index(name='counts')
df2023 = df2023.groupby('VAX_TYPE').value_counts().sort_values(ascending=False).reset_index(name='counts')

fig, axs = plt.subplots(nrows=3, ncols=2, figsize=(10,5))

maxVaxAno = 8
ylimGeral = 750000

axs[0][0].bar(df2018['VAX_TYPE'][:maxVaxAno], df2018['counts'][:maxVaxAno])
axs[0][0].set_ylim(0, ylimGeral)
axs[0][0].set_title(f'Top {maxVaxAno} eventos adversos 2018 por tipo de vacina')

axs[0][1].bar(df2019['VAX_TYPE'][:maxVaxAno], df2019['counts'][:maxVaxAno])
axs[0][1].set_ylim(0, ylimGeral)
axs[0][1].set_title(f'Top {maxVaxAno} eventos adversos 2019 por tipo de vacina')

axs[1][0].bar(df2020['VAX_TYPE'][:maxVaxAno], df2020['counts'][:maxVaxAno])
axs[1][0].set_ylim(0, ylimGeral)
axs[1][0].set_title(f'Top {maxVaxAno} eventos adversos 2020 por tipo de vacina')

axs[1][1].bar(df2021['VAX_TYPE'][:maxVaxAno], df2021['counts'][:maxVaxAno])
axs[1][1].set_ylim(0, ylimGeral)
axs[1][1].set_title(f'Top {maxVaxAno} eventos adversos 2021 por tipo de vacina')

axs[2][0].bar(df2022['VAX_TYPE'][:maxVaxAno], df2022['counts'][:maxVaxAno])
axs[2][0].set_ylim(0, ylimGeral)
axs[2][0].set_title(f'Top {maxVaxAno} eventos adversos 2022 por tipo de vacina')

axs[2][1].bar(df2023['VAX_TYPE'][:maxVaxAno], df2023['counts'][:maxVaxAno])
axs[2][1].set_ylim(0, ylimGeral)
axs[2][1].set_title(f'Top {maxVaxAno} eventos adversos 2023 por tipo de vacina')

fig2, ax = plt.subplots(nrows=1, ncols=1, figsize=(10,5))
ax.bar(dfAe['Ano'], dfAe['AE'])
ax.set_title('Eventos adversos por ano')

fig3, axpie = plt.subplots(nrows=1, ncols=3, figsize=(10,5))
pieLabels = ['AE covid vax', 'AE outros']
axpie[0].pie( np.array([ percentAeCovid2021, 100-percentAeCovid2021]), labels=pieLabels, autopct='%1.1f%%' )
axpie[0].set_title('% AE covid versus outras vacinas 2021')
axpie[1].pie( np.array([ percentAeCovid2022, 100-percentAeCovid2022]), labels=pieLabels, autopct='%1.1f%%' )
axpie[1].set_title('% AE covid versus outras vacinas 2022')
axpie[2].pie( np.array([ percentAeCovid2023, 100-percentAeCovid2023]), labels=pieLabels, autopct='%1.1f%%' )
axpie[2].set_title('% AE covid versus outras vacinas 2023')


plt.show()