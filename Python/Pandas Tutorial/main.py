import pandas as pd

poke = pd.read_csv('pokemon_data.csv')

# poke = pd.read_excel('pokemon_data.xlsx')

# poke = pd.read_csv('pokemon_data.txt')

# print(poke.tail(4))

# print(poke.aggregate)

# print(poke.columns)

# print(poke[['Name', 'Type 1']][0:5])

# print(poke.iloc[3,2])

# print(poke.sort_values(['Name']))

# poke['Total'] = poke['HP'] + poke['Attack'] + poke['Defense'] + poke['Sp. Atk'] + poke['Sp. Def'] + poke['Speed']

# poke = poke.drop(columns=['Total'])

# print(poke.head(5))

# poke['Total'] = poke.iloc[:, 4:10].sum(axis=1)

# cols = list(poke.columns)
# poke = poke[cols[0:4] + [cols[-1]]+cols[4:12]]

# poke = pd.read_csv('modified.csv')

# poke['count'] = 1

# poke.groupby(['Type 1', 'Type 2']).count()['count']

# poke.to_csv('modified.csv', index=False)

#poke.to_excel('modified.xlsx', index=False)

# poke.to_csv('modified.txt', index=False, sep='\t')

# new_poke = poke.loc[(poke['Type 1'] == 'Grass') & (poke['Type 2'] == 'Poison') & (poke['HP'] > 70)]

# new_poke.reset_index(drop=True, inplace=True)

# new_poke.to_csv('filtered.csv')

# import re

# poke.loc[poke['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)]

# poke.loc[poke['Total'] > 500, ['Generation', 'Legendary']] = ['Test 1', 'Test 2']

print(poke.head(5))