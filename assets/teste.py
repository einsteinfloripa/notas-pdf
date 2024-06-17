import pandas as pd

# Supondo que você tenha um DataFrame `df`
df = pd.DataFrame({
    'coluna1': [1, 2, 3, 4],
    'coluna2': ['a', 'b', 'c', 'd']
})
print(df)
# Valor que você está procurando
indices = df.index[df['coluna1'] == 3].tolist()

print(indices)


# Encontra todas as linhas onde `coluna1` é igual a `valor`

