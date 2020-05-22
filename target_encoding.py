"""
Example of creating a target encoding for category (cat)
from a target column (y) with more than two categories
"""
import pandas as pd

df = pd.DataFrame({'cat': list('AABBCCC'), 'y': [1, 1, 0, 1, 0, 0, 1],
                   'func': ['func', 'rep', 'nonf', 'func', 'nonf', 'nonf', 'func']
})

ydummy = pd.get_dummies(df['func'])
df = pd.concat([df, ydummy], axis=1)

target_means = df.groupby('cat').mean()

df['cat_func'] = df['cat'].replace(target_means['func'])
df['cat_nonf'] = df['cat'].replace(target_means['nonf'])
